# Harness Tutorial

## What Is A Harness?

A harness is the repeatable machine around your agent.

It:

- loads examples
- calls your agent
- saves predictions
- scores outputs
- helps compare versions

Without a harness, you are just chatting with a model.

## Current Starter Flow

```text
CSV dataset
  -> _load_examples()
  -> baseline_agent()
  -> JSONL predictions
  -> evaluate()
```

Files:

- `src/aio_agent_harness/cli.py`: command line runner
- `src/aio_agent_harness/task.py`: task prompt, agent, scoring placeholder
- `data/sample.csv`: tiny sample dataset

## Run Placeholder Mode

No API key needed:

```bash
uv run aio-harness run data/sample.csv runs/baseline.jsonl
uv run aio-harness evaluate runs/baseline.jsonl
```

## Run Real Model Mode

Set `.env`:

```bash
OPENAI_API_KEY=...
AIO_MODEL=openai/your-model-name
```

Then:

```bash
uv run aio-harness run data/sample.csv runs/model_test.jsonl
```

## Adapting To Hackathon Dataset

When organizers provide data, inspect columns:

```bash
python - <<'PY'
import pandas as pd
df = pd.read_csv("data/your_dataset.csv")
print(df.head())
print(df.columns)
print(df.shape)
PY
```

Then edit `_load_examples()` in `cli.py` if columns are different.

Most common input columns:

- `input`
- `text`
- `query`
- `message`
- `ticket`
- `description`

Most common expected columns:

- `expected`
- `label`
- `answer`
- `target`
- `ground_truth`

## Creating A Better Score

Edit `score_prediction()` in `task.py`.

Classification example:

```python
exact_match = prediction.answer.strip().lower() == example.expected.strip().lower()
```

Structured JSON example:

```python
import json

try:
    obj = json.loads(prediction.answer)
    valid_json = True
except json.JSONDecodeError:
    valid_json = False
```

## Versioning Runs

Use filenames:

```text
runs/baseline_v0.jsonl
runs/schema_v1.jsonl
runs/fewshot_v2.jsonl
runs/retrieval_v3.jsonl
runs/verifier_v4.jsonl
```

Keep notes:

```text
version | change | score | notes
v0 | baseline | 42% | many format errors
v1 | JSON schema | 61% | fewer format errors
v2 | few-shot | 70% | improved labels
```

## The Demo Value

The harness lets you say:

> Our baseline was weak. We measured failures, optimized the system, and improved
> reliability from X to Y.

That is a better story than "we used a powerful model."

