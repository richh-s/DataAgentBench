code = """import json, re

# Load data
civic_docs = json.load(open(locals()['var_functions.query_db:0']))
funding_data = json.load(open(locals()['var_functions.query_db:2']))

# Find park projects completed in 2022
projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if all(x in text for x in ['completed', '2022']):
        if 'park' in text.lower():
            for line in text.split('\n'):
                line = line.strip()
                if line and 'park' in line.lower() and line[0].isupper():
                    projects.append(line)

unique = list(set(projects))

# Calculate total funding
total = 0
seen = set()
for fund in funding_data:
    name = fund.get('Project_Name', '')
    if 'park' in name.lower() and name not in seen:
        total += int(fund.get('Amount', 0))
        seen.add(name)

answer = 'Total funding for park-related projects completed in 2022 is $' + str(total)
print('__RESULT__:', answer)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:16': ['civic_docs'], 'var_functions.list_db:17': ['Funding']}

exec(code, env_args)
