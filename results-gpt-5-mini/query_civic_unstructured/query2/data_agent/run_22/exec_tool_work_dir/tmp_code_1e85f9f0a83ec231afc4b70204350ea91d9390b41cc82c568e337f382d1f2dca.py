code = """import json
import re

# Load data from storage-provided file paths
with open(var_call_RoqpFVegPxKrZfJ3cpGXl0EE, 'r') as f:
    funding = json.load(f)
with open(var_call_ulqbMBXAqH2NYSxVEzNCdpb7, 'r') as f:
    docs = json.load(f)

# Normalize funding amounts and project names
for rec in funding:
    try:
        rec['Amount'] = int(rec.get('Amount') or 0)
    except:
        s = str(rec.get('Amount') or '0').replace(',', '')
        try:
            rec['Amount'] = int(s)
        except:
            rec['Amount'] = 0
    rec['Project_Name_clean'] = rec.get('Project_Name','').strip().lower()

# Lowercase doc texts
for d in docs:
    d['text_lower'] = d.get('text','').lower()

# Park-related keywords to match funding records
park_keywords = ['park', 'playground', 'walkway', 'bluffs', 'bluff']
park_funding = [r for r in funding if any(k in r['Project_Name_clean'] for k in park_keywords)]

matched = []
for rec in park_funding:
    pname = rec['Project_Name_clean']
    found = False
    for d in docs:
        txt = d['text_lower']
        if pname in txt:
            if 'completed' in txt and '2022' in txt:
                found = True
                break
    if found:
        matched.append({'Project_Name': rec['Project_Name'], 'Amount': rec['Amount']})

# Fallback matching using tokens
unmatched = [r for r in park_funding if r['Project_Name'] not in [m['Project_Name'] for m in matched]]
for rec in unmatched:
    tokens = [t for t in re.split(r"\W+", rec['Project_Name_clean']) if t and len(t)>3]
    if not tokens:
        continue
    for d in docs:
        txt = d['text_lower']
        # require first token and a park keyword present
        if tokens[0] in txt and any(k in txt for k in park_keywords):
            if 'completed' in txt and '2022' in txt:
                matched.append({'Project_Name': rec['Project_Name'], 'Amount': rec['Amount']})
                break

# Aggregate unique projects
unique = {}
for m in matched:
    unique[m['Project_Name']] = unique.get(m['Project_Name'], 0) + m['Amount']

matched_list = [{'Project_Name': k, 'Amount': v} for k,v in unique.items()]
total = sum(v for v in unique.values())

out = {'matched_projects': matched_list, 'total_funding_2022_completed_parks': total}

# Print result in required format
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_ulqbMBXAqH2NYSxVEzNCdpb7': 'file_storage/call_ulqbMBXAqH2NYSxVEzNCdpb7.json', 'var_call_RoqpFVegPxKrZfJ3cpGXl0EE': 'file_storage/call_RoqpFVegPxKrZfJ3cpGXl0EE.json'}

exec(code, env_args)
