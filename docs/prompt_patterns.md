# Prompt Patterns

## Structured Output Prompt

```text
You are a reliable enterprise AI agent.

Task:
...

Rules:
- Return only valid JSON.
- Do not include unsupported facts.
- If confidence is low, set "needs_review": true.

Schema:
{
  "label": "...",
  "confidence": 0.0,
  "reason": "...",
  "needs_review": false
}

Input:
...
```

## Few-Shot Prompt

```text
Examples:

Input: ...
Output: ...

Input: ...
Output: ...

Now solve:
Input: ...
Output:
```

## Retrieval-Grounded Prompt

```text
Use only the provided context.
If the context is insufficient, say so.

Context:
...

Task input:
...
```

## Verifier Prompt

```text
Check whether this output satisfies the task rules.
Return JSON:
{
  "valid": true/false,
  "issues": [],
  "fixed_output": ...
}
```

## Enterprise Safety Pattern

```text
Prefer conservative, auditable answers.
Do not invent policy, prices, medical advice, legal advice, or financial facts.
Escalate uncertain cases.
```

