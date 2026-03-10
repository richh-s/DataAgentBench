import re

def validate(llm_output: str):
    gt = "Amazon Music"
    # Case-insensitive check preserving word boundaries
    if re.search(r'\b' + re.escape(gt) + r'\b', llm_output, re.IGNORECASE):
        return True, "Ground truth found in LLM output."
    else:
        reason = f"Ground truth '{gt}' not found in LLM output: {llm_output}"
        return False, reason
