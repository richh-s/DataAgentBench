code = """import json

# Load funding and civic data
funding_path = locals()['var_functions.query_db:8']
civic_path = locals()['var_functions.query_db:4']

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup dictionary
funding_lookup = {}
for record in funding_records:
    name = record['Project_Name']
    amount = int(record['Amount'])
    funding_lookup[name] = funding_lookup.get(name, 0) + amount

# Find projects with Spring 2022 references
spring_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lowertext = text.lower()
    
    # Check for Spring 2022 patterns
    if 'spring 2022' in lowertext or '2022-spring' in lowertext:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and line[0].isupper() and len(line) > 10:
                lline = line.lower()
                keywords = ['project', 'improvement', 'repair', 'replacement']
                if any(k in lline for k in keywords):
                    spring_projects.add(line)

# Match with funding
matched = {}
for project in spring_projects:
    if project in funding_lookup:
        matched[project] = funding_lookup[project]
    else:
        for funded in funding_lookup:
            if project.lower() in funded.lower():
                matched[funded] = funding_lookup[funded]
                break

# Calculate totals
count = len(matched)
total = sum(matched.values())

result = {'count': count, 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}}

exec(code, env_args)
