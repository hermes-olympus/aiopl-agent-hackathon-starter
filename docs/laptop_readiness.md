# Laptop Readiness

## Essentials

- Python 3.11+
- `uv`
- git
- GitHub account logged in
- at least one model API key
- one backup model API key
- browser logged into event/platform accounts
- charger
- hotspot backup

## Recommended API Providers

Have keys ready for at least two:

- OpenAI
- Anthropic
- Google Gemini
- Groq
- Together/OpenRouter

Use one primary provider and one backup. Do not debug too many providers during
the event.

## Local Setup

```bash
uv sync
cp .env.example .env
uv run aio-harness run data/sample.csv runs/baseline.jsonl
uv run aio-harness evaluate runs/baseline.jsonl
```

## Optional Tools

- Docker
- VS Code or Cursor
- sqlite
- jq
- ripgrep
- Claude Code / Codex / another coding agent

## Hackathon Folder Habit

Keep outputs organized:

```text
runs/
  baseline.jsonl
  schema_v1.jsonl
  fewshot_v2.jsonl
  retrieval_v3.jsonl
notes/
  failures.md
  final_demo.md
```

