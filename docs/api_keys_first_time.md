# API Keys For First-Time Hackathon Builders

## The Mental Model

There are two different things:

1. **AI assistant subscription**: ChatGPT, Claude Code, Codex, Cursor, etc.
   These help you think, write code, debug, and design prompts.
2. **Runtime API key**: a secret token your app/script uses to call a model
   automatically while processing dataset rows.

For this hackathon, you can use your AI assistant subscriptions to build faster,
but your agent harness may still need a runtime API key.

## Should You Bring Your Own Key?

Yes. Assume you need your own key unless the organizers clearly provide credits
at check-in.

If organizers give credits, use them. But do not depend on it.

## Official Provider Links

- OpenAI Platform: https://platform.openai.com/
- Anthropic Console/API docs: https://docs.anthropic.com/en/docs/get-started
- Gemini API keys: https://ai.google.dev/gemini-api/docs/api-key
- Groq quickstart/API keys: https://console.groq.com/docs/quickstart

Notes from official docs:

- Anthropic says the Claude API is available through the Console and API keys
  are generated in account settings.
- Gemini API keys are associated with Google Cloud projects.
- Groq recommends setting API keys as environment variables.

## Safe Key Rules

- Never paste keys into GitHub.
- Never hard-code keys in Python files.
- Put keys in `.env`.
- Keep `.env` in `.gitignore`.
- Create a fresh hackathon/project key if possible.
- Delete or rotate the key after the event if it may have been exposed.
- Set a spend limit or billing alert in the provider dashboard.

## `.env` Example

```bash
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
GEMINI_API_KEY=your_gemini_key_here
GROQ_API_KEY=your_groq_key_here
AIO_MODEL=openai/your-model-name
```

Only one provider key is required for a first run. Two is safer.

## How This Starter Uses Keys

The starter uses `python-dotenv` to load `.env`, and LiteLLM to call models from
different providers.

If `AIO_MODEL` is empty, no paid model call is made.

If `AIO_MODEL` is set, `baseline_agent()` tries to call that model.

## Test Without Spending

```bash
uv run aio-harness run data/sample.csv runs/no_api.jsonl
uv run aio-harness evaluate runs/no_api.jsonl
```

This works without any API key.

## Test With A Real Model

1. Create `.env`.
2. Add one provider key.
3. Set `AIO_MODEL`.
4. Run a tiny sample first.

```bash
uv run aio-harness run data/sample.csv runs/api_test.jsonl
uv run aio-harness evaluate runs/api_test.jsonl
```

If the output says `MODEL_CALL_FAILED`, check:

- key exists in `.env`
- model name is correct
- billing/credits are enabled
- provider rate limit is not exceeded
- internet is working

## Spend Control

During the hackathon:

- Run 5 rows first.
- Then 20 rows.
- Then 50 rows.
- Only run full dataset when the harness and prompt are stable.
- Save outputs in `runs/`.
- Do not rerun the same version repeatedly.
- Use stronger models only for final or hard examples.

