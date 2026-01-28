import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
import logging_config
import json

from python_script.accuracy import pass_k_per_query

ROOT = Path("/home/ruiying/DataAgentBench-local")
def avg_acc(task, model):
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

    accuracies = []
    for query_id in query_ids:
        q_dir = query_dir / f"query{query_id}"
        r_dir = result_dir / f"query{query_id}"
        if "gemini" in model:
            r_dir = r_dir / "data_agent" 
        runs = list(range(50))
        accuracy, pass_k_results, reasons = pass_k_per_query(q_dir, r_dir, runs)
        accuracies.append(accuracy / len(runs))
    
    avg_accuracy = sum(accuracies) / len(accuracies)
    return avg_accuracy


if __name__ == "__main__":
    model_list = [
        "gpt5.1",
        "gemini-3-pro",
        "gemini-2.5-flash"
    ]
    print("task," + ",".join(model_list))
    for task in [
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
    ]:
        output_str = f"{task},"
        for model in model_list:
            avg_accuracy = avg_acc(task, model)
            output_str += f"{avg_accuracy:.4f},"
        print(output_str)
    
