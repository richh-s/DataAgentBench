code = """import json
import re

funding_result = var_functions.query_db:0
civic_result = var_functions.query_db:2

if isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_result

if isinstance(civic_result, str) and civic_result.endswith('.json'):
    with open(civic_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_result

print('Funding records:', len(funding_records))
print('Civic docs:', len(civic_docs))

design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    t_lower = text.lower()
    
    if 'capital improvement projects' in t_lower and 'design' in t_lower:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) >= 10:
                skip = ['updates', 'schedule', 'staff', 'city council', 'consultant', 'discussion', 'page', 'complete design', 'advertise', 'construction', 'project ', 'to:', 'from:', 'date:', 'subject:']
                if not any(term in line.lower() for term in skip):
                    keywords = ['road', 'avenue', 'drive', 'park', 'drain', 'storm', 'bridge', 'walkway', 'trail', 'sewer', 'water', 'traffic', 'signal', 'sign', 'median', 'crosswalk', 'improvements', 'repairs', 'project', 'structure', 'facility']
                    if any(k in line.lower() for k in keywords):
                        design_projects.append(line)

design_projects = list(set(design_projects))
print('Design projects found:', len(design_projects))

matches = 0
for proj in design_projects:
    proj_l = proj.lower()
    for fund in funding_records:
        amt = int(fund['Amount'])
        if amt > 50000:
            fund_l = fund['Project_Name'].lower()
            if proj_l == fund_l or proj_l in fund_l or fund_l in proj_l:
                matches += 1
                break

print('Matches with funding > 50000:', matches)
result = {'count': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
