code = """import json, re

# Load data from storage-provided file paths
with open(var_call_GGBtGSrvfmR2PjrVbxWqZnOH, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_UXCXLtVNi9h3czfNAagVQqhZ, 'r') as f:
    funding = json.load(f)

# Normalize funding records and amounts
for r in funding:
    # Ensure Amount is int
    try:
        r['Amount'] = int(r['Amount'])
    except:
        try:
            r['Amount'] = int(float(r['Amount']))
        except:
            r['Amount'] = 0
    r['Project_Name_str'] = r['Project_Name'] if isinstance(r['Project_Name'], str) else str(r['Project_Name'])

# Disaster-identifying keywords
disaster_keywords = ['fema', 'caloes', 'caljpia', 'cal o es', 'cal oes', 'fema/caloes', 'fema/caloes', 'fire', 'woolsey']

matched_projects = []

# Precompute lowercased doc texts
docs = [d.get('text','').lower() for d in civic_docs]

def doc_contains_basename_with_2022(basename_lower):
    for text in docs:
        idx = text.find(basename_lower)
        if idx != -1:
            # context window
            start = max(0, idx-250)
            end = min(len(text), idx+len(basename_lower)+250)
            window = text[start:end]
            if '2022' in window or '2022' in text:
                return True
    return False

for rec in funding:
    pname = rec['Project_Name_str']
    pname_l = pname.lower()
    is_disaster = any(k in pname_l for k in disaster_keywords)
    if not is_disaster:
        # Also check civic docs text for project mention plus disaster keywords nearby
        # We'll search for project name base in docs and see if disaster keywords present in window
        base = pname_l.split(' (')[0]
        found = False
        for text in docs:
            idx = text.find(base)
            if idx != -1:
                start = max(0, idx-250)
                end = min(len(text), idx+len(base)+250)
                window = text[start:end]
                if any(k in window for k in disaster_keywords) and '2022' in window:
                    found = True
                    break
        if found:
            matched_projects.append({'Project_Name': pname, 'Amount': rec['Amount']})
        continue
    # If project name itself indicates disaster, check civic docs for 2022
    base = pname_l.split(' (')[0]
    if doc_contains_basename_with_2022(base):
        matched_projects.append({'Project_Name': pname, 'Amount': rec['Amount']})

# Sum amounts
total = sum(p['Amount'] for p in matched_projects)

# Prepare result
result = {
    'total_disaster_funding_2022': total,
    'matched_projects': matched_projects
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ymUin5RF95XP4BWWmwjEUFMY': ['civic_docs'], 'var_call_p1QLNVPWU2GvrQ0HmED4NsyZ': ['Funding'], 'var_call_GGBtGSrvfmR2PjrVbxWqZnOH': 'file_storage/call_GGBtGSrvfmR2PjrVbxWqZnOH.json', 'var_call_UXCXLtVNi9h3czfNAagVQqhZ': 'file_storage/call_UXCXLtVNi9h3czfNAagVQqhZ.json'}

exec(code, env_args)
