code = """import json, re

# Load data
with open(locals()['var_functions.query_db:36']) as f:
    funding = json.load(f)
with open(locals()['var_functions.query_db:37']) as f:
    docs = json.load(f)

# Build funding map
fund_map = {}
for rec in funding:
    key = rec['Project_Name'].lower().strip()
    fund_map[key] = int(rec['Amount'])

# Extract design projects
projs = []
for doc in docs:
    t = doc.get('text', '')
    # Find section
    pos = t.lower().find('capital improvement projects (design)')
    if pos > 0:
        section = t[pos:pos+2000]
        for line in section.splitlines():
            ln = line.strip()
            if ln and len(ln) > 10 and ln[0] not in ['(', '\u2022', '']:
                low = ln.lower()
                if all(k not in low for k in ['updates', 'schedule', 'complete design', 'advertise']):
                    projs.append(low)

# Unique projects
unique_projs = set(projs)

# Count matches > 50k
count = 0
for p in unique_projs:
    if p in fund_map and fund_map[p] > 50000:
        count += 1
    else:
        base = re.sub(r'\s*\([^)]*\)', '', p).strip()
        if base in fund_map and fund_map[base] > 50000:
            count += 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_found': 276, 'sample_projects': ['project_227', 'project_131', 'project_95', 'project_35', 'project_46', 'project_138', 'project_123', 'project_282', 'project_488', 'project_486']}, 'var_functions.execute_python:8': {'funding_count': 38, 'civic_docs_count': 38}, 'var_functions.execute_python:12': {'type': "<class 'str'>", 'is_str': True}, 'var_functions.execute_python:16': {'success': True, 'civic_docs_count': 5, 'funding_count': 276, 'first_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:20': {'num_docs': 5, 'num_funding': 276, 'first_doc_length': 9796}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:37': 'file_storage/functions.query_db:37.json'}

exec(code, env_args)
