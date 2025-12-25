import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common_scaffold.validate.pass_k import pass_at_k_list
from common_scaffold.validate.validate  import validate
from pathlib import Path
import logging
import json

def pass_k_per_query(query_dir: Path, result_dir: Path, runs: list):
    results = []
    term_reasons = dict()
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
            llm_answer = llm_json['final_result']
            term_reason = llm_json['terminate_reason']

        validation_result = validate(query_dir, llm_answer, term_reason)
        if validation_result["is_valid"]:
            results.append(1)
        else:
            results.append(0)

        if term_reason not in term_reasons:
            term_reasons[term_reason] = 0
        term_reasons[term_reason] += 1
    
    n = len(results)
    c = sum(results)
    passk_results = pass_at_k_list(n, c)
    return c, passk_results, term_reasons