code = """import json, re

civic_path = locals()['var_functions.query_db:6']
funding_path = locals()['var_functions.query_db:8']

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Park' in text and '2022' in text and ('completed' in text.lower() or 'Complete' in text):
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if 'Park' in line and len(line) < 120:
                if 'updates' not in line.lower() and 'schedule' not in line.lower() and 'description' not in line.lower():
                    if line not in park_projects:
                        park_projects.append(line)

funding_matches = []
for project in park_projects:
    proj_key = project.lower().replace(' project', '').strip()
    
    for fund in funding_data:
        fund_name = fund['Project_Name'].lower()
        
        if proj_key in fund_name or fund_name in proj_key:
            funding_matches.append(int(fund['Amount']))

total = sum(funding_matches)
result = {'total_funding': total, 'projects_found': len(park_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
