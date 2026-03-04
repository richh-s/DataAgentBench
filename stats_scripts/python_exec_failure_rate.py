import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pathlib import Path
import json
import numpy as np

ROOT = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def python_fr_per_query(result_dir: Path, runs: list):
    fr_list = []
    for rid in runs:
        run_dir = result_dir / f"run_{rid}"
        tool_json_path = run_dir / f"tool_calls.jsonl"
        if not tool_json_path.exists():
            continue
        with open(tool_json_path, encoding="utf-8") as f:
            tool_calls = [json.loads(line) for line in f if line.strip()]
        python_calls = [call for call in tool_calls if call['tool_name'] == 'execute_python']
        if len(python_calls) == 0:
            continue
        else:
            fail_count = sum(1 for call in python_calls if call['result']['success'] == False)
            fr_list.append(fail_count / len(python_calls))

    if len(fr_list) == 0:
        return None # no python call is made across all runs in the query
    return np.mean(fr_list)


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
        for model in ['gpt-5.2', 'gpt-5-mini', 'gemini-3-pro', 'gemini-2.5-flash', 'kimi-k2-thinking']:
            qvg_python_fr_list = []
            for query_id in query_ids:
                result_dir = ROOT / f"results-{model}" / f"query_{dataset}" / f"query{query_id}" / "data_agent"
                runs = list(range(50))
                python_fr = python_fr_per_query(result_dir, runs)
                if python_fr == None:
                    continue
                qvg_python_fr_list.append(python_fr)
            avg_python_fr = np.mean(qvg_python_fr_list)
            result_str += f"{avg_python_fr:.2f},"
        print(result_str)

    

