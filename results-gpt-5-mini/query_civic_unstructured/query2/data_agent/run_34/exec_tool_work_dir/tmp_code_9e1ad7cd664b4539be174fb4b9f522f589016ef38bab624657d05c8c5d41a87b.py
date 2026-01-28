code = """import json
import os

# Load previous tool results from storage variables
# var_call_uw0LKKHz0jh3NTXG9JUM1lhf and var_call_N7KPwlViZqMH6mLKzmuKr0D3 are provided by the tool storage
funding_path = var_call_uw0LKKHz0jh3NTXG9JUM1lhf
civic_path = var_call_N7KPwlViZqMH6mLKzmuKr0D3

# Load JSON content
with open(funding_path, 'r') as f:
    funding = json.load(f)
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Prepare keywords for park-related projects
park_keywords = ['park', 'playground', 'walkway', 'benches', 'bluffs']

matched = []

for rec in funding:
    pname = rec.get('Project_Name','')
    pname_l = pname.lower()
    # Check if funding project name seems park-related
    if not any(kw in pname_l for kw in park_keywords):
        continue
    # Check civic docs for mention of this project being completed in 2022
    found = False
    for doc in civic_docs:
        text = doc.get('text','').lower()
        if pname_l in text and 'completed' in text and '2022' in text:
            found = True
            break
    if found:
        try:
            amt = int(rec.get('Amount',0))
        except:
            # Try to clean amount
            amt = int(''.join(ch for ch in str(rec.get('Amount','0')) if ch.isdigit()))
        matched.append({'Funding_ID': rec.get('Funding_ID'), 'Project_Name': pname, 'Amount': amt})

total = sum(r['Amount'] for r in matched)

# Prepare result dict
result = {'total_funding': total, 'matched_projects': matched}

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_iNhf8SlAwu9kXtvUs725CqW6': ['civic_docs'], 'var_call_e7fKFrdpykYTvYUU9sZS7t98': ['Funding'], 'var_call_uw0LKKHz0jh3NTXG9JUM1lhf': 'file_storage/call_uw0LKKHz0jh3NTXG9JUM1lhf.json', 'var_call_N7KPwlViZqMH6mLKzmuKr0D3': 'file_storage/call_N7KPwlViZqMH6mLKzmuKr0D3.json'}

exec(code, env_args)
