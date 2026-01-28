#!/usr/bin/env python
"""Run agent on all queries for a task and evaluate results."""

from argparse import ArgumentParser
from pathlib import Path
import os
import sys
import importlib.util

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from common_scaffold.DataAgent import DataAgent
import logging_config

def load_validate_func(query_dir: Path):
    """Load the validate function from a query's validate.py"""
    validate_py = query_dir / "validate.py"
    if not validate_py.exists():
        return None
    spec = importlib.util.spec_from_file_location("validate", str(validate_py))
    validate_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(validate_mod)
    return validate_mod.validate

def run_query(task: str, query_id: int, llm: str, iterations: int = 20):
    """Run agent on a single query and return the result."""
    print(f"\n{'='*60}")
    print(f"Running: task={task} query_id={query_id} llm={llm}")
    print(f"{'='*60}")

    db_dir = Path(os.path.dirname(__file__)) / f"query_{task}"
    query_dir = db_dir / f"query{query_id}"

    db_description_path = db_dir / "db_description.txt"
    db_description = db_description_path.read_text().strip()

    # Append hints if available
    db_hints_path = db_dir / "db_description_withhint.txt"
    if db_hints_path.exists():
        db_description += "\n\n" + db_hints_path.read_text().strip()

    db_config_path = db_dir / "db_config.yaml"

    data_agent = DataAgent(
        query_dir=query_dir,
        db_description=db_description,
        db_config_path=db_config_path,
        deployment_name=llm,
        exec_python_timeout=600,
        max_iterations=iterations,
    )

    try:
        result = data_agent.run()
    except Exception as e:
        print(f"Error during agent run: {e}")
        for tool in data_agent.tools.values():
            tool.clean_up()
        result = f"Error: {e}"

    return result

def main():
    parser = ArgumentParser(description="Run agent on all queries for a task")
    parser.add_argument("--task", type=str, required=True, help="Task name (e.g., civic_unstructured)")
    parser.add_argument("--llm", type=str, default="gpt-4o-mini", help="LLM deployment name")
    parser.add_argument("--iterations", type=int, default=20, help="Max iterations per query")
    parser.add_argument("--queries", type=str, default=None, help="Comma-separated query IDs (e.g., '1,2,3'). Default: all")
    args = parser.parse_args()

    task_dir = Path(f"query_{args.task}")
    if not task_dir.exists():
        print(f"Error: Task directory {task_dir} does not exist")
        return

    # Find all query directories
    if args.queries:
        query_ids = [int(q) for q in args.queries.split(",")]
    else:
        query_dirs = sorted(task_dir.glob("query[0-9]*"))
        query_ids = [int(d.name.replace("query", "")) for d in query_dirs]

    print(f"Task: {args.task}")
    print(f"LLM: {args.llm}")
    print(f"Queries to run: {query_ids}")

    results = []

    for query_id in query_ids:
        query_dir = task_dir / f"query{query_id}"
        if not query_dir.exists():
            print(f"Warning: {query_dir} does not exist, skipping")
            continue

        # Run the agent
        final_answer = run_query(args.task, query_id, args.llm, args.iterations)

        # Validate the result
        validate_func = load_validate_func(query_dir)
        if validate_func:
            is_valid, reason = validate_func(final_answer)
        else:
            is_valid, reason = False, "No validate.py found"

        results.append({
            "query_id": query_id,
            "final_answer": final_answer,
            "is_valid": is_valid,
            "reason": reason,
        })

        status = "✅" if is_valid else "❌"
        print(f"\nQuery {query_id}: {status}")
        print(f"  Answer: {final_answer}")
        print(f"  Validation: {reason}")

    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")

    total = len(results)
    correct = sum(1 for r in results if r["is_valid"])

    print(f"\nResults by query:")
    for r in results:
        status = "✅" if r["is_valid"] else "❌"
        print(f"  Query {r['query_id']}: {status} - {r['reason']}")

    print(f"\nAccuracy: {correct}/{total} ({100*correct/total:.1f}%)")

if __name__ == "__main__":
    main()
