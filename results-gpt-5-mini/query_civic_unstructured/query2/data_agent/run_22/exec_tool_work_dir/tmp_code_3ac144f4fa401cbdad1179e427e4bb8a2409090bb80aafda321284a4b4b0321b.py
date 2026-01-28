code = """import json
import re

# Load data from storage-provided file paths
with open(var_call_RoqpFVegPxKrZfJ3cpGXl0EE, 'r') as f:
    funding = json.load(f)
with open(var_call_ulqbMBXAqH2NYSxVEzNCdpb7, 'r') as f:
    docs = json.load(f)

# Normalize funding amounts and project names
for rec in funding:
    # convert Amount to int
    try:
        rec['Amount'] = int(rec.get('Amount') or 0)
    except:
        # remove commas
        s = str(rec.get('Amount') or '0').replace(',', '')
        try:
            rec['Amount'] = int(s)
        except:
            rec['Amount'] = 0
    rec['Project_Name_clean'] = rec.get('Project_Name','').strip().lower()

# Build a single big text for each doc
for d in docs:
    d['text_lower'] = d.get('text','').lower()

# Define park-related keyword filter for funding table
park_keywords = ['park', 'playground', 'walkway', 'bluffs', 'bluff']

# Find funding records that are park-related
park_funding = [r for r in funding if any(k in r['Project_Name_clean'] for k in park_keywords)]

# For each park funding, check if any civic doc indicates completion in 2022
matched = []
for rec in park_funding:
    pname = rec['Project_Name_clean']
    found = False
    for d in docs:
        txt = d['text_lower']
        if pname in txt:
            # check for 'completed' and '2022' in same document
            if 'completed' in txt and '2022' in txt:
                found = True
                break
    if found:
        matched.append({'Project_Name': rec['Project_Name'], 'Amount': rec['Amount']})

# As a fallback, also look for funding projects where doc mentions project base name words
# (e.g., 'bluffs park' might be in doc as 'Bluffs Park Shade Structure')
# We'll also check funding names token by token if not already matched
unmatched = [r for r in park_funding if r['Project_Name'] not in [m['Project_Name'] for m in matched]]
for rec in unmatched:
    tokens = [t for t in re.split(r"\W+", rec['Project_Name_clean']) if t and len(t)>3]
    if not tokens:
        continue
    for d in docs:
        txt = d['text_lower']
        if all(tok in txt for tok in tokens[:2]):  # require first two substantial tokens
            if 'completed' in txt and '2022' in txt:
                matched.append({'Project_Name': rec['Project_Name'], 'Amount': rec['Amount']})
                break

# Remove duplicates
unique = {}
for m in matched:
    unique[m['Project_Name']] = unique.get(m['Project_Name'], 0) + m['Amount']

# Prepare result
matched_list = [{'Project_Name': k, 'Amount': v} for k,v in unique.items()]
total = sum(v for v in unique.values())

out = {'matched_projects': matched_list, 'total_funding_2022_completed_parks': total}

# Print result in required format as JSON string
print("----BEGIN PRINT FORMAT----")
print("print(\"__RESULT__:\")")
import json
print('print(' + json.dumps(json.dumps(out)) + ')')
print("----END PRINT FORMAT----")"""

env_args = {'var_call_ulqbMBXAqH2NYSxVEzNCdpb7': 'file_storage/call_ulqbMBXAqH2NYSxVEzNCdpb7.json', 'var_call_RoqpFVegPxKrZfJ3cpGXl0EE': 'file_storage/call_RoqpFVegPxKrZfJ3cpGXl0EE.json'}

exec(code, env_args)
