code = """import json

# Load data from storage files
with open('/tmp/tmp1i3q6xjc.json', 'r') as f:
    civic_docs = json.load(f)

with open('/tmp/tmp6v8h4l_u.json', 'r') as f:
    funding_data = json.load(f)

print('Data loaded')

# Build funding lookup
funding = {}
for r in funding_data:
    name = r['Project_Name']
    amt = int(r['Amount'])
    funding[name] = funding.get(name, 0) + amt

# Find Spring 2022 projects
spring = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        spring.append(text)

print('Spring references found:', len(spring))

# Result placeholder
result = {'count': 0, 'total_funding': 0}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500}

exec(code, env_args)
