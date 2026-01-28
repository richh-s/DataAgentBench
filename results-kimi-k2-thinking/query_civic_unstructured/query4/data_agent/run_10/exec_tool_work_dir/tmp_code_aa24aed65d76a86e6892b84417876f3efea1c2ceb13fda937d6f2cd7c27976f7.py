code = """import json
import re

# Load civic documents
civic_path = locals()['var_functions.query_db:4']
with open(civic_path, 'r') as file:
    civic_docs = json.load(file)

# Find Spring 2022 projects
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    sections = text.split('\n\n')
    
    for section in sections:
        lower_section = section.lower()
        if 'spring 2022' in lower_section or '2022-spring' in lower_section:
            lines = section.split('\n')
            for line in lines:
                line = line.strip()
                if line and len(line) > 10 and line[0].isupper():
                    if 'project' in line.lower() or 'improvement' in line.lower() or 'repair' in line.lower():
                        spring_projects.append(line)

# Remove duplicates
unique_spring = []
seen = set()
for proj in spring_projects:
    if proj not in seen:
        unique_spring.append(proj)
        seen.add(proj)

print('Spring 2022 project candidates:', len(unique_spring))

# Load funding data
funding_path = locals()['var_functions.query_db:8']
with open(funding_path, 'r') as file:
    funding_records = json.load(file)

# Build funding lookup
funding_lookup = {}
for record in funding_records:
    name = record['Project_Name']
    amount = int(record['Amount'])
    funding_lookup[name] = funding_lookup.get(name, 0) + amount

print('Funding records available:', len(funding_lookup))

# Find matches
matched = {}
for project in unique_spring:
    if project in funding_lookup:
        matched[project] = funding_lookup[project]
    else:
        for funded_name in funding_lookup:
            if project.lower() in funded_name.lower() or funded_name.lower() in project.lower():
                matched[funded_name] = funding_lookup[funded_name]
                break

# Remove duplicates from matched
unique_matched = {}
for name, amount in matched.items():
    if name not in unique_matched:
        unique_matched[name] = amount

total_funding = sum(unique_matched.values())
print('Matched projects:', len(unique_matched))
print('Total funding:', total_funding)

result = {
    'count': len(unique_matched),
    'total_funding': total_funding,
    'projects': list(unique_matched.keys())
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}}

exec(code, env_args)
