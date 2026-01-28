code = """import json
import re

# Load data
funding_path = locals().get('var_functions.query_db:0', '')
civic_path = locals().get('var_functions.query_db:2', '')

with open(funding_path) as f:
    funding_data = json.load(f)

with open(civic_path) as f:
    civic_docs = json.load(f)

# Build funding lookup
funding_lookup = {}
for f in funding_data:
    name = f['Project_Name'].strip().lower()
    amount = int(f['Amount'])
    funding_lookup[name] = amount

# Parse projects
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design projects section - simpler approach
    parts = re.split(r'Capital Improvement Projects \(Design\)', text, flags=re.IGNORECASE)
    if len(parts) > 1:
        # Get content after this heading up to next major heading
        section = parts[1].split('\n\n')[0]
        
        for line in section.split('\n'):
            line = line.strip()
            # Filter project names
            if line and not any(line.startswith(x) for x in ['(', 'cid', '\u2022']) and \
               not any(p in line.lower() for p in ['updates', 'project schedule', 'complete design']) and \
               len(line) > 10:
                design_projects.add(line.lower())

# Match with funding > 50k
count = 0
matches = []

for proj in design_projects:
    if proj in funding_lookup and funding_lookup[proj] > 50000:
        count += 1
        matches.append({'project': proj, 'amount': funding_lookup[proj]})
    else:
        # Try without parenthetical
        base = re.sub(r'\s*\([^)]*\)', '', proj).strip()
        if base in funding_lookup and funding_lookup[base] > 50000:
            count += 1
            matches.append({'project': proj, 'amount': funding_lookup[base]})

print('__RESULT__:')
print(json.dumps({'count': count, 'sample': matches[:5]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_found': 276, 'sample_projects': ['project_227', 'project_131', 'project_95', 'project_35', 'project_46', 'project_138', 'project_123', 'project_282', 'project_488', 'project_486']}, 'var_functions.execute_python:8': {'funding_count': 38, 'civic_docs_count': 38}, 'var_functions.execute_python:12': {'type': "<class 'str'>", 'is_str': True}, 'var_functions.execute_python:16': {'success': True, 'civic_docs_count': 5, 'funding_count': 276, 'first_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:20': {'num_docs': 5, 'num_funding': 276, 'first_doc_length': 9796}}

exec(code, env_args)
