code = """import json, os, sys

civic_path = locals()['var_functions.query_db:0']
funding_path = locals()['var_functions.query_db:5']

with open(civic_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding_data = json.load(f)

emergency_projects = []
project_names = set()

for f in funding_data:
    pname = f['Project_Name']
    if 'fema' in pname.lower():
        emergency_projects.append({
            'Project_Name': pname,
            'Funding_Source': f['Funding_Source'],
            'Amount': int(f['Amount']),
            'Status': 'Status not found in civic docs'
        })
        project_names.add(pname.lower())

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    for line in lines:
        low = line.lower()
        if 'emergency' in low or 'fema' in low:
            clean = line.strip()
            if len(clean) > 8 and not clean.startswith('('):
                if clean.lower() not in project_names:
                    find_fund = None
                    for fund in funding_data:
                        if clean in fund['Project_Name'] or fund['Project_Name'] in clean:
                            find_fund = fund
                            break
                    if find_fund:
                        amount = int(find_fund['Amount'])
                        source = find_fund['Funding_Source']
                    else:
                        amount = 0
                        source = 'Unknown source'
                    
                    emergency_projects.append({
                        'Project_Name': clean,
                        'Funding_Source': source,
                        'Amount': amount,
                        'Status': 'Mentioned in civic docs'
                    })
                    project_names.add(clean.lower())

emergency_projects.sort(key=lambda x: x['Amount'], reverse=True)

print('__RESULT__:')
print(json.dumps(emergency_projects))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json'}

exec(code, env_args)
