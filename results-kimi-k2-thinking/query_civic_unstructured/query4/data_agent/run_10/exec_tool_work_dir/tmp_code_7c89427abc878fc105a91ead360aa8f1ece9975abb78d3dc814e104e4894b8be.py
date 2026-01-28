code = """import json
import re

# Load data
civic_path = locals()['var_functions.query_db:4']
funding_path = locals()['var_functions.query_db:8']

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

print('Loaded docs:', len(civic_docs))
print('Loaded funding:', len(funding_records))

# Find Spring 2022 projects
spring_candidates = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and line[0].isupper() and 10 < len(line) < 150:
                lower = line.lower()
                if 'project' in lower or 'improvement' in lower or 'repair' in lower:
                    spring_candidates.append(line)

# Deduplicate
unique_candidates = []
seen = set()
for proj in spring_candidates:
    if proj not in seen:
        unique_candidates.append(proj)
        seen.add(proj)

print('Spring candidates:', len(unique_candidates))

# Build funding lookup
funding_map = {}
for r in funding_records:
    name = r['Project_Name']
    amt = int(r['Amount'])
    funding_map[name] = funding_map.get(name, 0) + amt

print('Unique funded projects:', len(funding_map))

# Match
matches = {}
for project in unique_candidates:
    if project in funding_map:
        matches[project] = funding_map[project]
    else:
        for funded in funding_map:
            if project.lower() in funded.lower() or funded.lower() in project.lower():
                matches[funded] = funding_map[funded]
                break

# Deduplicate matches
final_matches = {}
for name, amount in matches.items():
    if name not in final_matches:
        final_matches[name] = amount

project_count = len(final_matches)
total_funding = sum(final_matches.values())

print('Final matches:', project_count)
print('Total funding:', total_funding)

result = {
    'count': project_count,
    'total_funding': total_funding,
    'projects': list(final_matches.keys())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}}

exec(code, env_args)
