code = """import json
from pathlib import Path

# Load data from storage-provided file paths
with open(var_call_6o4ArY2P01lqjMBIhxsg8MrN, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(var_call_ikN07Szlr2PBmWz7ILEYSXdb, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Helper to normalize strings for matching
import re

def normalize(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

# Build funding records list with numeric amounts
fund_records = []
for r in funding:
    try:
        amt = int(r.get('Amount') or 0)
    except:
        try:
            amt = int(float(r.get('Amount')))
        except:
            amt = 0
    name = r.get('Project_Name','')
    fund_records.append({'Funding_ID': r.get('Funding_ID'), 'name': name, 'name_norm': normalize(name), 'amount': amt})

# Search civic docs for lines/windows indicating completion in 2022
matched_ids = set()
matched_entries = []
for doc in civic_docs:
    text = doc.get('text','')
    # split into lines for context
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    # create normalized lines
    norm_lines = [normalize(ln) for ln in lines]
    for i, ln in enumerate(lines):
        ln_low = ln.lower()
        if 'completed' in ln_low and '2022' in ln_low:
            # build window of text (prev2, prev1, current, next1, next2)
            start = max(0, i-2)
            end = min(len(lines), i+3)
            window = ' '.join(lines[start:end])
            window_norm = normalize(window)
            # check for any funding project name in window
            for fr in fund_records:
                if fr['name_norm'] and fr['name_norm'] in window_norm:
                    if fr['Funding_ID'] not in matched_ids:
                        matched_ids.add(fr['Funding_ID'])
                        matched_entries.append(fr)
            # also, if window contains the word 'park', try to match funding names that include 'park' even if not exact substring
            if 'park' in window_norm:
                for fr in fund_records:
                    if 'park' in fr['name_norm'] and fr['Funding_ID'] not in matched_ids:
                        # fuzzy check: see if most words of fr['name_norm'] appear in window_norm
                        fr_words = fr['name_norm'].split()
                        matches = sum(1 for w in fr_words if w in window_norm)
                        if matches >= max(1, len(fr_words)//3):
                            matched_ids.add(fr['Funding_ID'])
                            matched_entries.append(fr)

# Additionally, look for lines that mention both 'park' and 'construction was completed' variants with 2022
# (already covered), but also look for patterns like 'construction was completed, November 2022' etc.
# Now compute total
total = sum(e['amount'] for e in matched_entries)

# Prepare output
out = {'total_funding': total, 'matched_projects': [{'Funding_ID': e['Funding_ID'], 'Project_Name': e['name'], 'Amount': e['amount']} for e in matched_entries]}

# Print result in required format
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_WnTSRsliNprbQJZz32wKk1dK': ['civic_docs'], 'var_call_FFpie3m1GhPA7SOJXOlVW19h': ['Funding'], 'var_call_6o4ArY2P01lqjMBIhxsg8MrN': 'file_storage/call_6o4ArY2P01lqjMBIhxsg8MrN.json', 'var_call_ikN07Szlr2PBmWz7ILEYSXdb': 'file_storage/call_ikN07Szlr2PBmWz7ILEYSXdb.json'}

exec(code, env_args)
