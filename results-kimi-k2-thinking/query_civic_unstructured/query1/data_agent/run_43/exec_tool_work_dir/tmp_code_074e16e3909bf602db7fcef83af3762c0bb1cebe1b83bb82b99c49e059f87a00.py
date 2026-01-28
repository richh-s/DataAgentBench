code = """import json

# Access funding data
funding_data = var_functions.query_db:90
# Access civic documents
civic_docs = var_functions.query_db:6

# Build funding project names set (already > 50000)
funding_names = set()
for item in funding_data:
    funding_names.add(item['Project_Name'])

# Find design capital projects from civic documents
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    # Check for capital improvement projects in design
    if 'Capital Improvement Projects' in text and 'Design' in text:
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 10:
                # Skip non-project lines
                if 'Page' in line or 'Schedule' in line:
                    continue
                if not line.startswith('202'):
                    design_projects.add(line.replace('•', '').strip())

# Count matches
count = 0
for proj in design_projects:
    proj_lower = proj.lower()
    for funded in funding_names:
        funded_lower = funded.lower()
        # Check name similarity
        if proj_lower in funded_lower or funded_lower in proj_lower:
            if abs(len(proj) - len(funded)) < 40:
                count += 1
                break

result = json.dumps({'count': count})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.list_db:82': ['civic_docs'], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:86': [], 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json'}

exec(code, env_args)
