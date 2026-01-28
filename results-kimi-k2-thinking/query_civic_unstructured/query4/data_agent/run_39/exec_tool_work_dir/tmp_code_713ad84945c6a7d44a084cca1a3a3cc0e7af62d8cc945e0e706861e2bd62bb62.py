code = """import json

# Get data from storage
civic_docs_input = locals().get('var_functions.query_db:5', [])
funding_input = locals().get('var_functions.query_db:8', [])

# Load if file paths
if isinstance(civic_docs_input, str):
    with open(civic_docs_input, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_input

if isinstance(funding_input, str):
    with open(funding_input, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_input

# Find projects starting in Spring 2022
spring_patterns = ['Spring 2022', '2022-Spring', '2022-March', '2022-April', '2022-May', 'March 2022', 'April 2022', 'May 2022']
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 5:
            continue
        following_text = ' '.join(lines[i+1:min(i+15, len(lines))])
        if any(pattern in following_text for pattern in spring_patterns):
            spring_projects.append(line)

# Remove duplicates
spring_projects = list(set(spring_projects))

# Build funding lookup
funding_lookup = {}
for fund in funding_data:
    name = fund.get('Project_Name', '').strip()
    amount = int(fund.get('Amount', 0))
    funding_lookup[name] = funding_lookup.get(name, 0) + amount

# Match and calculate
matched = []
total = 0

for proj in spring_projects:
    if proj in funding_lookup:
        matched.append({'name': proj, 'amount': funding_lookup[proj]})
        total += funding_lookup[proj]

result = {'project_count': len(matched), 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'total_civic_docs': 5, 'total_funding_records': 500}}

exec(code, env_args)
