code = """import json
import re

# Load data from files
with open(locals()['var_functions.query_db:40']) as f:
    funding_data = json.load(f)

with open(locals()['var_functions.query_db:5'], encoding='utf-8') as f:
    civic_docs = json.load(f)

# Find capital design projects from civic documents
projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    # Extract section between design header and next major heading
    pattern = r'Capital Improvement Projects \(Design\)(.+?)Capital Improvement Projects \(Construction\)'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        section = match.group(1)
        for line in section.split('\n'):
            clean_line = line.strip()
            if len(clean_line) > 10 and 'Project' in clean_line and 'fema' not in clean_line.lower():
                projects.add(clean_line)

# Match with funding > 50000
count = 0
matched = set()
for rec in funding_data:
    amount = int(rec['Amount'])
    if amount > 50000:
        project_name = rec['Project_Name']
        base_name = project_name.split('(')[0].strip()
        if base_name in projects:
            matched.add(base_name)

count = len(matched)

result = json.dumps({'count': count})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
