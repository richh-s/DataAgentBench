code = """import json
import re

# Load data
funding_file = locals()['var_functions.query_db:36']
civic_file = locals()['var_functions.query_db:37']

with open(funding_file, 'r') as f:
    funding = json.load(f)
with open(civic_file, 'r') as f:
    docs = json.load(f)

fund_map = {}
for item in funding:
    key = item['Project_Name'].lower().strip()
    fund_map[key] = int(item['Amount'])

design_list = []
pattern = r'Capital Improvement Projects \(Design\)(.*?)(?=\n\s*\n[A-Z]|$)'

for doc in docs:
    text = doc.get('text', '')
    m = re.search(pattern, text, re.IGNORECASE|re.DOTALL)
    if m:
        for ln in m.group(1).split('\n'):
            ln = ln.strip()
            if ln and len(ln) > 10 and not ln.startswith('('):
                low = ln.lower()
                if all(x not in low for x in ['updates', 'schedule', 'complete design', 'advertise', 'begin construction', 'project schedule']):
                    design_list.append(low)

design_set = set(design_list)

cnt = 0
for p in design_set:
    if p in fund_map and fund_map[p] > 50000:
        cnt += 1
    else:
        clean = re.sub(r'\s*\([^)]*\)', '', p).strip()
        if clean in fund_map and fund_map[clean] > 50000:
            cnt += 1

print('__RESULT__:')
print(json.dumps(cnt))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_found': 276, 'sample_projects': ['project_227', 'project_131', 'project_95', 'project_35', 'project_46', 'project_138', 'project_123', 'project_282', 'project_488', 'project_486']}, 'var_functions.execute_python:8': {'funding_count': 38, 'civic_docs_count': 38}, 'var_functions.execute_python:12': {'type': "<class 'str'>", 'is_str': True}, 'var_functions.execute_python:16': {'success': True, 'civic_docs_count': 5, 'funding_count': 276, 'first_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:20': {'num_docs': 5, 'num_funding': 276, 'first_doc_length': 9796}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:37': 'file_storage/functions.query_db:37.json'}

exec(code, env_args)
