from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import typer
from rich import print

from aio_agent_harness.task import TaskExample, baseline_agent, score_prediction

app = typer.Typer(no_args_is_help=True)


def _load_examples(input_path: Path) -> list[TaskExample]:
    df = pd.read_csv(input_path)
    examples: list[TaskExample] = []
    for idx, row in df.iterrows():
        example_id = str(row.get("id", idx))
        input_text = str(row.get("input", row.get("text", row.to_dict())))
        expected = row.get("expected")
        examples.append(
            TaskExample(
                example_id=example_id,
                input_text=input_text,
                expected=None if pd.isna(expected) else str(expected),
            )
        )
    return examples


@app.command()
def run(input: Path, output: Path) -> None:
    """Run the current agent over a CSV dataset."""
    output.parent.mkdir(parents=True, exist_ok=True)
    examples = _load_examples(input)
    with output.open("w", encoding="utf-8") as handle:
        for example in examples:
            prediction = baseline_agent(example)
            handle.write(json.dumps(prediction.__dict__, ensure_ascii=False) + "\n")
    print(f"[green]Wrote {len(examples)} predictions to {output}[/green]")


@app.command()
def evaluate(predictions: Path) -> None:
    """Placeholder evaluator for prediction JSONL files."""
    rows = []
    with predictions.open("r", encoding="utf-8") as handle:
        for line in handle:
            rows.append(json.loads(line))
    print(f"[cyan]Loaded {len(rows)} predictions from {predictions}[/cyan]")
    print("[yellow]Edit task-specific scoring once the hackathon dataset is known.[/yellow]")


def main() -> None:
    app()

