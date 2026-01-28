code = """import json

funding_file = locals()['var_functions.query_db:0']
civic_file = locals()['var_functions.query_db:2']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

projects = []

for doc in civic_docs:
    lines = doc.get('text', '').split('\n')
    status = None
    ptype = None
    
    for line in lines:
        line = line.strip()
        if 'Capital Improvement Projects (Design)' in line:
            status = 'design'
            ptype = 'capital'
        elif 'Capital Improvement Projects (Construction)' in line:
            status = 'completed'
            ptype = 'capital'
        elif 'Capital Improvement Projects (Not Started)' in line:
            status = 'not started'
            ptype = 'capital'
        elif status and ptype and line and len(line) < 150:
            if not line.startswith('(') and 'Updates:' not in line and 'Project Schedule' not in line:
                if 'Capital Improvement' not in line and 'Disaster Recovery' not in line:
                    projects.append({'name': line, 'status': status, 'type': ptype})

# Filter and match
capital_design = [p for p in projects if p['status'] == 'design' and p['type'] == 'capital']
matches = []
seen = set()

for proj in capital_design:
    for fund in funding_data:
        if int(fund['Amount']) > 50000:
            p = proj['name'].lower()
            f = fund['Project_Name'].lower()
            if p == f or p in f or f in p:
                if proj['name'] not in seen:
                    seen.add(proj['name'])
                    matches.append(proj['name'])

result = {'count': len(matches)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': {'total_funding_records': 276, 'total_civic_docs': 5, 'first_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'first_civic_keys': ['_id', 'filename', 'text']}}

exec(code, env_args)
