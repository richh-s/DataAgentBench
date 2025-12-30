code = """import re, json, pandas as pd
from pathlib import Path

with open(var_call_wO38ZjGimh1uwB8txz3OP2RP, 'r') as f:
    civic_docs = json.load(f)

projects_spring_2022 = set()

patterns = ['Spring 2022', '2022-Spring', '2022 March', 'March 2022', 'April 2022', 'May 2022']

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if any(p in line for p in patterns):
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            if j >= 0:
                name = lines[j].strip()
                if len(name.split()) > 1 and not name.endswith(':'):
                    projects_spring_2022.add(name)

funding = var_call_ZXPtfJt8g3NwUStm2Ba5qIIR

if isinstance(funding, list):
    funding_records = funding
else:
    with open(funding, 'r') as f:
        funding_records = json.load(f)

started_projects = []
for fr in funding_records:
    fname = fr.get('Project_Name', '')
    for pname in projects_spring_2022:
        if fname == pname or fname in pname or pname in fname:
            started_projects.append(fr)
            break

unique_projects = {fr['Project_Name'] for fr in started_projects}

total_projects = len(unique_projects)
total_funding = sum(int(fr['Amount']) for fr in started_projects)

result = {"projects_started_spring_2022": total_projects, "total_funding": total_funding, "matched_projects": sorted(unique_projects)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_wO38ZjGimh1uwB8txz3OP2RP': 'file_storage/call_wO38ZjGimh1uwB8txz3OP2RP.json', 'var_call_ZXPtfJt8g3NwUStm2Ba5qIIR': 'file_storage/call_ZXPtfJt8g3NwUStm2Ba5qIIR.json'}

exec(code, env_args)
