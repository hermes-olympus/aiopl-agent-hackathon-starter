from __future__ import annotations

from dataclasses import dataclass


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
    """Replace this with a real model call during the hackathon."""
    prompt = build_prompt(example)
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

