import re

def levenshtein(s1, s2):
    """
    Standard Levenshtein distance implementation
    """
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
    if len(s2) == 0:
        return len(s1)

    previous = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        current = [i + 1]
        for j, c2 in enumerate(s2):
            insert = previous[j + 1] + 1
            delete = current[j] + 1
            substitute = previous[j] + (c1 != c2)
            current.append(min(insert, delete, substitute))
        previous = current

    return previous[-1]

def validate(llm_output: str) -> (bool, str):
    """
    Validate if target string 'SwiftAndroid/swift' appears in LLM output,
    allowing up to 3 character differences and ignoring case.
    """
    ground_truth = "SwiftAndroid/swift"
    target = ground_truth.lower()
    llm_output_lower = llm_output.lower()

    window_size = len(target) + 3  # allow 3-character fuzzy match
    for i in range(len(llm_output_lower) - window_size + 1):
        window = llm_output_lower[i : i + window_size]
        dist = levenshtein(window, target)
        if dist <= 3:
            print(f"✅ Fuzzy matched: '{window}' with distance {dist}")
            return True, "OK"

    reason = f"❌ No fuzzy match found for '{target}' within 3-character distance"
    print(reason)
    return False, reason
