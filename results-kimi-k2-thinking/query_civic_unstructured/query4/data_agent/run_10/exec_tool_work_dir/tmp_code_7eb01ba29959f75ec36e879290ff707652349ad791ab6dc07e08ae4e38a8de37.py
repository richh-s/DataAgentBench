code = """import json

# Load data
funding_file = locals()['var_functions.query_db:8']
civic_file = locals()['var_functions.query_db:4']

with open(funding_file) as f:
    funding_records = json.load(f)

with open(civic_file) as f:
    civic_docs = json.load(f)

# Build funding lookup
funding_lookup = {}
for record in funding_records:
    name = record['Project_Name']
    amount = int(record['Amount'])
    if name in funding_lookup:
        funding_lookup[name] = funding_lookup[name] + amount
    else:
        funding_lookup[name] = amount

# Find Spring 2022 projects
spring_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    ltext = text.lower()
    if 'spring 2022' in ltext or '2022-spring' in ltext:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and len(line) > 10:
                if line[0].isupper():
                    lline = line.lower()
                    if 'project' in lline or 'improvement' in lline or 'repair' in lline:
                        spring_projects.add(line)

# Match with funding
results = {}
for project in spring_projects:
    if project in funding_lookup:
        results[project] = funding_lookup[project]
    else:
        for funded in funding_lookup:
            if project.lower() in funded.lower():
                results[funded] = funding_lookup[funded]
                break

count = len(results)
total = 0
for v in results.values():
    total = total + v

print('__RESULT__:')
print(json.dumps({'count': count, 'total_funding': total}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}}

exec(code, env_args)
