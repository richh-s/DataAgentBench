code = """import json
import re

# Load data from storage file paths
with open(var_call_W9taTNgz80x040dlqFJkcMgI, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_WcTFshncLoA0OkHv5sR0B4J0, 'r') as f:
    funding = json.load(f)

# Normalize texts
for d in civic_docs:
    d['text_norm'] = d['text']

# Helper to strip parenthetical suffixes
def strip_paren(name):
    return re.sub(r"\s*\(.*?\)\s*", "", name).strip()

# Disaster keywords
disaster_kw = ['fema', 'caloes', 'caljpia', 'disaster', 'woolsey', 'fire', 'fema/caloes', 'fema/']

matched_projects = []
total = 0

for rec in funding:
    pname = rec.get('Project_Name','')
    amt_raw = rec.get('Amount', 0)
    try:
        amt = int(amt_raw)
    except:
        try:
            amt = int(float(amt_raw))
        except:
            amt = 0

    base = strip_paren(pname)
    pname_lower = pname.lower()
    base_lower = base.lower()

    # Quick disaster indicator from funding name
    is_disaster_name = any(k in pname_lower for k in ['fema','caloes','caljpia'])

    found_in_2022 = False
    found_disaster_in_text = False

    # Search in civic docs texts
    for d in civic_docs:
        txt = d['text_norm'].lower()
        # find either full name or base in text
        idx = txt.find(pname_lower)
        if idx == -1:
            idx = txt.find(base_lower)
        if idx != -1:
            # get window around match
            start = max(0, idx-300)
            end = min(len(txt), idx+300)
            window = txt[start:end]
            if '2022' in window:
                found_in_2022 = True
            if any(k in window for k in disaster_kw):
                found_disaster_in_text = True
            # if both found we can break early for this rec
            if found_in_2022 and (is_disaster_name or found_disaster_in_text):
                break

    is_disaster = is_disaster_name or found_disaster_in_text
    # Consider project as disaster-related and started in 2022 if both flags true
    if is_disaster and found_in_2022:
        matched_projects.append({'Project_Name': pname, 'Base_Name': base, 'Amount': amt})
        total += amt

# Prepare result
result = {'total_funding': total, 'matched_projects': matched_projects}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_W9taTNgz80x040dlqFJkcMgI': 'file_storage/call_W9taTNgz80x040dlqFJkcMgI.json', 'var_call_WcTFshncLoA0OkHv5sR0B4J0': 'file_storage/call_WcTFshncLoA0OkHv5sR0B4J0.json'}

exec(code, env_args)
