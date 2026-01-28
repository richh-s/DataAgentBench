code = """import json
from pathlib import Path

# Load data from storage-provided file paths (variables from previous tool calls)
funding_path = Path(var_call_sK41BtYb2el82Z4oDCzMktLa)
civic_path = Path(var_call_HkkNDQewlqPXKW3Qv5AHGC1B)

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(civic_path, 'r', encoding='utf-8') as f:
    civic = json.load(f)

# Normalize amounts
for r in funding:
    amt = r.get('Amount', 0)
    if isinstance(amt, int):
        r['Amount'] = amt
    else:
        s = str(amt)
        # remove non-digit characters
        digits = ''.join(ch for ch in s if ch.isdigit())
        r['Amount'] = int(digits) if digits else 0

# Disaster-identifying keywords
disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'woolsey', 'emergency']

# Prepare combined civic text for year checks
all_civic_text = '\n'.join(d.get('text', '') for d in civic).lower()

included = {}

# First pass: find funding records whose project name appears in civic docs near disaster keywords and 2022
for fr in funding:
    pname = fr.get('Project_Name', '')
    pname_low = pname.lower()
    amount = fr.get('Amount', 0)
    found = False
    # search each civic doc
    for doc in civic:
        text = doc.get('text', '')
        text_low = text.lower()
        idx = text_low.find(pname_low)
        if idx != -1:
            # window around match
            start = max(0, idx - 500)
            end = min(len(text_low), idx + len(pname_low) + 500)
            window = text_low[start:end]
            has_disaster = any(k in window for k in disaster_keywords) or any(k in pname_low for k in disaster_keywords)
            has_2022 = ('2022' in window) or ('2022' in text_low)
            if has_disaster and has_2022:
                included[pname] = amount
                found = True
                break
    if found:
        continue

# Second pass: include funding records whose project_name contains disaster keywords and there is any mention of 2022 in civic docs
for fr in funding:
    pname = fr.get('Project_Name', '')
    pname_low = pname.lower()
    amount = fr.get('Amount', 0)
    if pname in included:
        continue
    if any(k in pname_low for k in disaster_keywords) and ('2022' in all_civic_text):
        included[pname] = amount

# Third pass: search civic docs for projects mentioned near disaster keywords and 2022 even if name match was fuzzy
# We'll look for lines mentioning 'fema' or 'caloes' and extract nearby project names by heuristics (Title Case sequences)
import re
for doc in civic:
    text = doc.get('text', '')
    text_low = text.lower()
    if '2022' not in text_low:
        continue
    for k in ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'woolsey', 'emergency']:
        for m in re.finditer(k, text_low):
            idx = m.start()
            start = max(0, idx - 300)
            end = min(len(text), idx + 300)
            window = text[start:end]
            # find Title Case phrases in window as candidate project names
            candidates = re.findall(r"([A-Z][A-Za-z0-9&'\- ]{3,50}?(?:Project|Repairs|Improvements|Repair|Road|Park|Roadway|Culvert|Bridge|Drain|Facility|Walkway|Walkway Repairs|Resurfacing|Drainage|Repairs))", window)
            for cand in candidates:
                # match against funding project names approximately
                cand_clean = cand.strip()
                for fr in funding:
                    pname = fr.get('Project_Name', '')
                    if cand_clean.lower() in pname.lower() or pname.lower() in cand_clean.lower():
                        included[pname] = fr.get('Amount', 0)

# Compute total
total = sum(int(v) for v in set(included.values())) if included else 0
# But above sum of set(values) might drop duplicates incorrectly; instead sum unique by project name
total = sum(int(v) for v in included.values())

# Prepare result list
projects = [{'Project_Name': k, 'Amount': v} for k, v in included.items()]

result = {'total_funding': total, 'projects': projects}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_vGqZjFy1hiG4jBrsj5lbPjuK': ['civic_docs'], 'var_call_qLHfZfu6d3IXNtIxkCJYCbxo': ['Funding'], 'var_call_sK41BtYb2el82Z4oDCzMktLa': 'file_storage/call_sK41BtYb2el82Z4oDCzMktLa.json', 'var_call_HkkNDQewlqPXKW3Qv5AHGC1B': 'file_storage/call_HkkNDQewlqPXKW3Qv5AHGC1B.json'}

exec(code, env_args)
