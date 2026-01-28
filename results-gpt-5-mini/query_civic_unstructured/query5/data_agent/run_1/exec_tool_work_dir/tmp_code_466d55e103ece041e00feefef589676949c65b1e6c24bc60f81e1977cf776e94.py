code = """import json, re
from pathlib import Path

# Load data from storage-provided file paths
civic_docs_path = Path(var_call_oT57ldMG6xcvw4U9HP3yXHI0)
funding_path = Path(var_call_jxu0spdKPCxPgFsEC8FMxpSS)

with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Normalize funding amounts
for r in funding:
    try:
        r['Amount'] = int(r['Amount'])
    except:
        try:
            r['Amount'] = int(float(r['Amount']))
        except:
            r['Amount'] = 0

# Disaster keywords
disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'woolsey']

matches = []

# Pre-concatenate all civic texts for search as well as per-document
all_texts = [d.get('text','') for d in civic_docs]

for row in funding:
    pname = row['Project_Name']
    pname_lower = pname.lower()
    amount = row['Amount']

    # Flag if project name itself indicates disaster
    disaster_by_name = any(k in pname_lower for k in disaster_keywords)

    # Search occurrences in civic documents
    started_in_2022 = False
    disaster_in_text = False
    found_any = False

    # Prepare a simpler base name without parenthetical suffixes for matching
    base_name = re.sub(r"\s*\([^)]*\)", "", pname).strip()
    candidates = [pname, base_name]

    for text in all_texts:
        text_lower = text.lower()
        for cand in candidates:
            if not cand:
                continue
            # case-insensitive search
            idx = text_lower.find(cand.lower())
            if idx != -1:
                found_any = True
                # extract window around match
                start = max(0, idx-200)
                end = min(len(text_lower), idx+len(cand)+400)
                window = text_lower[start:end]
                # check for disaster keywords in window
                if any(k in window for k in disaster_keywords):
                    disaster_in_text = True
                # check for 'begin' or 'start' near and 2022 present
                if '2022' in window and (re.search(r'begin|start', window) or re.search(r'begin\s+construction', window)):
                    started_in_2022 = True
                # also check if 'begin construction' appears elsewhere in doc near other references to project
                # break if both found
                if disaster_in_text and started_in_2022:
                    break
        if disaster_in_text and started_in_2022:
            break

    # If the project is disaster-related (by name or text) and started in 2022, include
    is_disaster = disaster_by_name or disaster_in_text
    if is_disaster and started_in_2022:
        matches.append({'Project_Name': pname, 'Amount': amount})

# Additionally, some disaster projects might appear only in funding table with disaster keywords and may have start info in civic docs under slightly different name; above handled by base_name.

# Sum amounts
total = sum(m['Amount'] for m in matches)

# Prepare result
result = {'total_funding': total, 'matches': matches}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_oT57ldMG6xcvw4U9HP3yXHI0': 'file_storage/call_oT57ldMG6xcvw4U9HP3yXHI0.json', 'var_call_jxu0spdKPCxPgFsEC8FMxpSS': 'file_storage/call_jxu0spdKPCxPgFsEC8FMxpSS.json'}

exec(code, env_args)
