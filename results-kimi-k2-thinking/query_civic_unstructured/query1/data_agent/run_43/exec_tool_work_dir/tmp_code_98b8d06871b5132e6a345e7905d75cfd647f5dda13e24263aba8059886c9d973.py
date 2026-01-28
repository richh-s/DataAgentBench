code = """import json
import os

# Get stored results
funding_result = var_functions.query_db:60
civic_result = var_functions.query_db:6

# These are file paths
print('Funding file:', funding_result)
print('Civic file:', civic_result)

# Load data from files
funding_data = json.load(open(funding_result))
civic_docs = json.load(open(civic_result))

print('Total funding records:', len(funding_data))
print('Total civic documents:', len(civic_docs))

# Get project names from funding
funding_projects = set()
for item in funding_data:
    funding_projects.add(item['Project_Name'])

# Extract design capital projects from civic documents
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and len(line) > 10 and not any(x in line for x in ['Page', 'Schedule:', 'Updates:']):
                design_projects.add(line.replace('•', '').strip())

# Count matches
match_count = 0
for design in design_projects:
    d_lower = design.lower()
    for funded in funding_projects:
        f_lower = funded.lower()
        if d_lower in f_lower or f_lower in d_lower:
            if abs(len(design) - len(funded)) < 40:
                match_count += 1
                break

# Output result
result = {'count': match_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
