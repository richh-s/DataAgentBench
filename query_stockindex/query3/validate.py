def validate(llm_output: str) -> (bool, str):
    """
    Validate that:
    - All name+country pairs from ground truth appear in LLM output
    - In the same order (not necessarily contiguous)
    - Name is followed (within 50 chars) by country
    - Case-insensitive

    Returns:
        (True, "OK") if all good
        (False, reason) if failed
    """
    gt_pairs = [
        ("399001.SZ", "China"),
        ("NSEI", "India"),
        ("IXIC", "United States"),
        ("000001.SS", "China"),
        ("NYA", "United States"),
    ]

    llm_lower = llm_output.lower()
    last_idx = -1

    for name, country in gt_pairs:
        name_lower = name.lower()
        country_lower = country.lower()

        idx = llm_lower.find(name_lower, last_idx + 1)
        if idx == -1:
            reason = f"Missing name: {name}"
            print(f"❌ {reason}")
            return False, reason

        window = llm_lower[idx: idx + len(name_lower) + 20]
        if country_lower not in window:
            reason = f"Country '{country}' not found within 50 chars after name '{name}'"
            print(f"❌ {reason}")
            return False, reason

        last_idx = idx

    print("✅ All name-country pairs found in correct order and close proximity.")
    return True, "OK"
