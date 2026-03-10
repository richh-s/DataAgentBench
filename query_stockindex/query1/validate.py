import re

def validate(llm_output: str):
    """
    Validate that:
    - '399001.SZ' is present in LLM output
    - None of the other candidates are the primary/first answer

    Returns:
        (True, "OK") if all good
        (False, reason) if failed
    """
    gt = "399001.SZ"
    forbidden = [
        "J203.JO", "N225", "GSPTSE", "NSEI", "GDAXI", "NYA",
        "000001.SS", "SSMI", "TWII", "N100", "IXIC", "HSI"
    ]

    llm_lower = llm_output.lower()
    gt_lower = gt.lower()

    # check gt
    if gt_lower not in llm_lower:
        reason = f"Missing target: {gt}"

        return False, reason

    # check forbidden — only fail if a forbidden value appears before the correct answer
    gt_idx = llm_lower.find(gt_lower)
    for f_orig, f in zip(forbidden, [f.lower() for f in forbidden]):
        idx = llm_lower.find(f)
        if idx != -1 and idx < gt_idx:
            reason = f"Found forbidden value '{f_orig}' before target '{gt}'"

            return False, reason

    return True, f"Target '{gt}' present as primary answer."
