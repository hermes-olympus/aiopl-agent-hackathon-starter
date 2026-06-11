# Cost Budgeting

## Is 5 USD Enough?

For a disciplined hackathon run, yes, 5 USD can be enough on a mini model.

It is not enough if you:

- rerun the full dataset repeatedly
- use large prompts for every row
- use multi-agent loops for every example
- generate long answers
- forget to cache/save outputs
- use expensive flagship models for every iteration

## GPT-5.4 Mini Reference Pricing

OpenAI's model page lists GPT-5.4 mini text pricing as:

- Input: 0.75 USD per 1M tokens
- Cached input: 0.075 USD per 1M tokens
- Output: 4.50 USD per 1M tokens

Official model page:

- https://developers.openai.com/api/docs/models/gpt-5.4-mini

Pricing can change, so check the pricing page before the event:

- https://openai.com/api/pricing/

## Rough Call Estimates For 5 USD

These are rough examples.

### Small Classification Task

Per row:

- 1,500 input tokens
- 300 output tokens

Approx cost:

- input: 0.001125 USD
- output: 0.00135 USD
- total: 0.002475 USD per row

5 USD buys roughly 2,000 calls.

### Medium Enterprise Task

Per row:

- 3,000 input tokens
- 800 output tokens

Approx cost:

- input: 0.00225 USD
- output: 0.00360 USD
- total: 0.00585 USD per row

5 USD buys roughly 850 calls.

### Retrieval-Heavy Task

Per row:

- 10,000 input tokens
- 1,000 output tokens

Approx cost:

- input: 0.00750 USD
- output: 0.00450 USD
- total: 0.01200 USD per row

5 USD buys roughly 400 calls.

## Practical Hackathon Budget Plan

Use this sequence:

1. No-key placeholder mode to test code.
2. 5-row API test.
3. 20-row baseline.
4. 50-row optimization loop.
5. 100-row comparison between best versions.
6. Full run only near the end.

## How To Avoid Burning Money

- Keep prompts short.
- Do not include huge context unless needed.
- Use retrieval to include only relevant chunks.
- Save every run to `runs/*.jsonl`.
- Reuse outputs; do not rerun the same version.
- Set temperature to 0 for stable evaluation.
- Use cheap models for iteration.
- Use stronger models only for final or hard examples.
- Avoid verifier calls on every row unless they improve score.
- Add deterministic validation before another model call.

## Simple Cost Formula

```text
cost = (input_tokens / 1_000_000 * input_price)
     + (output_tokens / 1_000_000 * output_price)
```

For GPT-5.4 mini:

```text
cost = (input_tokens / 1_000_000 * 0.75)
     + (output_tokens / 1_000_000 * 4.50)
```

## My Rule For A 5 USD Budget

If using GPT-5.4 mini:

- Keep early runs under 50 rows.
- Keep outputs short.
- Do not use multi-agent loops at first.
- Save every result.
- Do one final larger run after the prompt is stable.

That should be enough for a serious hackathon workflow.

## Better Two-Model Strategy

Use GPT-5.4 nano for cheap checking and GPT-5.4 mini for final quality.

Recommended flow:

1. Placeholder mode: test code without API spend.
2. GPT-5.4 nano: first API tests, prompt debugging, schema checks, small evals.
3. GPT-5.4 nano: repeated 20-50 row optimization loops.
4. GPT-5.4 mini: compare best 1-2 approaches on a larger sample.
5. GPT-5.4 mini: final eval run after the prompt/harness is stable.

This is better than using mini for everything.

## Nano vs Mini

Use nano for:

- cheap smoke tests
- classification
- extraction
- JSON formatting checks
- failure analysis drafts
- prompt iteration
- running many rows

Use mini for:

- final eval
- harder reasoning examples
- domain-sensitive output
- final demo examples
- cases where nano fails consistently

Do not use the expensive model until you know exactly what you are asking it to
do.

## Example Budget Split

For a 5 USD budget:

- 1 USD on nano for experiments
- 3 USD on mini for final comparisons/runs
- 1 USD reserve for debugging and emergency reruns

If nano performs well enough, spend even less on mini.
