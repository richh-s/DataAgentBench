import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
import logging_config

from stats_scripts.accuracy import pass_k_per_query
from common_scaffold.validate.pass_k import K_LIST

ROOT = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def avg_pass_k(dataset, model):
    query_dir = ROOT / f"query_{dataset}"
    result_dir = ROOT / f"results-{model}" / f"query_{dataset}"

    query_ids = []
    for query_path in query_dir.iterdir():
        if query_path.is_dir() and query_path.name.startswith("query"):
            try:
                query_id = int(query_path.name.replace("query", ""))
                query_ids.append(query_id)
            except ValueError:
                continue

    query_ids = sorted(query_ids)

    pass_k_sums = {k: 0.0 for k in K_LIST}
    for query_id in query_ids:
        q_dir = query_dir / f"query{query_id}"
        r_dir = result_dir / f"query{query_id}"
        if "gemini" in model or "gpt-5-mini" in model or "gpt-5.2" in model or "kimi" in model:
            r_dir = r_dir / "data_agent" 
        runs = list(range(50))
        accuracy, pass_k_results, reasons = pass_k_per_query(q_dir, r_dir, runs)
        for k in K_LIST:
            pass_k_sums[k] += pass_k_results[f"pass@{k}"]
    
    avg_pass_k = {k: v / len(query_ids) for k, v in pass_k_sums.items()}
    return avg_pass_k




if __name__ == "__main__":
    model_list = [
        "gpt-5.2",
        "gpt-5-mini",
        "gemini-3-pro",
        "gemini-2.5-flash",
        "kimi-k2-thinking"
    ]
    dataset_list = [
        "bookreview",
        "crmarenapro",
        "DEPS_DEV_V1",
        "GITHUB_REPOS",
        "googlelocal",
        "PANCANCER_ATLAS",
        "PATENTS",
        "stockindex",
        "stockmarket",
        "yelp",
        "agnews",
        "music_brainz_20k",
    ]
    # for each dataset, plot pass@k for each model on one subplot
    for i, dataset in enumerate(dataset_list):
        result_str = f"{dataset},"
        for model in model_list:
            avg_pass_k_results = avg_pass_k(dataset, model)
            assert sorted(avg_pass_k_results.keys()) == K_LIST
            pass_k_values = [avg_pass_k_results[k] for k in K_LIST]
            for v in pass_k_values:
                result_str += f"{v:.4f},"

        print(result_str)
        
    
