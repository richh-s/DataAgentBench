code = """import json
import re

# Load civic docs and funding data from stored files
with open(var_call_eA0xJZWygM8q62BlCiIPmWwv, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

with open(var_call_CVAV72xeKdGMECzEU9GvpR7x, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Normalize funding amounts and identify disaster-related funding records by name
disaster_indicators = ['fema', 'caloes', 'caljpia', 'fema/caloes', 'caloes project', 'fema project', 'caljpia project']

matches = []

# Pre-concatenate all civic texts for easier searching, but also keep per-doc
all_text = "\n".join([doc.get('text','') for doc in civic_docs])
all_text_lower = all_text.lower()

for rec in funding:
    proj_name = rec.get('Project_Name','')
    proj_name_lower = proj_name.lower()
    amount_str = rec.get('Amount', '0')
    try:
        amount = int(amount_str)
    except:
        try:
            amount = int(float(amount_str))
        except:
            amount = 0

    # Determine if funding record is disaster-related by name containing indicators
    is_disaster = any(ind in proj_name_lower for ind in disaster_indicators)

    if not is_disaster:
        # Also consider names where funding source mentions Federal Assistance etc.
        fs = rec.get('Funding_Source','').lower()
        if 'federal assistance' in fs or 'caloes' in fs or 'fema' in fs:
            is_disaster = True

    if not is_disaster:
        continue

    # Try to find project name or base name (without parenthetical suffix) in civic docs
    found = False
    started_2022 = False
    search_terms = [proj_name_lower]
    # add base name without parentheses
    base = re.sub(r"\s*\([^)]*\)", "", proj_name_lower).strip()
    if base and base != proj_name_lower:
        search_terms.append(base)

    for term in search_terms:
        if not term:
            continue
        idx = all_text_lower.find(term)
        if idx != -1:
            found = True
            # Extract a window around the found term and search for '2022'
            start = max(0, idx-300)
            end = min(len(all_text_lower), idx+300)
            window = all_text_lower[start:end]
            if '2022' in window:
                started_2022 = True
            else:
                # Also look for patterns like 'Begin Construction: Fall 2022' or 'Complete Construction: November 2022'
                if re.search(r'begin construction[:\s].{0,50}2022', window) or re.search(r'complete construction[:\s].{0,50}2022', window) or re.search(r'construction was (completed|completed,).{0,50}2022', window):
                    started_2022 = True
            break

    # If not found in combined text, try per-document search to be thorough
    if not found:
        for doc in civic_docs:
            txt = doc.get('text','').lower()
            for term in search_terms:
                idx = txt.find(term)
                if idx != -1:
                    found = True
                    start = max(0, idx-300)
                    end = min(len(txt), idx+300)
                    window = txt[start:end]
                    if '2022' in window:
                        started_2022 = True
                    else:
                        if re.search(r'begin construction[:\s].{0,50}2022', window) or re.search(r'complete construction[:\s].{0,50}2022', window) or re.search(r'construction was (completed|completed,).{0,50}2022', window):
                            started_2022 = True
                    break
            if found:
                break

    if started_2022:
        matches.append({
            'Funding_ID': int(rec.get('Funding_ID')) if rec.get('Funding_ID') and str(rec.get('Funding_ID')).isdigit() else rec.get('Funding_ID'),
            'Project_Name': rec.get('Project_Name'),
            'Amount': amount
        })

# Sum amounts
total = sum(m['Amount'] for m in matches)

# Prepare result
result = {
    'total_funding': total,
    'matched_projects_count': len(matches),
    'matched_projects': matches
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_9m8TflfbCJWo96QQhMCIesyq': ['civic_docs'], 'var_call_eA0xJZWygM8q62BlCiIPmWwv': 'file_storage/call_eA0xJZWygM8q62BlCiIPmWwv.json', 'var_call_81lfzMGYLNjxzefeEW7o1uY3': ['Funding'], 'var_call_CVAV72xeKdGMECzEU9GvpR7x': 'file_storage/call_CVAV72xeKdGMECzEU9GvpR7x.json'}

exec(code, env_args)
