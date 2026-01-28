code = """import json
import re

# Load civic documents
civic_file = locals()['var_functions.query_db:4']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Find Spring 2022 projects
spring_2022_projects = []

# Patterns to match Spring 2022
spring_patterns = [
    'Spring 2022',
    '2022-Spring',
    'March 2022',
    'April 2022',
    'May 2022',
    '2022-March',
    '2022-April',
    '2022-May'
]

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    has_spring_2022 = any(pattern.lower() in lower_text for pattern in spring_patterns)
    
    if has_spring_2022:
        sections = text.split('\n\n')
        for section in sections:
            lower_section = section.lower()
            if any(pattern.lower() in lower_section for pattern in spring_patterns):
                lines = section.split('\n')
                for line in lines:
                    line = line.strip()
                    if line and line[0].isupper():
                        words = line.split()
                        if 3 <= len(words) <= 15:
                            spring_2022_projects.append(line)

unique_projects = list(set(spring_2022_projects))

print('Potential Spring 2022 projects found in text:')
for proj in unique_projects:
    print('  - ' + proj)

# Now look for project names with funding
funding_file = locals()['var_functions.query_db:8']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

funding_lookup = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    if project_name not in funding_lookup:
        funding_lookup[project_name] = 0
    funding_lookup[project_name] += amount

print('\nMatching with funding database...')
matched_projects = []
total_funding = 0

for project in unique_projects:
    # Direct match
    if project in funding_lookup:
        matched_projects.append({
            'name': project,
            'funding': funding_lookup[project]
        })
        total_funding += funding_lookup[project]
    else:
        # Fuzzy matching
        for funded_project in funding_lookup:
            if project.lower() in funded_project.lower() or funded_project.lower() in project.lower():
                matched_projects.append({
                    'name': funded_project,
                    'funding': funding_lookup[funded_project]
                })
                total_funding += funding_lookup[funded_project]
                break

unique_matched = {}
for proj in matched_projects:
    unique_matched[proj['name']] = proj['funding']

print('\nMatched projects with funding:')
for name, funding in unique_matched.items():
    print('  - ' + name + ': $' + str(funding))

print('\n__RESULT__:')
result = {
    'spring_2022_projects': len(unique_matched),
    'total_funding': total_funding,
    'projects': list(unique_matched.keys())
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}}

exec(code, env_args)
