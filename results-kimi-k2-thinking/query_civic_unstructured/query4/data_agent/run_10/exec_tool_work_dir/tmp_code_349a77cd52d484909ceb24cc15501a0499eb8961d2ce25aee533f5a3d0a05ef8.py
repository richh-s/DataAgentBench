code = """import json

# Load the data from files
civic_docs = json.load(open('/tmp/tmp1i3q6xjc.json'))
funding_data = json.load(open('/tmp/tmp6v8h4l_u.json'))

print("Loaded {} civic documents and {} funding records".format(len(civic_docs), len(funding_data)))

# Build funding lookup (aggregate amounts for same project)
funding_lookup = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    if project_name in funding_lookup:
        funding_lookup[project_name] += amount
    else:
        funding_lookup[project_name] = amount

print("Funding lookup contains {} unique projects".format(len(funding_lookup)))

# Find Spring 2022 projects
spring_2022_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check for Spring 2022 references
    if 'Spring 2022' in text or '2022-Spring' in text:
        # Split text into lines to find project names
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Look for lines that might be project names
            if line and len(line) > 10 and line[0].isupper():
                # Heuristic: project names contain these keywords or are capitalized titles
                lowercase_line = line.lower()
                if ('project' in lowercase_line or 
                    'improvement' in lowercase_line or 
                    'repair' in lowercase_line or
                    'replacement' in lowercase_line or
                    'renovation' in lowercase_line):
                    spring_2022_projects.add(line)

print("Found {} potential Spring 2022 projects in text".format(len(spring_2022_projects)))

# Match with funding data
matched_projects = {}
for project in spring_2022_projects:
    # Direct match
    if project in funding_lookup:
        matched_projects[project] = funding_lookup[project]
    else:
        # Try partial/fuzzy matching
        project_lower = project.lower()
        for funded_name in funding_lookup:
            funded_lower = funded_name.lower()
            # Check if one is contained in the other
            if (project_lower in funded_lower or funded_lower in project_lower):
                matched_projects[funded_name] = funding_lookup[funded_name]
                break

# Final results
project_count = len(matched_projects)
total_funding = sum(matched_projects.values())

print("Final results:")
print("Projects:", project_count)
print("Total funding:", total_funding)
print("Project names:", list(matched_projects.keys()))

result = {
    'count': project_count,
    'total_funding': total_funding,
    'projects': list(matched_projects.keys())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500}

exec(code, env_args)
