code = """import json
import re

# Load data
with open(locals()['var_functions.query_db:36'], 'r') as f:
    funding_records = json.load(f)

with open(locals()['var_functions.query_db:37'], 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup
funding_map = {rec['Project_Name'].lower().strip(): int(rec['Amount']) for rec in funding_records}

# Extract capital design projects
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?=\n\s*\n[A-Z]|$)', 
                      text, re.IGNORECASE|re.DOTALL)
    if match:
        for line in match.group(1).split('\n'):
            line = line.strip()
            # Skip metadata and get project names
            if line and not any(line.lower().startswith(x) for x in 
                                ['(', 'cid:', 'updates', 'complete design', 'advertise', 'begin construction']):
                if len(line) > 10 and 'Project Schedule' not in line:
                    design_projects.add(line.lower())

# Match with funding > 50k
count = 0
for proj in design_projects:
    if proj in funding_map and funding_map[proj] > 50000:
        count += 1
    else:
        # Try without parenthetical
        base = re.sub(r'\s*\([^)]*\)', '', proj).strip()
        if base in funding_map and funding_map[base] > 50000:
            count += 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_found': 276, 'sample_projects': ['project_227', 'project_131', 'project_95', 'project_35', 'project_46', 'project_138', 'project_123', 'project_282', 'project_488', 'project_486']}, 'var_functions.execute_python:8': {'funding_count': 38, 'civic_docs_count': 38}, 'var_functions.execute_python:12': {'type': "<class 'str'>", 'is_str': True}, 'var_functions.execute_python:16': {'success': True, 'civic_docs_count': 5, 'funding_count': 276, 'first_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:20': {'num_docs': 5, 'num_funding': 276, 'first_doc_length': 9796}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:37': 'file_storage/functions.query_db:37.json'}

exec(code, env_args)
