code = """import json
import re

civic_docs_data = var_functions.query_db:10
funding_data = var_functions.query_db:7

# Read civic docs
if isinstance(civic_docs_data, str) and civic_docs_data.endswith('.json'):
    with open(civic_docs_data, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_data

# Read funding data  
if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_data

# Build funding map
funding_map = {}
for rec in funding_records:
    name = rec.get('Project_Name', '')
    amount = int(rec.get('Amount', 0))
    funding_map[name] = amount

# Find Spring 2022 projects
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check for Spring 2022 indicators
    spring_indicators = ['2022-Spring', 'Spring 2022', '2022-March', '2022-April', '2022-May',
                        'March 2022', 'April 2022', 'May 2022']
    
    if any(indicator in text for indicator in spring_indicators):
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Look for project names (lines that start with capital letters and contain keywords)
            if re.match(r'^[A-Z]', line) and any(keyword in line for keyword in 
                ['Project', 'Improvements', 'Repairs', 'Drainage', 'Resurfacing', 'Structure']):
                if len(line) > 10 and not line.startswith('('):
                    spring_projects.append(line)

# Remove duplicates
spring_projects = list(set(spring_projects))

# Match projects with funding data
matched_projects = []
for project in spring_projects:
    if project in funding_map:
        matched_projects.append({'name': project, 'funding': funding_map[project]})
    else:
        # Try to find partial matches
        for funded_name, amount in funding_map.items():
            if project.lower() in funded_name.lower() or funded_name.lower() in project.lower():
                matched_projects.append({'name': project, 'funding': amount})
                break

# Remove duplicates and sum funding
unique_projects = []
seen_names = set()
total_funding = 0

for project in matched_projects:
    if project['name'] not in seen_names:
        unique_projects.append(project)
        seen_names.add(project['name'])
        total_funding += project['funding']

result = {'num_projects': len(unique_projects), 'total_funding': total_funding, 'projects': unique_projects}
print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
