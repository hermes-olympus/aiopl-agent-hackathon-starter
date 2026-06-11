# Study Material

Use this as quick prep before an enterprise AI agent optimization hackathon.

## Core Concepts

### Agent

An AI system that can take inputs, reason over a task, optionally use tools or
retrieval, and produce an action or answer.

In this hackathon, an agent is not just a chatbot. It is a task performer.

### Evaluation Harness

A repeatable system that runs the agent against examples and measures output
quality.

This matters because agent work without evals becomes guesswork.

### Baseline

The simplest working version of the system. Usually one prompt and no tools.

The baseline gives you something to beat.

### Error Taxonomy

A categorized list of failure types.

Examples:

- Missing required field
- Wrong classification
- Hallucinated policy
- Bad citation
- Weak reasoning
- Format error
- Did not use available context
- Over-escalated or under-escalated

### Retrieval

Fetching relevant reference material before the model answers.

Use retrieval when the task depends on domain rules, policies, product docs,
contracts, FAQs, or historical records.

### Tool Use

Letting the model call deterministic functions.

Good tools:

- lookup customer record
- calculate totals
- validate JSON
- search docs
- classify intent with fixed labels
- check policy constraints

Bad tools:

- vague "think harder" functions
- unnecessary APIs that slow the system
- anything that is not measured

### Verifier

A second pass that checks whether the output is complete, valid, and aligned
with task rules.

Use a verifier for high-stakes enterprise output, but keep it simple.

## Useful Things To Review

- JSON schemas and structured outputs
- Few-shot prompting
- Classification metrics: accuracy, precision, recall, F1
- Retrieval basics: chunking, keyword search, embeddings
- ReAct/tool calling pattern
- Self-consistency and verifier patterns
- Pydantic validation
- JSONL logs
- Confusion matrices
- Latency and cost tradeoffs

## Enterprise Agent Domains

### Customer Support

Tasks may include:

- intent classification
- urgency detection
- response drafting
- escalation routing
- policy-grounded answers

Optimization ideas:

- fixed label taxonomy
- policy retrieval
- escalation rules
- response tone constraints

### Finance

Tasks may include:

- invoice categorization
- anomaly detection
- transaction explanation
- cashflow summary
- risk scoring

Optimization ideas:

- deterministic calculations
- strict schemas
- anomaly thresholds
- conservative explanations

### Healthcare

Tasks may include:

- triage support
- summarization
- coding/classification
- intake routing

Optimization ideas:

- strong safety constraints
- no unsupported diagnosis
- cite provided context
- escalate uncertainty

### Sales Outreach

Tasks may include:

- lead scoring
- personalization
- follow-up drafting
- objection handling

Optimization ideas:

- persona extraction
- CRM context retrieval
- short persuasive output
- avoid overclaiming

## Final Demo Checklist

- Show baseline score
- Show optimization steps
- Show final score
- Show examples of fixed failures
- Explain enterprise value
- Explain reliability, safety, and cost considerations

