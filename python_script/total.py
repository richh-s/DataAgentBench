import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
import logging_config
import json

from python_script.accuracy import pass_k_per_query
from python_script.llm_calls import llm_calls_analysis_per_query
from python_script.tool_calls import tool_calls_analysis_per_query

K_LIST = [1, 5, 10, 15, 20, 30, 40, 50]
QUERY_ROOT = Path("/home/ruiying/DataAgentBench")
RESULT_ROOT = Path("/home/ruiying/DataAgentBench/results-gpt5.1")
# RESULT_ROOT = Path("/home/ruiying/DataAgentBench/results-gemini-3-pro")
# RESULT_ROOT = Path("/home/ruiying/DataAgentBench/results-gemini-2.5-flash")
# RESULT_ROOT = Path("/home/ruiying/DataAgentBench")
TOOL_LIST = ["query_db", "list_db", "execute_python", "return_answer"]

def analysis_per_query(task, query_id, result_root: Path, runs: list):
    query_dir = QUERY_ROOT / f"query_{task}" / f"query{query_id}"
    result_dir = result_root / f"query_{task}" / f"query{query_id}" # results-gpt5.1
    # result_dir = result_root / f"query_{task}" / f"query{query_id}" / "data_agent" # gemini
    # result_dir = result_root / f"query_{task}" / f"query{query_id}" / "logs" / "data_agent"
    assert result_dir.exists(), f"Result dir {result_dir} does not exist."

    accuracy, pass_k_results, reasons = pass_k_per_query(query_dir, result_dir, runs)
    # accuracy = 0
    # pass_k_results = {f"pass@{k}": 0.0 for k in K_LIST}
    # reasons = dict()


    llm_calls_results = llm_calls_analysis_per_query(result_dir, runs)

    tool_calls_results = dict()
    for tool_name in TOOL_LIST:
        tool_calls_results[tool_name] = tool_calls_analysis_per_query(result_dir, tool_name, runs)

    # PRINT
    result = f"{query_id},{accuracy}/{len(runs)},,"
    result += ",".join([f"{pass_k_results[f'pass@{k}']:.4f}" for k in K_LIST]) + ",,"

    LLM_CALL_KEYS = ['llm_calls', 'time', 'input', 'output']
    for key in LLM_CALL_KEYS:
        mean, std = llm_calls_results[key]
        result += f"{mean:.2f}±{std:.2f},"
    result += ","
    for tool_name in TOOL_LIST:
        TOOL_CALL_KEYS = ['tool_calls', 'time', 'success_rate']
        for key in TOOL_CALL_KEYS:
            mean, std = tool_calls_results[tool_name][key]
            result += f"{mean:.4f} ± {std:.4f},"
        result += ","
    
    result += ",".join([f"{reason}:{count}/{len(runs)}" for reason, count in reasons.items()])

    return result




if __name__ == "__main__":
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
        "music_brainz_20k",
    ]:
        print(task)
        query_dir = QUERY_ROOT / f"query_{task}"
        for folder_name in sorted(os.listdir(query_dir)):
            if folder_name.startswith("query"):
                try:
                    query_id = int(folder_name.replace("query", ""))
                    # print(query_id)
                except Exception as e:
                    continue
                runs = list(range(50))
                result = analysis_per_query(task, query_id, RESULT_ROOT, runs)
                print(result)
        print("\n\n")