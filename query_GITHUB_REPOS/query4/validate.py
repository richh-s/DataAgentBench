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

def validate(llm_output: str):
    """
    Validate whether all repo_names appear in LLM output,
    using case-insensitive fuzzy matching (<= 3 char differences).
    """
    ground_truth = [
        "apple/swift",
        "twbs/bootstrap",
        "Microsoft/vscode",
        "facebook/react",
        "tensorflow/tensorflow"
    ]

    llm_output_lower = llm_output.lower()

    for name in ground_truth:
        target = name.lower()
        window_size = len(target) + 3  # allow 3-character fuzzy match
        found = False
        for i in range(len(llm_output_lower) - window_size + 1):
            window = llm_output_lower[i : i + window_size]
            if levenshtein(window, target) <= 3:
                found = True
                break
        if not found:
            reason = f"Could not match: '{name}'"
            return False, reason

    return True, "All repo names matched with fuzzy tolerance."
