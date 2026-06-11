# AIOPL Agent Hackathon Starter

Eval-first starter kit for AI Optimization Premier League style hackathons,
where teams build and optimize domain-specific enterprise AI agents.

The core idea: build the evaluation harness before making the agent fancy.

## What This Helps With

- Loading hackathon datasets
- Running a baseline agent
- Saving predictions as JSONL
- Creating task-specific evaluation
- Comparing prompt/tool/retrieval iterations
- Preparing a strong final demo story

## Repository Structure

```text
.
├── data/sample.csv
├── docs/
│   ├── agent_optimization_playbook.md
│   ├── api_keys_first_time.md
│   ├── cost_budgeting.md
│   ├── eval_harness_notes.md
│   ├── first_hackathon_guide.md
│   ├── harness_tutorial.md
│   ├── how_to_use_ai_assistants.md
│   ├── laptop_readiness.md
│   ├── prompt_patterns.md
│   ├── questions_for_organizers.md
│   └── study_material.md
├── src/aio_agent_harness/
│   ├── cli.py
│   └── task.py
└── pyproject.toml
```

## Setup

```bash
uv sync
cp .env.example .env
```

Add API keys to `.env` if needed.

If you do not set `AIO_MODEL`, the harness runs in no-spend placeholder mode.
That is useful for testing the flow.

When you are ready to call a real model, set one provider key and `AIO_MODEL` in
`.env`.

Example:

```bash
OPENAI_API_KEY=sk-...
AIO_MODEL=openai/your-model-name
```

Check current model names in the provider dashboard/docs before the hackathon.

## Expected Flow

1. Put dataset files in `data/`.
2. Edit `src/aio_agent_harness/task.py` for the given task.
3. Run a baseline.
4. Inspect outputs.
5. Improve prompts/tools.
6. Compare runs.

## Commands

```bash
uv run aio-harness run data/sample.csv runs/baseline.jsonl
uv run aio-harness evaluate runs/baseline.jsonl
```

This starter is intentionally small. Add framework code only when the task
demands it.

## Hackathon Strategy

1. Inspect dataset and expected output.
2. Build baseline fast.
3. Create the eval loop.
4. Find failure types.
5. Improve prompts, tools, retrieval, memory, and validators.
6. Compare every change against the baseline.
7. Tell the final story with measured improvement.

Do not spend the first half of the hackathon building a complex UI or a
multi-agent architecture unless the task clearly needs it.

## First-Time Hackathon Reading Order

1. `docs/first_hackathon_guide.md`
2. `docs/api_keys_first_time.md`
3. `docs/cost_budgeting.md`
4. `docs/harness_tutorial.md`
5. `docs/agent_optimization_playbook.md`
6. `docs/eval_harness_notes.md`
7. `docs/prompt_patterns.md`
8. `docs/questions_for_organizers.md`
9. `docs/how_to_use_ai_assistants.md`
