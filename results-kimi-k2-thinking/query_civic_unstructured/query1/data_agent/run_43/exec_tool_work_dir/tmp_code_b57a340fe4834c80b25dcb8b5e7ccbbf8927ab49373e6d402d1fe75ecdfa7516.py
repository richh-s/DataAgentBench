code = """import json

# Access the stored results properly
funding_data = locals()['var_functions.query_db:90']
civic_docs = locals()['var_functions.query_db:6']

# Build funding names list
funding_names = []
for item in funding_data:
    if isinstance(item, dict) and 'Project_Name' in item:
        funding_names.append(item['Project_Name'])

# Find design projects
design_projects = set()
for doc in civic_docs:
    if isinstance(doc, dict) and 'text' in doc:
        text = doc['text']
        if 'Capital Improvement Projects' in text and 'Design' in text:
            for line in text.split('\n'):
                line = line.strip()
                if line and len(line) > 10:
                    # Filter out non-project lines
                    if not any(skip in line for skip in ['Page', 'Schedule:', 'Updates:', 'Item ', '2022-']):
                        clean = line.replace('•', '').replace('○', '').strip()
                        if len(clean) > 8 and len(clean) < 200:
                            design_projects.add(clean)

# Count matches
count = 0
for proj in design_projects:
    proj_lower = proj.lower()
    for funded in funding_names:
        funded_lower = funded.lower()
        if proj_lower in funded_lower or funded_lower in proj_lower:
            if abs(len(proj) - len(funded)) < 40:
                count += 1
                break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.list_db:82': ['civic_docs'], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:86': [], 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.execute_python:106': {'count': 7}}

exec(code, env_args)
