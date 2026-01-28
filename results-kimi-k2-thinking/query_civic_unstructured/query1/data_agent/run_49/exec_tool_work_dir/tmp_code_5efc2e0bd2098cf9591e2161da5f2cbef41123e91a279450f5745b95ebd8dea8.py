code = """import json
import re

# Load funding data
funding_path = locals().get('var_functions.query_db:0', '')
with open(funding_path, 'r') as f:
    funding = json.load(f)

# Load civic docs
civic_path = locals().get('var_functions.query_db:2', '')
with open(civic_path, 'r') as f:
    docs = json.load(f)

print('Funding records: %d' % len(funding))
print('Civic documents: %d' % len(docs))

# Build funding map
fund_map = {}
for rec in funding:
    key = rec['Project_Name'].lower().strip()
    fund_map[key] = int(rec['Amount'])

# Find design projects
design_project_names = set()
for doc in docs:
    text = doc.get('text', '')
    # Look for design projects section (case insensitive search)
    if 'Capital Improvement Projects (Design)' in text:
        start = text.index('Capital Improvement Projects (Design)')
        section = text[start: start + 2000]  # Get reasonable chunk
        lines = section.split('\n')
        in_design_list = False
        for line in lines:
            clean = line.strip()
            # Simple heuristic: project names are lines that don't start with special chars
            if clean and len(clean) > 10 and not clean[0] in ['(', '\u2022', '']:
                if 'Updates' not in clean and 'Schedule' not in clean:
                    lower = clean.lower()
                    design_project_names.add(lower)

print('Design projects found: %d' % len(design_project_names))

# Count funded projects > 50k
count = 0
examples = []
for proj in design_project_names:
    if proj in fund_map and fund_map[proj] > 50000:
        count += 1
        examples.append([proj, fund_map[proj]])

print('__RESULT__:')
print(json.dumps({'count': count, 'examples': examples[:5]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_found': 276, 'sample_projects': ['project_227', 'project_131', 'project_95', 'project_35', 'project_46', 'project_138', 'project_123', 'project_282', 'project_488', 'project_486']}, 'var_functions.execute_python:8': {'funding_count': 38, 'civic_docs_count': 38}, 'var_functions.execute_python:12': {'type': "<class 'str'>", 'is_str': True}, 'var_functions.execute_python:16': {'success': True, 'civic_docs_count': 5, 'funding_count': 276, 'first_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:20': {'num_docs': 5, 'num_funding': 276, 'first_doc_length': 9796}}

exec(code, env_args)
