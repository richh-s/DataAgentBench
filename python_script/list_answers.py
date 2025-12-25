import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common_scaffold.validate.pass_k import pass_at_k_list
from common_scaffold.validate.validate  import validate
from pathlib import Path
import logging
import json


def list_answers(result_dir: Path, runs: list):
    for rid in runs:
        run_dir = result_dir / f"run_{rid}"
        llm_json_path = run_dir / "final_agent.json"
        if not llm_json_path.exists():
            logging.getLogger(__name__).warning(f"⚠️ {llm_json_path} not found")
            llm_answer = ""
            term_reason = "final_agent.json not found"
        else:

            with open(llm_json_path, encoding="utf-8") as f:
                llm_json = json.load(f)
            llm_answer = llm_json['final_result'].strip()
            print(llm_answer)



if __name__ == "__main__":
    TASK = "music_brainz_20k"
    QUERY_ID = 3
    for MODEL in ["gpt5.1", "gemini-3-pro", "gemini-2.5-flash"]:
        ROOT_DIR = Path(f"/home/ruiying/DataAgentBench/results-{MODEL}/query_{TASK}/query{QUERY_ID}")
        if MODEL != "gpt5.1":
            ROOT_DIR = ROOT_DIR / "data_agent"
        print(f"=== MODEL: {MODEL} ===")
        list_answers(ROOT_DIR, runs=list(range(50)))
        print("")

