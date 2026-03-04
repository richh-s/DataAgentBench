import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pathlib import Path
import json
import numpy as np

ROOT = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def _get_cost_k(input_token, output_token, model):
    """
    Cost: 0.001 USD
    """
    if model == "gpt-5-mini":
        input_cost_per_1m = 0.25
        output_cost_per_1m = 2
    elif model == "gpt-5.2":
        input_cost_per_1m = 1.75
        output_cost_per_1m = 14
    elif model == "gemini-3-pro":
        if input_token <= 200000:
            input_cost_per_1m = 2
        else:
            input_cost_per_1m = 4
        if output_token <= 200000:
            output_cost_per_1m = 12
        else:
            output_cost_per_1m = 18
    elif model == "gemini-2.5-flash":
        input_cost_per_1m = 0.3
        output_cost_per_1m = 2.5
    else:
        raise ValueError(f"Unsupported model: {model}")
    
    return (input_token / 1e3) * input_cost_per_1m + (output_token / 1e3) * output_cost_per_1m

def cost_analysis_per_query(result_dir: Path, runs: list, model: str):
    """
    cost: 0.001 USD
    """
    tot_cost = []
    for rid in runs:
        run_dir = result_dir / f"run_{rid}"
        assert run_dir.exists(), f"Run dir {run_dir} does not exist."
        llm_json_path = run_dir / "llm_calls.jsonl"
        run_cost = 0.0
        if not llm_json_path.exists():
            continue
        with open(llm_json_path, 'r') as f:
            llm_calls = [json.loads(line) for line in f if line.strip()]
        for call in llm_calls:
            if call['response'] == None:
                continue
            input_token = call['response']['usage']['prompt_tokens']
            output_token = call['response']['usage']['completion_tokens']
            run_cost += _get_cost_k(input_token, output_token, model)
        tot_cost.append(run_cost)

    assert tot_cost, f"No valid runs found in {result_dir} for model {model}."
    assert len(tot_cost) <= len(runs), f"More costs calculated than runs in {result_dir} for model {model}."

    return np.mean(tot_cost) if tot_cost else 0.0


if __name__ == "__main__":
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
        # get queries
        query_ids = []        
        query_dir = ROOT / f"query_{dataset}"
        for folder_name in sorted(os.listdir(query_dir)):
            if folder_name.startswith("query"):
                try:
                    query_id = int(folder_name.replace("query", ""))
                    query_ids.append(query_id)
                except Exception as e:
                    continue
        # get per-dataset result for each model
        result_str = f"{dataset},"
        for model in ['gpt-5.2', 'gpt-5-mini', 'gemini-3-pro', 'gemini-2.5-flash']:
            avg_cost_per_query = []
            for query_id in query_ids:
                result_dir = ROOT / f"results-{model}" / f"query_{dataset}" / f"query{query_id}"
                runs = list(range(50))
                avg_cost_per_query.append(cost_analysis_per_query(result_dir, runs, model))
            cost_result = np.mean(avg_cost_per_query)
            result_str += f"{cost_result:.4f},"
        print(result_str)

    

