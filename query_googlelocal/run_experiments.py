import re
import sys
import os
import numpy as np
from pathlib import Path
import yaml
from dotenv import load_dotenv
from openai import AzureOpenAI

sys.path.append(str(Path(__file__).resolve().parents[1]))
from common_scaffold.agent_tools import run_baseline_agent


def find_query_dirs(project_dir: Path):
    return sorted(
        [p for p in project_dir.iterdir() if p.is_dir() and re.fullmatch(r"query\d+", p.name)],
        key=lambda p: int(re.search(r"\d+", p.name).group())
    )


def pass_at_k(n, c, k):
    if n - c < k:
        return 1.0
    return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))


def main():
    # 🎯 这里定义
    n = 20
    k_list = [1, 5, 10, 20]

    project_dir = Path(__file__).parent
    load_dotenv()

    with open(project_dir / "db_description.txt") as f:
        db_description = f.read()

    with open(project_dir / "db_config.yaml") as f:
        db_config = yaml.safe_load(f)

    client = AzureOpenAI(
        api_key=os.getenv("AZURE_API_KEY_o3"),
        api_version=os.getenv("AZURE_API_VERSION_o3", "2023-05-15"),
        azure_endpoint=os.getenv("AZURE_API_BASE_o3")
    )
    deployment_name = "o3"

    queries = find_query_dirs(project_dir)
    print(f"📝 Found {len(queries)} queries: {[q.name for q in queries]}")

    query_results = []  # 保存每个 query 的 c

    for i, query_dir in enumerate(queries, 1):
        print(f"\n🚀 Query {i}/{len(queries)}: {query_dir.name}")
        c = 0
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
        query_results.append((query_dir.name, n, c))

    # 🎯 汇总 pass@k
    for k in k_list:
        all_passk = []
        for name, n, c in query_results:
            passk = pass_at_k(n, c, k)
            all_passk.append(passk)
            print(f"🎯 {name} pass@{k}: {passk:.4f}")

        overall_passk = np.mean(all_passk)
        print(f"\n🌟 Overall pass@{k}: {overall_passk:.4f}")

if __name__ == "__main__":
    main()
