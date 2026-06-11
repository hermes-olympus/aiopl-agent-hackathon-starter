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
│   ├── eval_harness_notes.md
│   ├── laptop_readiness.md
│   ├── prompt_patterns.md
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
