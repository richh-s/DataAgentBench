code = """import json
from pathlib import Path

# Load file paths from storage variables
funding_path = Path(var_call_sK41BtYb2el82Z4oDCzMktLa)
civic_path = Path(var_call_HkkNDQewlqPXKW3Qv5AHGC1B)

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(civic_path, 'r', encoding='utf-8') as f:
    civic = json.load(f)

# Normalize Amount to int
for r in funding:
    amt = r.get('Amount', 0)
    try:
        r['Amount'] = int(amt)
    except Exception:
        s = str(amt)
        digits = ''.join(ch for ch in s if ch.isdigit())
        r['Amount'] = int(digits) if digits else 0

# disaster keywords
keys = ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'woolsey', 'emergency']

included = {}

# Check each funding record
for fr in funding:
    pname = fr.get('Project_Name', '')
    pname_low = pname.lower()
    amount = fr.get('Amount', 0)
    # If project name itself contains disaster keyword, and any civic doc mentions 2022, include
    if any(k in pname_low for k in keys):
        if any('2022' in doc.get('text','').lower() for doc in civic):
            included[pname] = amount
            continue
    # Otherwise, search civic docs for exact project name mention
    for doc in civic:
        text_low = doc.get('text','').lower()
        if pname_low in text_low:
            # include if this doc mentions 2022 and any disaster keyword
            if '2022' in text_low and any(k in text_low for k in keys):
                included[pname] = amount
                break

# Sum amounts for unique project names
total = sum(v for v in included.values())
projects = [{'Project_Name': k, 'Amount': v} for k,v in included.items()]

result = {'total_funding': total, 'projects': projects}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_vGqZjFy1hiG4jBrsj5lbPjuK': ['civic_docs'], 'var_call_qLHfZfu6d3IXNtIxkCJYCbxo': ['Funding'], 'var_call_sK41BtYb2el82Z4oDCzMktLa': 'file_storage/call_sK41BtYb2el82Z4oDCzMktLa.json', 'var_call_HkkNDQewlqPXKW3Qv5AHGC1B': 'file_storage/call_HkkNDQewlqPXKW3Qv5AHGC1B.json'}

exec(code, env_args)
