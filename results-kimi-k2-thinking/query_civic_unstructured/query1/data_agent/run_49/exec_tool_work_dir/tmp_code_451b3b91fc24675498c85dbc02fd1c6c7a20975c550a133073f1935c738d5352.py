code = """import json, re

with open(locals()['var_functions.query_db:0'], 'r') as f:
    funding = json.load(f)

with open(locals()['var_functions.query_db:2'], 'r') as f:
    docs = json.load(f)

fund_map = {}
for rec in funding:
    fund_map[rec['Project_Name'].lower().strip()] = int(rec['Amount'])

design_projects = set()
for doc in docs:
    text = doc.get('text','')
    match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?=\n\s*\n[A-Z]|$)', text, re.IGNORECASE|re.DOTALL)
    if match:
        for line in match.group(1).split('\n'):
            line = line.strip()
            if line and not any(line.lower().startswith(x) for x in ['(','cid','updates','complete design','advertise']) and 'Project Schedule' not in line and len(line) > 10:
                design_projects.add(line.lower())

count = sum(1 for proj in design_projects if proj in fund_map and fund_map[proj] > 50000)

for proj in design_projects:
    base = re.sub(r'\s*\([^)]*\)','', proj).strip()
    if proj not in fund_map and base in fund_map and fund_map[base] > 50000:
        count += 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_found': 276, 'sample_projects': ['project_227', 'project_131', 'project_95', 'project_35', 'project_46', 'project_138', 'project_123', 'project_282', 'project_488', 'project_486']}, 'var_functions.execute_python:8': {'funding_count': 38, 'civic_docs_count': 38}, 'var_functions.execute_python:12': {'type': "<class 'str'>", 'is_str': True}, 'var_functions.execute_python:16': {'success': True, 'civic_docs_count': 5, 'funding_count': 276, 'first_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:20': {'num_docs': 5, 'num_funding': 276, 'first_doc_length': 9796}}

exec(code, env_args)
