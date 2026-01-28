code = """import json
import re

funding = var_call_ychSnGxEyD6LmutQmtue78yd
civic_path = var_call_ARKTxcuByEvIhdGRDlu4dikK

with open(civic_path, 'r') as f:
    civic_records = json.load(f)

texts = ' '.join(rec['text'] for rec in civic_records)

project_pattern = re.compile(r'(?P<name>[A-Z0-9][A-Za-z0-9 &/().\'-]*?(?:Project|Improvements|Repairs|Repair|Park|Study|Signs|Sirens|Wall|Drain|Bridge|Road|Culvert|Walkway|Playground)[^\n]*?)', re.MULTILINE)

projects_found = set(m.group('name').strip() for m in project_pattern.finditer(texts))

keywords = ('emergency', 'fema')

matching_projects = set()
for p in projects_found:
    lp = p.lower()
    if any(k in lp for k in keywords):
        matching_projects.add(p)

for rec in civic_records:
    t = rec['text'].lower()
    if 'emergency' in t or 'fema' in t:
        for p in list(matching_projects):
            if p.lower() in t:
                pass

funding_df = funding

related_funding = []
for row in funding_df:
    name = row['Project_Name']
    lname = name.lower()
    if 'fema' in lname or 'emergency' in lname:
        related_funding.append({
            'Project_Name': name,
            'Funding_Source': row['Funding_Source'],
            'Amount': int(row['Amount']) if isinstance(row['Amount'], str) and row['Amount'].isdigit() else row['Amount'],
            'Status': None
        })

result = related_funding

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ychSnGxEyD6LmutQmtue78yd': 'file_storage/call_ychSnGxEyD6LmutQmtue78yd.json', 'var_call_ARKTxcuByEvIhdGRDlu4dikK': 'file_storage/call_ARKTxcuByEvIhdGRDlu4dikK.json'}

exec(code, env_args)
