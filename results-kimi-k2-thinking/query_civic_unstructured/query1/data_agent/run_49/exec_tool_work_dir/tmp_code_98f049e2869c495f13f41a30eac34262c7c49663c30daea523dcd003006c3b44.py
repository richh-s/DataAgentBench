code = """import json
import re

# Load funding data
funding_file = locals()['var_functions.query_db:36']
civic_file = locals()['var_functions.query_db:37']

with open(funding_file, 'r') as f:
    funding_records = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup
funding_lookup = {}
for rec in funding_records:
    key = rec['Project_Name'].lower().strip()
    funding_lookup[key] = int(rec['Amount'])

# Extract design projects
design_projs = []
for doc in civic_docs:
    text = doc.get('text', '')
    section = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?=\n\s*\n[A-Z]|$)', text, re.IGNORECASE|re.DOTALL)
    if section:
        for line in section.group(1).split('\n'):
            stripped = line.strip()
            if stripped and len(stripped) > 10 and not stripped.startswith('('):
                lowered = stripped.lower()
                if 'updates' not in lowered and 'schedule' not in lowered and 'complete design' not in lowered:
                    design_projs.append(lowered)

# Remove duplicates
design_projs = list(set(design_projs))

# Count matches > $50k
count = 0
for proj in design_projs:
    if proj in funding_lookup and funding_lookup[proj] > 50000:
        count = count + 1
    else:
        base = re.sub(r'\s*\([^)]*\)', '', proj).strip()
        if base in funding_lookup and funding_lookup[base] > 50000:
            count = count + 1

result = {'design_projects': len(design_projs), 'funded_over_50k': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_found': 276, 'sample_projects': ['project_227', 'project_131', 'project_95', 'project_35', 'project_46', 'project_138', 'project_123', 'project_282', 'project_488', 'project_486']}, 'var_functions.execute_python:8': {'funding_count': 38, 'civic_docs_count': 38}, 'var_functions.execute_python:12': {'type': "<class 'str'>", 'is_str': True}, 'var_functions.execute_python:16': {'success': True, 'civic_docs_count': 5, 'funding_count': 276, 'first_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:20': {'num_docs': 5, 'num_funding': 276, 'first_doc_length': 9796}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:37': 'file_storage/functions.query_db:37.json'}

exec(code, env_args)
