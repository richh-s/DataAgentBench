code = """import json, re

# Load funding data (>50k)
funding_file = locals()['var_functions.query_db:36']
civic_file = locals()['var_functions.query_db:37']

with open(funding_file, 'r') as f:
    funding = json.load(f)
with open(civic_file, 'r') as f:
    docs = json.load(f)

# Create lookup for funding amounts
fund_lookup = {}
for item in funding:
    name = item['Project_Name'].lower().strip()
    fund_lookup[name] = int(item['Amount'])

# Extract capital design projects from documents
design_prjs = set()
for doc in docs:
    text = doc.get('text', '')
    section = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?=\n\s*\n[A-Z]|$)', 
                        text, re.IGNORECASE|re.DOTALL)
    if section:
        for line in section.group(1).split('\n'):
            line = line.strip()
            if line and len(line) > 10 and not line.startswith('('):
                low = line.lower()
                if 'updates' not in low and 'schedule' not in low:
                    design_prjs.add(low)

# Count funded projects over 50k
cnt = 0
for prj in design_prjs:
    if prj in fund_lookup and fund_lookup[prj] > 50000:
        cnt += 1
    else:
        base = re.sub(r'\s*\([^)]*\)', '', prj).strip()
        if base in fund_lookup and fund_lookup[base] > 50000:
            cnt += 1

print('__RESULT__:')
print(json.dumps(cnt))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_found': 276, 'sample_projects': ['project_227', 'project_131', 'project_95', 'project_35', 'project_46', 'project_138', 'project_123', 'project_282', 'project_488', 'project_486']}, 'var_functions.execute_python:8': {'funding_count': 38, 'civic_docs_count': 38}, 'var_functions.execute_python:12': {'type': "<class 'str'>", 'is_str': True}, 'var_functions.execute_python:16': {'success': True, 'civic_docs_count': 5, 'funding_count': 276, 'first_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:20': {'num_docs': 5, 'num_funding': 276, 'first_doc_length': 9796}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:37': 'file_storage/functions.query_db:37.json'}

exec(code, env_args)
