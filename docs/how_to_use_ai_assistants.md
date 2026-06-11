# How To Use AI Assistants Smartly

## The Point

The hackathon is about using AI smartly, not proving you can do everything
alone.

Use assistants for speed, but keep judgment with the team.

## Use Claude Code/Codex For

- creating the first harness
- adapting CSV loading
- writing scoring code
- debugging stack traces
- generating prompt variants
- adding structured output parsing
- creating final README/demo notes
- refactoring messy code

## Use ChatGPT/Claude Chat For

- understanding domain task
- brainstorming failure modes
- writing judge-facing explanations
- turning messy notes into demo narrative
- asking "what are we missing?"
- generating edge cases

## Do Not Use Assistants Blindly For

- deciding final architecture without measuring
- inventing domain facts
- hiding errors
- generating fake metrics
- creating overly complex code you cannot explain

## Good Assistant Prompts

### Dataset Understanding

```text
Here are the dataset columns and 5 sample rows.
What is the likely task?
What output schema should we use?
What failure modes should we expect?
```

### Eval Design

```text
We need to evaluate this agent output.
Expected column is X.
Predicted output is Y.
Suggest simple deterministic metrics first, then optional LLM rubric.
```

### Prompt Improvement

```text
Here are 10 failures from baseline.
Group them into failure types.
Suggest the smallest prompt/tool/retrieval changes to fix the biggest group.
```

### Demo Prep

```text
We improved from baseline score X to final score Y.
Failure modes were A, B, C.
Optimizations were D, E, F.
Create a 3-minute demo script for enterprise AI judges.
```

## Keep A Human Loop

Every 45-60 minutes, pause and ask:

- Did the score improve?
- Did complexity increase too much?
- Can we explain this to judges?
- Is this enterprise-relevant?
- What is the next highest-impact change?

