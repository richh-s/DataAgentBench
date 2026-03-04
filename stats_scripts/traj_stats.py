import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pathlib import Path
import json
import numpy as np
from stats_scripts.llm_calls import llm_calls_analysis_per_query
from stats_scripts.tool_calls import tool_calls_analysis_per_query

ROOT = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def latency_per_query(result_dir: Path, runs: list):
    latency_list = []
    for rid in runs:
        run_dir = result_dir / f"run_{rid}"
        latency_json_path = run_dir / "final_agent.json"
        if not latency_json_path.exists():
            continue
        with open(latency_json_path, 'r') as f:
            latency_data = json.load(f)
        latency_list.append(latency_data['duration'])

    return {
        'latency': [np.mean(latency_list), np.std(latency_list)],
    }
def tool_calls_per_query(result_dir: Path, runs: list):
    tool_calls_list = []
    python_list = []
    db_list = []
    for rid in runs:
        run_dir = result_dir / f"run_{rid}"
        tool_json_path = run_dir / f"tool_calls.jsonl"
        if not tool_json_path.exists():
            continue
        with open(tool_json_path, encoding="utf-8") as f:
            tool_calls = [json.loads(line) for line in f if line.strip()]
        tool_calls_list.append(len(tool_calls))
        python_calls = [call for call in tool_calls if call['tool_name'] == 'execute_python']
        db_calls = [call for call in tool_calls if call['tool_name'] in ['list_db', 'query_db']]
        python_list.append(len(python_calls))
        db_list.append(len(db_calls))

    

    return {
        'tool_calls': [np.mean(tool_calls_list), np.std(tool_calls_list)],
        'python_calls': [np.mean(python_list), np.std(python_list)],
        'db_calls': [np.mean(db_list), np.std(db_list)],
    }

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
            avg_latency_per_query = []
            avg_llm_calls_per_query = []
            avg_listdb_calls_per_query = []
            avg_querydb_calls_per_query = []
            avg_executepython_calls_per_query = []
            avg_returnanswer_calls_per_query = []
            avg_tool_calls_per_query = []
            for query_id in query_ids:
                result_dir = ROOT / f"results-{model}" / f"query_{dataset}" / f"query{query_id}" / "data_agent"
                runs = list(range(50))
                latency_result = latency_per_query(result_dir, runs)
                llm_calls_result = llm_calls_analysis_per_query(result_dir, runs)
                for tool_name in ['list_db', 'query_db', 'execute_python', 'return_answer']:
                    tool_calls_result = tool_calls_analysis_per_query(result_dir, tool_name, runs)
                    if tool_name == 'list_db':
                        avg_listdb_calls_per_query.append(tool_calls_result['tool_calls'][0])
                    elif tool_name == 'query_db':
                        avg_querydb_calls_per_query.append(tool_calls_result['tool_calls'][0])
                    elif tool_name == 'execute_python':
                        avg_executepython_calls_per_query.append(tool_calls_result['tool_calls'][0])
                    elif tool_name == 'return_answer':
                        avg_returnanswer_calls_per_query.append(tool_calls_result['tool_calls'][0])
                avg_latency_per_query.append(latency_result['latency'][0])
                avg_llm_calls_per_query.append(llm_calls_result['llm_calls'][0])
                avg_tool_calls_per_query.append(tool_calls_per_query(result_dir, runs)['tool_calls'][0])
            avg_latency = np.mean(avg_latency_per_query)
            avg_llm_calls = np.mean(avg_llm_calls_per_query)
            avg_listdb_calls = np.mean(avg_listdb_calls_per_query)
            avg_querydb_calls = np.mean(avg_querydb_calls_per_query)
            avg_executepython_calls = np.mean(avg_executepython_calls_per_query)
            avg_returnanswer_calls = np.mean(avg_returnanswer_calls_per_query)
            avg_tool_calls = np.mean(avg_tool_calls_per_query)
            result_str += f"{avg_latency:.2f},{avg_llm_calls:.2f},{avg_tool_calls:.2f},{avg_listdb_calls:.2f},{avg_querydb_calls:.2f},{avg_executepython_calls:.2f},{avg_returnanswer_calls:.2f},"
        print(result_str)

    

