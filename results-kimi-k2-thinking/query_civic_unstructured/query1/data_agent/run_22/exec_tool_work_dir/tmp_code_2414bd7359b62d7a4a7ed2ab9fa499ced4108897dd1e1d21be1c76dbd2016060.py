code = """import json
funding_file = locals()['var_functions.query_db:0']
civic_file = locals()['var_functions.query_db:2']

with open(funding_file, 'r') as f:
    funding = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract projects from text
projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
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
        elif status and ptype and line:
            if not line.startswith('(') and 'Updates:' not in line and 'Project Schedule' not in line and len(line) < 150:
                if 'Capital Improvement' not in line and 'Disaster Recovery' not in line:
                    projects.append({'name': line, 'status': status, 'type': ptype})

# Find matches
result_set = set()
for proj in projects:
    if proj['status'] == 'design' and proj['type'] == 'capital':
        for fund in funding:
            if int(fund['Amount']) > 50000:
                if proj['name'].lower() in fund['Project_Name'].lower() or fund['Project_Name'].lower() in proj['name'].lower():
                    result_set.add(proj['name'])

result = {'count': len(result_set)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': {'total_funding_records': 276, 'total_civic_docs': 5, 'first_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'first_civic_keys': ['_id', 'filename', 'text']}}

exec(code, env_args)
