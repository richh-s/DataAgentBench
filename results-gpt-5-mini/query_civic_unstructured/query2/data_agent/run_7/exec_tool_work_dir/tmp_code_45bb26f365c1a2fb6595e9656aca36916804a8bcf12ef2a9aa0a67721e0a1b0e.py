code = """import json

with open(var_call_PKlwf4Qk93xrFly3pK1f1W1I, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_UhGNs1Y0qDSFpmbp65i5E0oC, 'r') as f:
    funding = json.load(f)

# Normalize funding records
for rec in funding:
    rec['Amount'] = int(rec['Amount'])
    rec['name_low'] = rec['Project_Name'].strip().lower()

# Extract park-related project lines from civic docs that mention completion in 2022
park_lines = set()
for doc in civic_docs:
    txt_low = doc.get('text','').lower()
    if 'completed' in txt_low and '2022' in txt_low:
        # collect lines containing park/playground
        for line in doc.get('text','').splitlines():
            if 'park' in line.lower() or 'playground' in line.lower():
                cleaned = line.strip().rstrip(':')
                if cleaned:
                    park_lines.add(cleaned)

# Now match these park project names to funding records (case-insensitive exact or substring)
matched = {}
for pl in park_lines:
    pl_low = pl.lower()
    for rec in funding:
        if pl_low == rec['name_low'] or pl_low in rec['name_low'] or rec['name_low'] in pl_low:
            matched[rec['Project_Name']] = matched.get(rec['Project_Name'], 0) + rec['Amount']

# Also consider funding records with 'park' in name that appear near 'completed' and '2022' in the civic docs text
for rec in funding:
    if 'park' in rec['name_low'] and rec['Project_Name'] not in matched:
        name_low = rec['name_low']
        for doc in civic_docs:
            txt_low = doc.get('text','').lower()
            if name_low in txt_low and 'completed' in txt_low and '2022' in txt_low:
                matched[rec['Project_Name']] = matched.get(rec['Project_Name'], 0) + rec['Amount']
                break

total = sum(matched.values())

result = {
    'park_project_lines_from_docs_completed_in_2022': sorted(list(park_lines)),
    'matched_funding': [{'Project_Name': k, 'Amount': v} for k,v in matched.items()],
    'total_funding_for_park_projects_completed_in_2022': total
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_PKlwf4Qk93xrFly3pK1f1W1I': 'file_storage/call_PKlwf4Qk93xrFly3pK1f1W1I.json', 'var_call_UhGNs1Y0qDSFpmbp65i5E0oC': 'file_storage/call_UhGNs1Y0qDSFpmbp65i5E0oC.json'}

exec(code, env_args)
