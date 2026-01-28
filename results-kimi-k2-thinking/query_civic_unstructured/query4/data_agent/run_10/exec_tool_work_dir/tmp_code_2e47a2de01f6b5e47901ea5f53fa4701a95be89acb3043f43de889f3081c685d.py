code = """import json

# Load funding data
funding_content = locals()['var_functions.query_db:8']
print('Funding data type:', type(funding_content))
if isinstance(funding_content, str) and funding_content.endswith('.json'):
    funding_data = json.load(open(funding_content))
else:
    funding_data = funding_content

print('Funding records:', len(funding_data))

# Build funding lookup
funding_lookup = {}
for record in funding_data:
    name = record['Project_Name']
    amount = int(record['Amount'])
    funding_lookup[name] = funding_lookup.get(name, 0) + amount

print('Unique funded projects:', len(funding_lookup))

# Load civic documents
civic_content = locals()['var_functions.query_db:4']
print('Civic content type:', type(civic_content))
if isinstance(civic_content, str) and civic_content.endswith('.json'):
    civic_docs = json.load(open(civic_content))
else:
    civic_docs = civic_content

print('Civic documents:', len(civic_docs))

# Find Spring 2022 projects
spring_2022_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check for Spring 2022 references
    has_spring_ref = 'Spring 2022' in text or '2022-Spring' in text
    
    if has_spring_ref:
        # Look for potential project names in the same document
        lines = text.split('
')
        for line in lines:
            line = line.strip()
            # Heuristic for project names
            if line and len(line) > 10 and line[0].isupper():
                # Check if it looks like a project name
                if any(word in line.lower() for word in ['project', 'improvement', 'repair', 'replacement', 'renovation']):
                    spring_2022_projects.add(line)

print('Potential Spring 2022 projects found:', len(spring_2022_projects))

# Match with funding database
matched_projects = {}
for project in spring_2022_projects:
    # Direct match first
    if project in funding_lookup:
        matched_projects[project] = funding_lookup[project]
    else:
        # Try fuzzy matching
        proj_lower = project.lower()
        for funded_name in funding_lookup:
            funded_lower = funded_name.lower()
            if proj_lower in funded_lower or funded_lower in proj_lower:
                matched_projects[funded_name] = funding_lookup[funded_name]
                break

# Calculate final results
project_count = len(matched_projects)
total_funding = sum(matched_projects.values())

print('Matched projects:', project_count)
print('Total funding:', total_funding)
print('Projects:', list(matched_projects.keys()))

result = {
    'count': project_count,
    'total_funding': total_funding,
    'projects': list(matched_projects.keys())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500}

exec(code, env_args)
