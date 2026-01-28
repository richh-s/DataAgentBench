code = """import json

# Load data from both sources
funding_file = locals()['var_functions.query_db:96']
civic_file = locals()['var_functions.query_db:92']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup: project name -> total funding
funding_lookup = {}
for record in funding_data:
    project_name = record['Project_Name']
    total_amount = int(record['Total_Amount'])
    funding_lookup[project_name] = total_amount

print('Funding lookup contains', len(funding_lookup), 'unique projects')
print('Civic documents to analyze:', len(civic_docs))

# Search for projects with start dates in Spring 2022
spring_2022_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Check for Spring 2022 references in the document
    if 'spring 2022' in lower_text or '2022-spring' in lower_text:
        # Split into lines and look for project names
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Heuristic: project names are capitalized, reasonable length, contain keywords
            if line and len(line) > 10 and line[0].isupper():
                low_line = line.lower()
                keywords = ['project', 'improvement', 'repair', 'renovation', 'construction']
                if any(k in low_line for k in keywords):
                    spring_2022_projects.add(line)

print('Found', len(spring_2022_projects), 'potential Spring 2022 projects')

# Match projects with funding records
matched_projects = {}
for project in spring_2022_projects:
    # Direct match first
    if project in funding_lookup:
        matched_projects[project] = funding_lookup[project]
    else:
        # Try partial matching: project name contained in funded name
        proj_lower = project.lower()
        for funded_name in funding_lookup:
            funded_lower = funded_name.lower()
            if proj_lower in funded_lower:
                matched_projects[funded_name] = funding_lookup[funded_name]
                break

# Results
project_count = len(matched_projects)
total_funding = sum(matched_projects.values())

print('Matched', project_count, 'projects')
print('Total funding:', total_funding)
print('Projects:', list(matched_projects.keys()))

result = {'count': project_count, 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.execute_python:84': {'spring_2022_docs': 4, 'funding_projects': 500}, 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json', 'var_functions.query_db:96': 'file_storage/functions.query_db:96.json', 'var_functions.execute_python:98': {'found_spring': True, 'matched_funding': 8868000}}

exec(code, env_args)
