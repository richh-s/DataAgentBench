code = """import json
import re

# Load data files
civic_path = locals()['var_functions.query_db:6']
funding_path = locals()['var_functions.query_db:5']

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Build funding lookup
total_funds = {}
for row in funding_data:
    name = row.get('Project_Name', '')
    amount = int(row.get('Amount', 0))
    if name and amount > 0:
        total_funds[name] = total_funds.get(name, 0) + amount

# Extract projects from civic docs
project_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Look for project names (title case lines) followed by 2022 spring references
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Basic heuristic: first uppercase line before schedule info
        if line and line[0].isupper() and len(line) < 80:
            # Look ahead for spring 2022
            lookahead = ' '.join(lines[i:i+10]).lower()
            if '2022' in lookahead and ('spring' in lookahead or 'march' in lookahead or 'april' in lookahead or 'may' in lookahead):
                project_names.add(line)

# Match projects with funding
matched = []
total = 0

for project in project_names:
    # Direct match
    if project in total_funds:
        matched.append(project)
        total += total_funds[project]
        continue
    
    # Try fuzzy match
    for funded_name in total_funds:
        if project.lower() in funded_name.lower() or funded_name.lower() in project.lower():
            matched.append(project)
            total += total_funds[funded_name]
            break

result = {'project_count': len(matched), 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_documents': 5, 'status': 'loaded'}}

exec(code, env_args)
