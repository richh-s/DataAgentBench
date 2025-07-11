import re

def validate(llm_output: str) -> (bool, str):
    """
    Validate LLM output for query1:
    - All names from ground truth must appear.
    - Names must appear in the same order as in ground truth.
    - For each name, a number must appear nearby, which when rounded
      to 2 decimal places matches the ground truth.
    - LLM output can contain numbers of any precision.
    Returns:
        (True, "OK") if valid
        (False, reason) if invalid
    """
    ground_truth = [
        ("Widows Peak Salon", 4.857142857142857),
        ("City Textile", 4.5),
        ("Nobel Textile Co", 4.285714285714286),
        ("San Soo Dang", 4.277777777777778),
        ("Nova Fabrics", 3.3333333333333335)
    ]

    last_index = -1
    for name, true_score in ground_truth:
        # Find the position of the name in LLM output
        idx = llm_output.find(name)
        if idx == -1:
            reason = f"Missing name in LLM output: {name}"
            print(f"❌ {reason}")
            return False, reason

        # Ensure names appear in correct order
        if idx < last_index:
            reason = f"Name out of order: {name}"
            print(f"❌ {reason}")
            return False, reason
        last_index = idx

        # Look for a number within 50 characters after the name
        window = llm_output[idx:idx+50]
        matches = re.findall(r"(\d+\.\d+)", window)
        if not matches:
            reason = f"No score found near {name}"
            print(f"❌ {reason}")
            return False, reason

        # Check if any number in the window matches ground truth rounded to 2 decimals
        gt_rounded = round(true_score, 2)
        for m in matches:
            llm_val = float(m)
            if round(llm_val, 2) == gt_rounded:
                break
        else:
            reason = f"Score mismatch for {name}: expected ~{gt_rounded:.2f}, but not found nearby."
            print(f"❌ {reason}")
            return False, reason

    print("✅ All names and scores are present, in correct order, and scores match within 2 decimals.")
    return True, "OK"
