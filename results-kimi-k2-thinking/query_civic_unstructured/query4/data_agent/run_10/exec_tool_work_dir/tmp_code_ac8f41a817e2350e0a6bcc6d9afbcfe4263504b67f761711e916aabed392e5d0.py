code = """import json
import re

# Load data
civic_docs = json.load(open(locals()['var_functions.query_db:4']))
funding_data = json.load(open(locals()['var_functions.query_db:8']))

print(f"Loaded {len(civic_docs)} civic documents and {len(funding_data)} funding records")

# Build funding lookup
funding_lookup = {}
for record in funding_data:
    name = record['Project_Name']
    amt = int(record['Amount'])
    funding_lookup[name] = funding_lookup.get(name, 0) + amt

# Find projects with Spring 2022 references
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        # Look for project names in the text
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and line[0].isupper():
                if len(line) > 15 and len(line) < 150:
                    lower = line.lower()
                    if 'project' in lower or 'improvement' in lower or 'repair' in lower:
                        spring_projects.append(line)

# Remove duplicates
seen = set()
unique_spring = []
for proj in spring_projects:
    if proj not in seen:
        unique_spring.append(proj)
        seen.add(proj)

print(f"Found {len(unique_spring)} potential Spring 2022 projects")

# Match with funding
matched = {}
for project in unique_spring:
    if project in funding_lookup:
        matched[project] = funding_lookup[project]
    else:
        # Try partial matching
        for funded in funding_lookup:
            if project.lower() in funded.lower() or funded.lower() in project.lower():
                matched[funded] = funding_lookup[funded]
                break

# Remove duplicates
final_matches = {}
for name, amount in matched.items():
    if name not in final_matches:
        final_matches[name] = amount

project_count = len(final_matches)
total_funding = sum(final_matches.values())

print(f"Matched {project_count} projects with total funding ${total_funding}")

result = {
    'count': project_count,
    'total_funding': total_funding,
    'projects': list(final_matches.keys())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}}

exec(code, env_args)
