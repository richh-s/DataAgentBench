code = """import json

# Load data from the two databases
with open(locals()['var_functions.query_db:8'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_functions.query_db:4'], 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup dictionary
funding_lookup = {}
for r in funding_data:
    name = r['Project_Name']
    amount = int(r['Amount'])
    funding_lookup[name] = funding_lookup.get(name, 0) + amount

# Find Spring 2022 projects in civic documents
spring_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    if 'spring 2022' in lower_text or '2022-spring' in lower_text:
        for line in text.split('\n'):
            line = line.strip()
            if line and line[0].isupper():
                lower_line = line.lower()
                keywords = ['project', 'improvement', 'repair']
                if any(k in lower_line for k in keywords):
                    spring_projects.add(line)

# Match with funding records
matched = {}
for project in spring_projects:
    if project in funding_lookup:
        matched[project] = funding_lookup[project]
    else:
        for funded in funding_lookup:
            if project.lower() in funded.lower():
                matched[funded] = funding_lookup[funded]
                break

# Calculate final results
count = len(matched)
total_funding = sum(matched.values())

result = {'count': count, 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}}

exec(code, env_args)
