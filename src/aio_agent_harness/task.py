from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class TaskExample:
    example_id: str
    input_text: str
    expected: str | None = None


@dataclass
class AgentPrediction:
    example_id: str
    answer: str
    rationale: str
    version: str


def build_prompt(example: TaskExample) -> str:
    return f"""You are a reliable enterprise AI agent.

Task:
Read the input and produce the best possible answer for the business task.

Input:
{example.input_text}

Return a concise, structured answer.
"""


def baseline_agent(example: TaskExample) -> AgentPrediction:
    """Baseline agent.

    If AIO_MODEL is set and the matching API key exists, this calls a real
    model through LiteLLM. Otherwise it returns a placeholder so the harness can
    still be tested without spending money.
    """
    prompt = build_prompt(example)
    model = os.getenv("AIO_MODEL", "").strip()
    if model:
        try:
            from litellm import completion

            response = completion(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
            )
            answer = response.choices[0].message.content or ""
            return AgentPrediction(
                example_id=example.example_id,
                answer=answer,
                rationale=f"Model call through LiteLLM using {model}.",
                version=f"baseline-{model}",
            )
        except Exception as exc:
            return AgentPrediction(
                example_id=example.example_id,
                answer=f"MODEL_CALL_FAILED: {exc}",
                rationale="Model call failed. Check .env, provider key, and model name.",
                version=f"baseline-{model}-failed",
            )

    return AgentPrediction(
        example_id=example.example_id,
        answer=prompt,
        rationale="Baseline placeholder. Replace with model output.",
        version="baseline-v0",
    )


def score_prediction(example: TaskExample, prediction: AgentPrediction) -> dict:
    """Task-specific scoring goes here once the dataset/rules are known."""
    exact_match = (
        example.expected is not None
        and prediction.answer.strip().lower() == example.expected.strip().lower()
    )
    return {
        "example_id": example.example_id,
        "version": prediction.version,
        "exact_match": exact_match,
        "has_answer": bool(prediction.answer.strip()),
    }
