code = """import json, re

# Load the stored query results from files
with open(var_call_SiCHIW4NXPtV3IOtzV6YblHd, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_4VUmllIEoUO1wUaXRg3YRUG6, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Prepare funding records as list of dicts, ensure Amount as int
for rec in funding:
    try:
        rec['Amount'] = int(rec['Amount'])
    except:
        try:
            rec['Amount'] = int(float(rec['Amount']))
        except:
            rec['Amount'] = 0

# Candidate funding projects that are park-related by keywords
park_keywords = ['park', 'walkway', 'playground', 'benches', 'bluffs', 'legacy park', 'south walkway', 'shade structure']
park_funding = [rec for rec in funding if any(k in rec['Project_Name'].lower() for k in park_keywords)]

# Find funding project names that appear near 'completed' and '2022' in civic docs
matched_funding_ids = set()
matched_projects = []

for doc in civic_docs:
    text = doc.get('text','')
    lower = text.lower()
    # find indices of 'completed'
    for m in re.finditer(r'completed', lower):
        i = m.start()
        # window around occurrence
        start = max(0, i-300)
        end = min(len(lower), i+300)
        window = lower[start:end]
        if '2022' in window:
            # check each park-related funding project whether name appears in window
            for rec in park_funding:
                name_low = rec['Project_Name'].lower()
                if name_low in window:
                    if rec['Funding_ID'] not in matched_funding_ids:
                        matched_funding_ids.add(rec['Funding_ID'])
                        matched_projects.append({'Funding_ID': rec['Funding_ID'], 'Project_Name': rec['Project_Name'], 'Amount': rec['Amount']})
            # also capture generic mentions like 'bluffs park' -> try to match partial names
            # e.g., 'bluffs park shade structure' may appear as 'Bluffs Park Shade Structure' already matched
            # Find phrases with 'park' in window and try to match any funding name containing those words
            if 'park' in window:
                # extract candidate substrings around 'park'
                for pk in re.finditer(r'([A-Za-z0-9 &()\-]{0,60}park[A-Za-z0-9 &()\-]{0,60})', window):
                    cand = pk.group(0)
                    for rec in park_funding:
                        if any(word in cand for word in rec['Project_Name'].lower().split() if len(word)>3):
                            if rec['Funding_ID'] not in matched_funding_ids:
                                matched_funding_ids.add(rec['Funding_ID'])
                                matched_projects.append({'Funding_ID': rec['Funding_ID'], 'Project_Name': rec['Project_Name'], 'Amount': rec['Amount']})

# Additionally, some projects might be noted as 'Construction was completed, November 2022' with comma - already covered
# Now compute total amount
total_amount = sum(p['Amount'] for p in matched_projects)

# Prepare result
result = {
    'matched_projects': matched_projects,
    'total_amount': total_amount
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_SiCHIW4NXPtV3IOtzV6YblHd': 'file_storage/call_SiCHIW4NXPtV3IOtzV6YblHd.json', 'var_call_4VUmllIEoUO1wUaXRg3YRUG6': 'file_storage/call_4VUmllIEoUO1wUaXRg3YRUG6.json'}

exec(code, env_args)
