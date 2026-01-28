code = """import json, re, os

# Load previous tool results stored as file paths
with open(var_call_8SkE5F1pcJP7D4j2FT2FzXVg, 'r') as f:
    funding = json.load(f)
with open(var_call_jm0EZnNIySW9PRFtrxrYOPvZ, 'r') as f:
    docs = json.load(f)

# Get funded projects with Amount > 50000 (records already filtered by query)
funded_projects = []
for rec in funding:
    try:
        amt = int(rec.get('Amount', 0))
    except:
        try:
            amt = int(float(rec.get('Amount', 0)))
        except:
            amt = 0
    if amt > 50000:
        funded_projects.append(rec.get('Project_Name', '').strip())

funded_projects = list(dict.fromkeys(funded_projects))  # preserve order unique

# Prepare candidate name variants (original and stripped parentheses suffix)
candidate_map = {}
for name in funded_projects:
    variants = set()
    variants.add(name.lower())
    # strip trailing parenthetical suffixes
    base = re.sub(r"\s*\([^)]*\)\s*$", "", name).strip()
    if base:
        variants.add(base.lower())
    # also replace multiple spaces
    variants = {re.sub(r"\s+", " ", v) for v in variants}
    candidate_map[name] = list(variants)

# Headers for design section and section delimiters
design_headers = ['capital improvement projects (design)', 'capital improvement projects - design', 'capital improvement projects (design):', 'capital improvement projects \(design\)']
section_delimiters = [
    'capital improvement projects (construction)',
    'capital improvement projects (not started)',
    'capital improvement projects (construction)',
    'capital improvement projects (not started)',
    'capital improvement projects (design)',
    'capital improvement projects (construction)',
    'capital improvement projects (not started)',
    'capital improvement projects (design)'
]

matches = set()

for doc in docs:
    text = doc.get('text', '')
    lower = text.lower()
    # Find all design header positions
    for hdr in design_headers:
        if hdr in lower:
            # find first occurrence
            start = lower.find(hdr)
            start_pos = start + len(hdr)
            # find next delimiter after start_pos
            next_pos = len(lower)
            for delim in section_delimiters:
                idx = lower.find(delim, start_pos)
                if idx != -1 and idx < next_pos:
                    next_pos = idx
            section = lower[start_pos:next_pos]
            # Search for candidate project names in this section
            for orig_name, variants in candidate_map.items():
                for v in variants:
                    if v and v in section:
                        matches.add(orig_name)
                        break

# As a fallback, also search for phrases indicating 'design' near project name occurrences
# e.g., if project name appears and within 200 chars there's 'design' or 'preliminary design' or 'complete design'
for doc in docs:
    text = doc.get('text', '')
    lower = text.lower()
    for orig_name, variants in candidate_map.items():
        if orig_name in matches:
            continue
        found = False
        for v in variants:
            if v and v in lower:
                idx = lower.find(v)
                if idx != -1:
                    window_start = max(0, idx - 200)
                    window_end = min(len(lower), idx + 200)
                    window = lower[window_start:window_end]
                    if 'design' in window or 'preliminary design' in window or 'complete design' in window or 'final design' in window:
                        matches.add(orig_name)
                        found = True
                        break
        if found:
            continue

result_projects = sorted(matches)
result_count = len(result_projects)

out = {"count": result_count, "projects": result_projects}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_8SkE5F1pcJP7D4j2FT2FzXVg': 'file_storage/call_8SkE5F1pcJP7D4j2FT2FzXVg.json', 'var_call_jm0EZnNIySW9PRFtrxrYOPvZ': 'file_storage/call_jm0EZnNIySW9PRFtrxrYOPvZ.json'}

exec(code, env_args)
