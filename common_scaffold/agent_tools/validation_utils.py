from pathlib import Path
from datetime import datetime
import importlib.util
import os
import json

def validate_and_log(query_dir: Path, llm_answer: str, root_log_dir: str) -> tuple[bool, str]:
    """
    Run query_dir/validate.py to check the LLM answer, and log the result.

    Args:
        query_dir (Path)
        llm_answer (str)

    Returns:
        (is_valid, reason)
    """
    validate_py = query_dir / "validate.py"
    if not validate_py.exists():
        raise FileNotFoundError(f"validate.py not found at: {validate_py}")

    spec = importlib.util.spec_from_file_location("validate", str(validate_py))
    validate_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(validate_mod)

    is_valid, reason = validate_mod.validate(llm_answer)

    write_validation_log(
        query_dir=query_dir,
        llm_answer=llm_answer,
        match_result=is_valid,
        reason=reason,
        root_log_dir=root_log_dir,
    )

    return is_valid, reason


def write_validation_log(query_dir: Path, llm_answer: str, match_result: bool, reason: str, root_log_dir: str = None):
    log_path = os.path.join(root_log_dir, "validation.jsonl")
    gt_path = query_dir / "ground_truth.csv"

    if not gt_path.exists():
        print(f"⚠️ ground_truth.csv not found: {gt_path}")
        gt_lines = ["<ground truth file missing>"]
    else:
        with open(gt_path, encoding="utf-8") as f:
            gt_lines = [line.strip() for line in f if line.strip()]

    gt_str = "\n".join(gt_lines)

    log_dict = {
        "timestamp": datetime.now().strftime("%Y%m%d_%H%M%S"),
        "query_name": query_dir.name,
        "is_match": match_result,
        "reason": reason,
        "ground_truth": gt_str,
        "llm_answer": llm_answer.strip(),
    }

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_dict, ensure_ascii=False) + "\n")

    print(f"\nValidation log updated at: {log_path}")

def log_failed(query_dir: Path, reason: str, root_log_dir: str):
    """
    when agent break down due to code issue
    """
    write_validation_log(
        query_dir=query_dir,
        llm_answer="FAILED due to agent crash",
        match_result=False,
        reason=reason,
        root_log_dir=root_log_dir,
    )
