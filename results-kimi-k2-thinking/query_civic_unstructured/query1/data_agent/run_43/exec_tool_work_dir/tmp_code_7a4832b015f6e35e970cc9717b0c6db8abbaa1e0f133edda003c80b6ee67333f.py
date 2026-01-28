code = """import json

funding = var_functions.query_db:90
docs = var_functions.query_db:6

# Simple lists
f_names = [item['Project_Name'] for item in funding]
all_design = []

for doc in docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        # Look for project name patterns (lines without common metadata patterns)
        for line in text.split('\n'):
            line = line.strip()
            if len(line) > 10 and 'Page' not in line and 'Schedule' not in line:
                all_design.append(line.replace('•', '').strip())

# Remove duplicates
design_set = list(set(all_design))

# Count simple matches
count = 0
for proj in design_set:
    proj_lower = proj.lower()
    for funded in f_names:
        funded_lower = funded.lower()
        if proj_lower in funded_lower or funded_lower in proj_lower:
            count += 1
            break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.list_db:82': ['civic_docs'], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:86': [], 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.execute_python:106': {'count': 7}}

exec(code, env_args)
