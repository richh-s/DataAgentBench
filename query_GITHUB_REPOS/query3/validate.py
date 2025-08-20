import re

def validate(llm_output: str) -> (bool, str):
    """
    Check if the number 1077 appears in the LLM output.

    The match should be exact (as a complete number, not part of another number),
    and can be anywhere in the text.

    Returns:
        (True, "OK") if 1077 is found
        (False, reason) otherwise
    """
    matches = re.findall(r"\b1077\b", llm_output)
    if matches:
        print("✅ Found 1077 in LLM output.")
        return True, "OK"
    else:
        reason = "❌ Number 1077 not found in LLM output."
        print(reason)
        return False, reason

