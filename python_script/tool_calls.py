import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
import json
import numpy as np


def tool_calls_analysis_per_query(result_dir: Path, tool_name, runs: list):
    call_num_list = []
    time_list = []
    success_rate_list = []

    for rid in runs:
        run_dir = result_dir / f"run_{rid}"
        tool_json_path = run_dir / f"tool_calls.jsonl"
        if not tool_json_path.exists():
            continue
        call_num = 0
        tot_time = 0.0
        success_count = 0
        with open(tool_json_path, encoding="utf-8") as f:
            tool_calls = [json.loads(line) for line in f if line.strip()]
        for call in tool_calls:
            if call['tool_name'] == tool_name:
                call_num += 1
                tot_time += call['time']
                if call['result']['success'] == True:
                    success_count += 1
        call_num_list.append(call_num)
        time_list.append(tot_time)
        if call_num > 0:
            success_rate_list.append(success_count / call_num)

    return {
        'tool_calls': [np.mean(call_num_list), np.std(call_num_list)],
        'time': [np.mean(time_list), np.std(time_list)],
        'success_rate': [np.mean(success_rate_list), np.std(success_rate_list)],
    }