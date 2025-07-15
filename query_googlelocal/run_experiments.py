import re
import sys
import numpy as np
import pandas as pd
import os
from pathlib import Path
import yaml
from dotenv import load_dotenv
from openai import AzureOpenAI

# Add parent directory to sys.path so that common_scaffold can be imported
sys.path.append(str(Path(__file__).resolve().parents[1]))
from common_scaffold.agent_tools import run_baseline_agent


def find_query_dirs(project_dir: Path):
    """
    Find all subdirectories in project_dir named queryN (N is a number).
    These are treated as individual queries/tasks.
    """
    return sorted(
        [p for p in project_dir.iterdir() if p.is_dir() and re.fullmatch(r"query\d+", p.name)],
        key=lambda p: int(re.search(r"\d+", p.name).group())
    )


def pass_at_k(n, c, k):
    """
    Compute the unbiased estimate of pass@k as defined in the Codex paper:
    n: total number of samples
    c: number of correct samples
    k: number of samples to select
    """
    if n - c < k:
        return 1.0
    return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))


def main():
    # Configurable parameters
    n = 20  # number of runs per query
    k_list = [1, 5, 10, 20]  # k values to evaluate pass@k

    project_dir = Path(__file__).parent
    load_dotenv()

    # Load database description text
    with open(project_dir / "db_description.txt") as f:
        db_description = f.read()

    # Load database connection configuration
    with open(project_dir / "db_config.yaml") as f:
        db_config = yaml.safe_load(f)

    # Initialize Azure OpenAI client
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_API_KEY_o3"),
        api_version=os.getenv("AZURE_API_VERSION_o3", "2023-05-15"),
        azure_endpoint=os.getenv("AZURE_API_BASE_o3")
    )
    deployment_name = "o3"

    # Discover all query directories
    queries = find_query_dirs(project_dir)
    print(f"📝 Found {len(queries)} queries: {[q.name for q in queries]}")

    query_results = []  # list to store results for each query

    # Run each query n times
    for i, query_dir in enumerate(queries, 1):
        print(f"\n🚀 Query {i}/{len(queries)}: {query_dir.name}")
        c = 0  # counter for correct runs

        for run_id in range(1, n+1):
            print(f"   ▶ Run {run_id}/{n}")
            success = run_baseline_agent(
                query_dir=query_dir,
                project_dir=project_dir,
                db_description=db_description,
                db_config=db_config,
                client=client,
                deployment_name=deployment_name
            )
            if success:
                c += 1

        print(f"✅ Query {query_dir.name}: {c}/{n} correct")
        query_results.append({"query_id": query_dir.name, "n": n, "c": c})

    # 🎯 Compute pass@k for each query and save to DataFrame
    rows = []
    for q in query_results:
        row = {
            "query_id": q["query_id"],
            "n": q["n"],
            "c": q["c"]
        }
        for k in k_list:
            passk = pass_at_k(q["n"], q["c"], k)
            row[f"pass@{k}"] = passk
            print(f"🎯 {q['query_id']} pass@{k}: {passk:.4f}")
        rows.append(row)

    df = pd.DataFrame(rows)

    # Compute overall average pass@k across all queries
    overall_row = {"query_id": "Overall"}
    for k in k_list:
        overall_row[f"pass@{k}"] = df[f"pass@{k}"].mean()
    df = pd.concat([df, pd.DataFrame([overall_row])], ignore_index=True)

    # Save results to Excel file
    out_path = project_dir / "pass_at_k_results.xlsx"
    df.to_excel(out_path, index=False)
    print(f"\n📄 Results saved to: {out_path}")

    # Optionally save as CSV too
    df.to_csv(project_dir / "pass_at_k_results.csv", index=False)

if __name__ == "__main__":
    main()
