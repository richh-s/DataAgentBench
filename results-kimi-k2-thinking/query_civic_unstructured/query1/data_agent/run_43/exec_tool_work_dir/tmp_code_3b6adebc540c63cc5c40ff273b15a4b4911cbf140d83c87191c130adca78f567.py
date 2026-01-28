code = """import json

# Get funding data (already filtered for Amount > 50000)
funding_data = var_functions.query_db:90
funding_names = [item['Project_Name'] for item in funding_data]

# Get civic documents
civic_docs = var_functions.query_db:6

# Find design capital projects
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 10:
                # Skip non-project lines
                skip_terms = ['Page', 'Schedule:', 'Updates:', 'Item ', '2022-', 'Staff ', 'City ', 'Consultant ']
                should_skip = False
                for term in skip_terms:
                    if term in line:
                        should_skip = True
                        break
                if should_skip:
                    continue
                clean_name = line.replace('•', '').replace('○', '').strip()
                if len(clean_name) > 8 and len(clean_name) < 200:
                    design_projects.add(clean_name)

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

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.list_db:82': ['civic_docs'], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:86': [], 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.execute_python:106': {'count': 7}, 'var_functions.query_db:132': 'file_storage/functions.query_db:132.json'}

exec(code, env_args)
