code = """import json

# Get file paths from storage
civic_docs_file = locals()['var_functions.query_db:30']
funding_file = locals()['var_functions.query_db:18']

print('Loading files...')

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_data))

# Look for Spring 2022 projects
spring_months = ['March', 'April', 'May']
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if '2022' in line and any(m in line for m in spring_months):
            for j in range(max(0, i-5), i):
                prev = lines[j].strip()
                if prev and len(prev) > 10 and prev[0].isupper() and 'Schedule:' not in prev:
                    projects.append(prev)
                    break

unique = list(set(projects))
print('Spring 2022 projects:', len(unique))

# Calculate funding
matched = []
total = 0
for proj in unique:
    for fund in funding_data:
        name = fund['Project_Name']
        if proj in name or name in proj:
            amount = int(fund['Amount'])
            matched.append({'project': proj, 'funding': name, 'amount': amount})
            total += amount
            break

result = str(len(unique)) + ' projects, $' + str(total) + ' total funding'
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': [], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
