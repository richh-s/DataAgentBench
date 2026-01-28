code = """import json

# Load funding data first
funding_file = locals()['var_functions.query_db:8']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Build funding lookup - summing amounts for same project
funding_lookup = {}
for record in funding_records:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    if project_name in funding_lookup:
        funding_lookup[project_name] += amount
    else:
        funding_lookup[project_name] = amount

print('Funding lookup built with', len(funding_lookup), 'projects')

# Load civic documents
civic_file = locals()['var_functions.query_db:4']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print('Processing', len(civic_docs), 'civic documents')

# Find Spring 2022 project references
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        # Split into lines and find project names
        for line in text.split('\n'):
            line = line.strip()
            # Basic heuristic: project names are capitalized, reasonable length, contain keywords
            if line and len(line) > 15 and line[0].isupper():
                lower_line = line.lower()
                if 'project' in lower_line or 'improvement' in lower_line or 'repair' in lower_line:
                    spring_2022_projects.append(line)

# Remove duplicates
unique_spring = list(set(spring_2022_projects))
print('Found', len(unique_spring), 'unique Spring 2022 project candidates')

# Match with funding database
matched_projects = {}
for project_name in unique_spring:
    # Direct match
    if project_name in funding_lookup:
        matched_projects[project_name] = funding_lookup[project_name]
    else:
        # Try partial matching
        for funded_name in funding_lookup:
            if (project_name.lower() in funded_name.lower() or 
                funded_name.lower() in project_name.lower()):
                matched_projects[funded_name] = funding_lookup[funded_name]
                break

# Final count and funding
project_count = len(matched_projects)
total_funding = sum(matched_projects.values())

print('Matched', project_count, 'projects with total funding', total_funding)

result = {
    'count': project_count,
    'total_funding': total_funding,
    'project_names': list(matched_projects.keys())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}}

exec(code, env_args)
