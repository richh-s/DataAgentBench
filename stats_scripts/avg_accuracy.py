import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path

from stats_scripts.accuracy import pass_k_per_query

ROOT = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def avg_acc(dataset, model):
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

    accuracies = []
    for query_id in query_ids:
        q_dir = query_dir / f"query{query_id}"
        r_dir = result_dir / f"query{query_id}"
        if "gemini" in model or "gpt-5-mini" in model or "gpt-5.2" in model or "kimi" in model:
            r_dir = r_dir / "data_agent" 
        runs = list(range(50))
        accuracy, pass_k_results, reasons = pass_k_per_query(q_dir, r_dir, runs)
        accuracies.append(accuracy / len(runs))
    
    avg_accuracy = sum(accuracies) / len(accuracies)
    return avg_accuracy


if __name__ == "__main__":
    model_list = [
        "gpt-5.2",
        "gpt-5-mini",
        "gemini-3-pro",
        "gemini-2.5-flash",
        "kimi-k2-thinking"
    ]
    print("dataset," + ",".join(model_list))
    for dataset in [
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
    ]:
        output_str = f"{dataset},"
        for model in model_list:
            avg_accuracy = avg_acc(dataset, model)
            output_str += f"{avg_accuracy:.4f},"
        print(output_str)
    
