import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
import json


def count_no_tool_calls(result_dir: Path, runs: list):
    no_tool_calls = 0
    for rid in runs:
        run_dir = result_dir / f"run_{rid}"
        llm_json_path = run_dir / "final_agent.json"
        if not llm_json_path.exists():
            continue
        else:

            with open(llm_json_path, encoding="utf-8") as f:
                llm_json = json.load(f)

            term_reason = llm_json['terminate_reason']
            if term_reason == "no_tool_call":
                no_tool_calls += 1
    
    return no_tool_calls



if __name__ == "__main__":
    model_list = [
        "gemini-2.5-flash",
        "gemini-3-pro",
        "gpt-5-mini",
        "gpt-5.2",
        "gpt5.1",
        "kimi-k2-thinking",
    ]

    task_list = [
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
    ]

    for model in model_list:
        no_tool_calls_cnt = 0
        for task in task_list:
            query_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), f"query_{task}")
            assert os.path.exists(query_dir), f"⚠️ {query_dir} not found"
            query_id_list = []
            for d in Path(query_dir).iterdir():
                try:
                    query_id = int(d.name.replace("query", ""))
                    query_id_list.append(query_id)
                except:
                    continue
            for query_id in sorted(query_id_list):
                result_dir = f"/home/ruiying/DataAgentBench-local/results-{model}/query_{task}/query{query_id}"
                if model != "gpt5.1":
                    result_dir = os.path.join(result_dir, "data_agent")
                
                no_tool_calls_cnt += count_no_tool_calls(Path(result_dir), list(range(50)))
            
        print(f"{model}: {no_tool_calls_cnt}")
                
