import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
import logging_config
import json

from python_script.accuracy import pass_k_per_query
from common_scaffold.validate.pass_k import K_LIST
import matplotlib.pyplot as plt

ROOT = Path("/home/ruiying/DataAgentBench-local")
def avg_pass_k(task, model):
    query_dir = ROOT / f"query_{task}"
    result_dir = ROOT / f"results-{model}" / f"query_{task}"

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
        if "gemini" in model:
            r_dir = r_dir / "data_agent" 
        runs = list(range(50))
        accuracy, pass_k_results, reasons = pass_k_per_query(q_dir, r_dir, runs)
        for k in K_LIST:
            pass_k_sums[k] += pass_k_results[f"pass@{k}"]
    
    avg_pass_k = {k: v / len(query_ids) for k, v in pass_k_sums.items()}
    return avg_pass_k




if __name__ == "__main__":
    model_list = [
        "gpt5.1",
        "gemini-3-pro",
        "gemini-2.5-flash"
    ]
    task_list = [
        # "bookreview",
        # "crmarenapro",
        # "DEPS_DEV_V1",
        # "GITHUB_REPOS",
        # "googlelocal",
        # "PANCANCER_ATLAS",
        # "PATENTS",
        # "stockindex",
        # "stockmarket",
        # "yelp",
        # "agnews",
        # "music_brainz_20k",
        "civic_unstructured",
        "paper_unstructured"
    ]
    # create a #task x 1 subplot, each subplot has pass@k curves for all models
    fig, axs = plt.subplots(len(task_list), 1, figsize=(8, 4 * len(task_list)))
    # for each task, plot pass@k for each model on one subplot
    for i, task in enumerate(task_list):
        ax = axs[i]
        for model in model_list:
            avg_pass_k_results = avg_pass_k(task, model)
            assert sorted(avg_pass_k_results.keys()) == K_LIST
            pass_k_values = [avg_pass_k_results[k] for k in K_LIST]
            ax.plot(K_LIST, pass_k_values, label=model)
        
        ax.set_title(f"Average Pass@K for Task: {task}")
        ax.set_xlabel("K")
        ax.set_ylabel("Average Pass@K")
        ax.set_ylim(0, 1)
        ax.legend()
        ax.grid(True)
    
    plt.savefig("figures/avg_pass_k_per_task_unstructured.png", bbox_inches='tight')
    
