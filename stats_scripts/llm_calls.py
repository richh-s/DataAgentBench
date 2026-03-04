import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
import json
import numpy as np


def llm_calls_analysis_per_query(result_dir: Path, runs: list):
    llm_call_counts_list = []
    time_list = []
    input_list = []
    output_list = []
    for rid in runs:
        run_dir = result_dir / f"run_{rid}"
        llm_json_path = run_dir / "llm_calls.jsonl"
        llm_call_counts = 0
        tot_time = 0.0
        tot_input = 0
        tot_output = 0
        if not llm_json_path.exists():
            continue
        with open(llm_json_path, 'r') as f:
            llm_calls = [json.loads(line) for line in f if line.strip()]
        for call in llm_calls:
            llm_call_counts += 1
            tot_time += call['duration']
            if call['response'] == None:
                continue
            tot_input += call['response']['usage']['prompt_tokens']
            tot_output += call['response']['usage']['completion_tokens']
        llm_call_counts_list.append(llm_call_counts)
        time_list.append(tot_time)
        input_list.append(tot_input)
        output_list.append(tot_output)


    
    return {
        'llm_calls': [np.mean(llm_call_counts_list), np.std(llm_call_counts_list)],
        'time': [np.mean(time_list), np.std(time_list)],
        'input': [np.mean(input_list), np.std(input_list)],
        'output': [np.mean(output_list), np.std(output_list)],
    }

