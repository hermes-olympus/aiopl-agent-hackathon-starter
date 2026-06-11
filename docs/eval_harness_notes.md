# Eval Harness Notes

## Why Eval First

Agent quality is hard to feel by intuition. A harness makes improvement visible.

At minimum, every run should record:

- example id
- input
- output
- expected output if available
- model/provider
- prompt version
- tool/retrieval version
- score
- error notes

## JSONL Prediction Format

Example:

```json
{"example_id":"42","answer":"billing_escalation","rationale":"Duplicate charge mentioned.","version":"fewshot-v2"}
```

## Metrics By Task Type

### Classification

- accuracy
- precision/recall/F1
- confusion matrix

### Extraction

- field-level exact match
- missing field count
- invalid field count

### Generation

- rubric score
- constraint pass/fail
- citation correctness
- human spot checks

### Tool Tasks

- tool success rate
- tool error rate
- final task success
- latency
- cost

## Error Analysis Prompts

Use a separate analysis pass:

```text
Compare expected and predicted output.
Return the failure type and a one-line explanation.
Allowed failure types: format_error, missing_field, wrong_label,
unsupported_claim, insufficient_context, calculation_error, other.
```

Do not let this replace deterministic scoring when deterministic scoring is
possible.

