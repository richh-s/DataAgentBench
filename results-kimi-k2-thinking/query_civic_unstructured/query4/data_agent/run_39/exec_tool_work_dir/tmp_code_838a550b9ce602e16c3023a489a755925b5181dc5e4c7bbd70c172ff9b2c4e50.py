code = """import json

# Load the full civic documents data
civic_docs_raw = locals().get('var_functions.query_db:5')

# Check if it's a file path or data
if isinstance(civic_docs_raw, str) and civic_docs_raw.endswith('.json'):
    with open(civic_docs_raw, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_raw

# Load funding data
funding_raw = locals().get('var_functions.query_db:8')
if isinstance(funding_raw, str) and funding_raw.endswith('.json'):
    with open(funding_raw, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_raw

spring_projects = []
spring_patterns = ['Spring 2022', '2022-Spring', '2022-March', '2022-April', '2022-May']

for doc in civic_docs:
    text = doc.get('text', '')
    if any(p in text for p in spring_patterns):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if line and len(line) > 5:
                for pattern in spring_patterns:
                    if pattern in ' '.join(lines[i+1:i+15]):
                        spring_projects.append(line)
                        break

spring_projects = list(set(spring_projects))

funding_lookup = {}
for fund in funding_data:
    name = fund.get('Project_Name', '').strip()
    amount = int(fund.get('Amount', 0))
    funding_lookup[name] = funding_lookup.get(name, 0) + amount

matched = []
total = 0

for proj in spring_projects:
    if proj in funding_lookup:
        matched.append({'name': proj, 'amount': funding_lookup[proj]})
        total += funding_lookup[proj]

result = {'project_count': len(matched), 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'total_civic_docs': 5, 'total_funding_records': 500}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
