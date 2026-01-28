code = """import json, re

civic_docs = json.load(open('var_functions.query_db_6'))
funding = json.load(open('var_functions.query_db_8'))

park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for park projects completed in 2022
    # Search for pattern: Park name followed by completion in 2022
    pattern = r'([A-Za-z\s]+Park[A-Za-z\s]*)[^\n]*?(?:Construction was completed)[^\n]*2022'
    matches = re.finditer(pattern, text, re.IGNORECASE | re.DOTALL)
    for m in matches:
        name = m.group(1).strip()
        if name and name not in park_projects:
            park_projects.append(name)

# Match with funding records
total = 0
count = 0

for project in park_projects:
    proj_lower = project.lower()
    for f in funding:
        fund_name = f['Project_Name'].lower()
        if proj_lower == fund_name:
            total += int(f['Amount'])
            count += 1

result = {'total_funding': total, 'matching_projects': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
