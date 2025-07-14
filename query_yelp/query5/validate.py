import re

def validate(llm_output: str) -> (bool, str):
    """
    Validate if ground truth 'PA' and its number (rounded to 2 decimals) are present in LLM output.
    Returns:
        (True, "OK") if found
        (False, reason) if not
    """
    ground_truth_name = "PA"
    ground_truth_value = 3.48
    gt_rounded = round(ground_truth_value, 2)

    llm_lower = llm_output.lower()
    name_lower = ground_truth_name.lower()

    # check if name is present
    idx = llm_lower.find(name_lower)
    if idx == -1:
        reason = f"Missing name: {ground_truth_name}"
        print(f"❌ {reason}")
        return False, reason

    # take a window of text after the name
    window = llm_output[idx:idx+50]
    matches = re.findall(r"(\d+\.\d+)", window)

    if not matches:
        reason = f"No number found near name: {ground_truth_name}"
        print(f"❌ {reason}")
        return False, reason

    for m in matches:
        try:
            val = float(m)
            if round(val, 2) == gt_rounded:
                print(f"✅ Found: name='{ground_truth_name}', value≈{gt_rounded}")
                return True, "OK"
        except Exception:
            continue

    reason = f"Number near '{ground_truth_name}' does not match ≈{gt_rounded}"
    print(f"❌ {reason}")
    return False, reason
