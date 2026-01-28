code = """import json

# Load data
civic_path = locals()['var_functions.query_db:4']
funding_path = locals()['var_functions.query_db:8']

civic_docs = json.load(open(civic_path))
funding_data = json.load(open(funding_path))

print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_data))

# Build funding lookup
funding_lookup = {}
for r in funding_data:
    name = r['Project_Name']
    amt = int(r['Amount'])
    funding_lookup[name] = funding_lookup.get(name, 0) + amt

# Find Spring 2022 projects
spring_candidates = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and line[0].isupper() and len(line) > 15:
                lower_line = line.lower()
                if 'project' in lower_line or 'improvement' in lower_line or 'repair' in lower_line:
                    spring_candidates.append(line)

# Remove duplicates
unique_candidates = list(set(spring_candidates))

print('Spring candidates:', len(unique_candidates))

# Match with funding records
matches = {}
for project in unique_candidates:
    if project in funding_lookup:
        matches[project] = funding_lookup[project]
    else:
        for funded_name in funding_lookup:
            if project.lower() in funded_name.lower() or funded_name.lower() in project.lower():
                matches[funded_name] = funding_lookup[funded_name]
                break

# Final results
final_projects = []
final_funding = {}
for name, amount in matches.items():
    if name not in final_funding:
        final_funding[name] = amount
        final_projects.append(name)

project_count = len(final_projects)
total_funding = sum(final_funding.values())

print('Final matches:', project_count)
print('Total funding:', total_funding)

result = {
    'count': project_count,
    'total_funding': total_funding,
    'projects': final_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}}

exec(code, env_args)
