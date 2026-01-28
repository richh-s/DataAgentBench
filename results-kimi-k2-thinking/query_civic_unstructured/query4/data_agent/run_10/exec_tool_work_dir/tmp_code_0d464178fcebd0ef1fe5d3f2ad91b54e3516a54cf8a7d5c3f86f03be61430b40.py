code = """import json

# Load data from both sources
funding_file = locals()['var_functions.query_db:96']
civic_file = locals()['var_functions.query_db:92']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup
funding_lookup = {}
for item in funding_data:
    project_name = item['Project_Name']
    amount = int(item['Total_Amount'])
    funding_lookup[project_name] = amount

print('Funding lookup built with', len(funding_lookup), 'projects')
print('Civic documents:', len(civic_docs))

# Look for actual Spring 2022 projects with start dates
spring_2022_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Check for Spring 2022 references
    if 'spring 2022' in lower_text or '2022-spring' in lower_text:
        print('Found Spring 2022 in:', doc.get('filename'))
        
        # Extract lines that might be project names
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Heuristic: project names are typically capitalized, reasonable length, and contain keywords
            if line and len(line) > 15 and line[0].isupper():
                low_line = line.lower()
                if any(kw in low_line for kw in ['project', 'improvement', 'repair', 'renovation']):
                    spring_2022_projects.add(line)

print('Potential Spring 2022 projects found:', len(spring_2022_projects))
for proj in list(spring_2022_projects)[:10]:
    print('  -', proj)

# Match with funding database
matched = {}
for project in spring_2022_projects:
    if project in funding_lookup:
        matched[project] = funding_lookup[project]
        print('Direct match:', project, '=', funding_lookup[project])
    else:
        # Try partial matching
        proj_lower = project.lower()
        for funded_name in funding_lookup:
            funded_lower = funded_name.lower()
            if proj_lower in funded_lower or funded_lower in proj_lower:
                matched[funded_name] = funding_lookup[funded_name]
                print('Partial match:', project, '->', funded_name, '=', funding_lookup[funded_name])
                break

result = {
    'spring_2022_project_count': len(matched),
    'total_funding': sum(matched.values())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.execute_python:84': {'spring_2022_docs': 4, 'funding_projects': 500}, 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json', 'var_functions.query_db:96': 'file_storage/functions.query_db:96.json', 'var_functions.execute_python:98': {'found_spring': True, 'matched_funding': 8868000}}

exec(code, env_args)
