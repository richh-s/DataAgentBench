import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pathlib import Path
import json
import numpy as np
ROOT = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def model_api_calls(model, dataset_list):
    tot_calls = 0
    num_tool_call_per_call = []
    for dataset in dataset_list:  
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
            
                for query_id in query_ids:
                    result_dir = ROOT / f"results-{model}" / f"query_{dataset}" / f"query{query_id}" / "data_agent"
                    runs = list(range(50))
                    for rid in runs:
                        run_dir = result_dir / f"run_{rid}"
                        result_path = run_dir / f"llm_calls.jsonl"
                        if not result_path.exists():
                            continue
                        with open(result_path, encoding="utf-8") as f:
                            messages = []
                            for l in f:
                                llm_call = json.loads(l)
                                try:
                                    messages.append(llm_call['response']['choices'][0]['message'])
                                except Exception as e:
                                    continue
                        for msg in messages:
                            if msg['role'] != 'assistant':
                                continue
                            tot_calls += 1
                            try:
                                num_tool_calls = len(msg['tool_calls'])
                                num_tool_call_per_call.append(num_tool_calls)
                            except Exception as e:
                                num_tool_call_per_call.append(0)
                                continue
    assert len(num_tool_call_per_call) == tot_calls, f"{model}: total calls {tot_calls} does not match length of tool call list {len(num_tool_call_per_call)}"

    avg_calls_per_api_call = np.mean(num_tool_call_per_call)
    std_calls_per_api_call = np.std(num_tool_call_per_call)
    max_calls_per_api_call = max(num_tool_call_per_call)
    num_calls_with_more_than_one_tool_call = sum(1 for c in num_tool_call_per_call if c > 1)
    ratio_more_than_one = num_calls_with_more_than_one_tool_call / tot_calls
    num_calls_with_more_than_two_tool_call = sum(1 for c in num_tool_call_per_call if c > 2)
    ratio_more_than_two = num_calls_with_more_than_two_tool_call / tot_calls

    print(f"{model},{tot_calls},{avg_calls_per_api_call:.2f} ({std_calls_per_api_call:.2f}),{max_calls_per_api_call},{ratio_more_than_one:.3f},{ratio_more_than_two:.3f}")

for model in ['gpt-5.2', 'gpt-5-mini', 'gemini-3-pro', 'gemini-2.5-flash', 'kimi-k2-thinking']:
    model_api_calls(model, [
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
        "music_brainz_20k"
    ])