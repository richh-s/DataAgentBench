import re

def validate(llm_output: str) -> (bool, str):
    """
    Validate if ground truth 'PA' and its number (rounded to 2 decimals) are present in LLM output.
    Returns:
        (True, "OK") if found
        (False, reason) if not
    """
    ground_truth_name = "PA"
    ground_truth_value = 3.699395770392749
    gt_rounded = round(ground_truth_value, 2)

    llm_lower = llm_output.lower()
    name_lower = ground_truth_name.lower()

    # check name
    idx = llm_lower.find(name_lower)
    if idx == -1:
        reason = f"Missing name: {ground_truth_name}"
        print(f"❌ {reason}")
        return False, reason

    # search for number near name (within 50 chars after name)
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
        except:
            continue

    reason = f"Number near '{ground_truth_name}' does not match ≈{gt_rounded}"
    print(f"❌ {reason}")
    return False, reason
