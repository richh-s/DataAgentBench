code = """import json, os, re
funding_path = locals()['var_functions.query_db:12']
civic_path = locals()['var_functions.query_db:14']
with open(funding_path) as f:
    funding = json.load(f)
with open(civic_path) as f:
    civic_docs = json.load(f)
disaster_2022 = []
for doc in civic_docs:
    lines = doc['text'].split('\n')
    for i, line in enumerate(lines):
        if '2022' in line and len(line) < 150:
            snippet = '\n'.join(lines[max(0,i-3):i+10]).lower()
            if 'fema' in snippet or 'caloes' in snippet:
                disaster_2022.append(line.strip())
disaster_2022 = list(set(disaster_2022))
matched = []
for proj in disaster_2022:
    proj_lower = proj.lower()
    for rec in funding:
        if '(FEMA' in rec['Project_Name'] or '(CalOES' in rec['Project_Name']:
            if proj_lower.split()[0] in rec['Project_Name'].lower():
                matched.append(int(rec['Amount']))
                break
print('__RESULT__:')
print(json.dumps({'total': sum(matched)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': {'success': True, 'num_docs': 5}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'funding_total': 500, 'civic_docs_total': 5, 'disaster_funding_count': 27}}

exec(code, env_args)
