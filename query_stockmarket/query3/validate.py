import re

def validate(llm_output: str) -> (bool, str):
    """
    Validate that:
    - All gt names appear in LLM output (case-insensitive)
    - For each name, a number appears nearby (within 50 chars)
    - Both GT and LLM numbers rounded to nearest integer are equal
    Returns:
        (True, "OK") if all pass
        (False, reason) if not
    """
    gt_pairs = [
        ("Apex Global Brands Inc", 23781.42),
        ("BIO-key International, Inc", 10988.14),
        ("CBAK Energy Technology, Inc", 86223.32),
        ("China Ceramics Co, Ltd", 4366.80),
        ("Correvio Pharma Corp", 145247.83),
        ("CounterPath Corporation", 375.49),
        ("DASAN Zhone Solutions, Inc", 15578.66),
        ("Future FinTech Group Inc", 9.85),
        ("Frontier Communications Corporation", 254397.63),
        ("Ideanomics, Inc", 10.28),
        ("Ocean Power Technologies, Inc", 254.15),
        ("Pacific Ethanol, Inc", 10706.72),
        ("Synthesis Energy Systems, Inc", 2390.51),
        ("Sunesis Pharmaceuticals, Inc", 781.82),
        ("Sypris Solutions, Inc", 36836.36),
    ]

    llm_lower = llm_output.lower()

    for name, value in gt_pairs:
        name_lower = name.lower()
        idx = llm_lower.find(name_lower)
        if idx == -1:
            reason = f"Missing name: {name}"
            print(f"❌ {reason}")
            return False, reason

        # Name found → look within next 50 characters for a number
        window = llm_output[idx: idx + len(name) + 50]
        matches = re.findall(r"(\d+(?:\.\d+)?)", window)

        if not matches:
            reason = f"No number found near name: {name}"
            print(f"❌ {reason}")
            return False, reason

        expected_rounded = round(value)
        found_match = False

        for m in matches:
            try:
                val_rounded = round(float(m))
                if val_rounded == expected_rounded:
                    found_match = True
                    break
            except Exception:
                continue

        if not found_match:
            reason = f"Number near '{name}' does not match rounded {expected_rounded}"
            print(f"❌ {reason}")
            return False, reason

    print("✅ All names and rounded numbers matched.")
    return True, "OK"
