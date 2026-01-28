code = """import json, re

# Load data from storage variables provided by previous tool calls
# var_call_FWLvRyVk61pUzu6YC929B7gy and var_call_5JC9iJ9ed8liTfBztXNsUllh

with open(var_call_FWLvRyVk61pUzu6YC929B7gy, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

with open(var_call_5JC9iJ9ed8liTfBztXNsUllh, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Normalize funding amounts and filter park-related funding records
park_funding = []
for rec in funding:
    name = rec.get('Project_Name','')
    amount = rec.get('Amount')
    fid = rec.get('Funding_ID')
    try:
        amt = int(amount)
    except:
        try:
            amt = int(float(amount))
        except:
            amt = 0
    if 'park' in name.lower():
        park_funding.append({'Funding_ID': fid, 'Project_Name': name, 'Amount': amt})

# For each park funding record, search civic docs for evidence of completion in 2022
matched_projects = []
for p in park_funding:
    pname = p['Project_Name']
    pname_l = pname.lower()
    found = False
    for doc in civic_docs:
        text = doc.get('text','')
        text_l = text.lower()
        # If exact project name appears
        idx = text_l.find(pname_l)
        if idx != -1:
            # examine window around occurrence
            start = max(0, idx-400)
            end = min(len(text_l), idx+400)
            window = text_l[start:end]
            if ('2022' in window) and (('complete' in window) or ('construction was completed' in window) or ('notice of completion' in window)):
                found = True
                break
        else:
            # fallback: check presence of key words from project name (e.g., parts) that might be in doc near completion
            # split name into words and check if all significant words present within small span
            tokens = [t for t in re.split('[^a-z0-9]+', pname_l) if t and len(t)>3]
            if tokens:
                # search for first token and then check window
                t0 = tokens[0]
                idx2 = text_l.find(t0)
                if idx2 != -1:
                    start = max(0, idx2-400)
                    end = min(len(text_l), idx2+400)
                    window = text_l[start:end]
                    if all(tok in window for tok in tokens[:3]):
                        if ('2022' in window) and (('complete' in window) or ('construction was completed' in window) or ('notice of completion' in window)):
                            found = True
                            break
    if found:
        matched_projects.append(p)

# Additionally, there might be park projects mentioned in docs that don't have 'park' in funding name but are clearly park-related by context. We'll also scan civic docs for lines mentioning 'park' and 'completed' and '2022' and try to match funding entries by fuzzy name inclusion.
# Build a set of project names already matched to avoid duplicates
matched_names = set([p['Project_Name'] for p in matched_projects])

# Scan civic docs for park-completed-2022 snippets
park_completed_snippets = []
for doc in civic_docs:
    text = doc.get('text','')
    text_l = text.lower()
    # find occurrences where 'park' and 'complete' and '2022' appear within 500 chars
    for m in re.finditer('park', text_l):
        i = m.start()
        start = max(0, i-300)
        end = min(len(text_l), i+300)
        window = text_l[start:end]
        if ('2022' in window) and (('complete' in window) or ('construction was completed' in window) or ('notice of completion' in window)):
            snippet = window
            park_completed_snippets.append(snippet)

# Try to match funding records (even if they didn't include 'park' in name) to these snippets by checking if funding project name tokens appear in any snippet
for rec in funding:
    name = rec.get('Project_Name','')
    if name in matched_names:
        continue
    name_l = name.lower()
    # Only consider names with at least one of common park keywords or containing parts like 'bluffs','malibu','playground','walkway','park'
    if any(k in name_l for k in ['park','bluffs','playground','walkway','bench','paver','shade','playground','play area']):
        tokens = [t for t in re.split('[^a-z0-9]+', name_l) if t and len(t)>3]
        for snippet in park_completed_snippets:
            if all(tok in snippet for tok in tokens[:3]):
                try:
                    amt = int(rec.get('Amount') or 0)
                except:
                    amt = 0
                matched_projects.append({'Funding_ID': rec.get('Funding_ID'), 'Project_Name': name, 'Amount': amt})
                matched_names.add(name)
                break

# Sum amounts
total = sum(p['Amount'] for p in matched_projects)

result = {'total_funding': total, 'projects': matched_projects}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_FWLvRyVk61pUzu6YC929B7gy': 'file_storage/call_FWLvRyVk61pUzu6YC929B7gy.json', 'var_call_5JC9iJ9ed8liTfBztXNsUllh': 'file_storage/call_5JC9iJ9ed8liTfBztXNsUllh.json'}

exec(code, env_args)
