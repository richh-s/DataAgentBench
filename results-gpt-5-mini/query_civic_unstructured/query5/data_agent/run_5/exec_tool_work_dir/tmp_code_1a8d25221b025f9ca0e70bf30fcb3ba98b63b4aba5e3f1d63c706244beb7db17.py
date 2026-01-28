code = """import json
import re

# Load data from storage-provided file paths
with open(var_call_sQ1WBUnx8ul2SmBr22RM4Sts, 'r') as f:
    funding = json.load(f)
with open(var_call_YVbRUFyjTsRLkKhZDfBIVPlk, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding records
fund_records = []
for r in funding:
    name = r.get('Project_Name')
    amt = r.get('Amount')
    try:
        amt_int = int(amt)
    except:
        try:
            amt_int = int(float(amt))
        except:
            amt_int = 0
    fund_records.append({'Project_Name': name, 'Amount': amt_int})

# Prepare indicators
indicators = ['fema','caloes','caljpia','fema/','fema)','fema (','fema project','disaster','fire','woolsey','federal assistance']

def strip_parentheses(s):
    return re.sub(r"\s*\([^)]*\)", "", s).strip()

selected = []

# Pre-lowercase civic docs texts
docs = []
for d in civic_docs:
    txt = d.get('text','')
    docs.append({'filename': d.get('filename'), 'text': txt, 'text_l': txt.lower()})

for rec in fund_records:
    pname = rec['Project_Name']
    pname_l = pname.lower()
    base = strip_parentheses(pname)
    base_l = base.lower()
    is_disaster = any(ind in pname_l for ind in indicators)
    found = False

    # Search docs for base project name
    for doc in docs:
        txt = doc['text_l']
        if base_l and base_l in txt:
            # Check for year 2022 anywhere in that doc
            if '2022' in txt:
                # Check context window around first occurrence
                idx = txt.find(base_l)
                start = max(0, idx-200)
                end = min(len(txt), idx+200)
                window = txt[start:end]
                if is_disaster or any(ind in window for ind in indicators):
                    found = True
                    break
    # Also allow including if pname itself contains indicator and any doc has base and 2022
    if not found and is_disaster:
        # try to ensure it appears in some 2022 doc (even if base not found)
        for doc in docs:
            if '2022' in doc['text_l'] and (pname_l in doc['text_l'] or any(word in doc['text_l'] for word in pname_l.split()[:3])):
                found = True
                break
    if found:
        selected.append(rec)

# Deduplicate by Project_Name (summing duplicates if any duplicates exist as separate rows)
agg = {}
for s in selected:
    name = s['Project_Name']
    agg[name] = agg.get(name, 0) + s['Amount']

total = sum(agg.values())

output = {'total_funding': total, 'projects': [{'Project_Name': k, 'Amount': v} for k,v in agg.items()]}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_j5J7wCganrKDbNBChEdW5TG7': ['civic_docs'], 'var_call_zWFXId4pivHUUXSDRtFXj0HT': ['Funding'], 'var_call_YVbRUFyjTsRLkKhZDfBIVPlk': 'file_storage/call_YVbRUFyjTsRLkKhZDfBIVPlk.json', 'var_call_sQ1WBUnx8ul2SmBr22RM4Sts': 'file_storage/call_sQ1WBUnx8ul2SmBr22RM4Sts.json'}

exec(code, env_args)
