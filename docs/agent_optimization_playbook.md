# Agent Optimization Playbook

## Principle

Optimize with evidence. Every prompt, retrieval, tool, or verifier change should
be connected to a measured failure mode.

## Step 1: Understand The Task

Write down:

- input fields
- output fields
- scoring metric
- domain constraints
- allowed tools/data
- examples of correct output
- examples of risky output

## Step 2: Build Baseline

Use one simple prompt:

```text
You are a reliable enterprise AI agent.
Given the input, complete the task.
Return only valid JSON matching this schema:
...
```

Save predictions.

## Step 3: Build Evaluation

Start with simple metrics:

- exact match for labels
- JSON validity
- required fields present
- similarity or rubric score for generated text
- policy violation count

Then add task-specific scoring.

## Step 4: Analyze Failures

Create an error table:

```text
id | expected | predicted | failure_type | note
```

Improve the highest-volume failure first.

## Step 5: Improve Agent

Common optimizations:

- add output schema
- add few-shot examples
- add domain rules
- add retrieval
- add deterministic tool
- add verifier
- split task into classification then generation
- add uncertainty/escalation behavior

## Step 6: Compare Versions

Name versions clearly:

- `baseline-v0`
- `schema-v1`
- `fewshot-v2`
- `retrieval-v3`
- `verifier-v4`

Keep a short note for each version:

- what changed
- why it changed
- metric impact
- new failure introduced

## Step 7: Prepare Demo

Tell a measured improvement story:

```text
Baseline: X
Main failures: A, B, C
Optimizations: prompt schema, retrieval, verifier
Final: Y
Enterprise impact: fewer errors, more consistent output, auditable process
```

