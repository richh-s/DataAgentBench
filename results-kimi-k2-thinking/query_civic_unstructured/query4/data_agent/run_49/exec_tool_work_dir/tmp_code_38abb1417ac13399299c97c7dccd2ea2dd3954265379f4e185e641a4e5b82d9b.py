code = """import json
import re

# Load data from files
civic_docs_file = var_functions.query_db:10
funding_file = var_functions.query_db:7

if isinstance(civic_docs_file, str) and '.json' in civic_docs_file:
    with open(civic_docs_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_file

if isinstance(funding_file, str) and '.json' in funding_file:
    with open(funding_file, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_file

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
    
    # Look for Spring 2022 date patterns
    spring_patterns = ['2022-Spring', 'Spring 2022', '2022-March', 'March 2022', 
                       '2022-April', 'April 2022', '2022-May', 'May 2022']
    
    has_spring = any(p in text for p in spring_patterns)
    
    if has_spring:
        # Find project names (lines that look like project titles)
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Project titles are usually uppercase or title case and contain keywords
            if any(keyword in line for keyword in ['Project', 'Improvements', 'Repairs', 
                                                  'Drainage', 'Resurfacing', 'Structure']):
                if len(line) > 15 and not line.startswith('(') and not line.startswith('cid:'):
                    spring_projects.append(line)

# Remove duplicates
spring_projects = list(set(spring_projects))

# Match with funding
matches = []
total = 0

for project in spring_projects:
    if project in funding_map:
        amount = funding_map[project]
        matches.append({'name': project, 'funding': amount})
        total += amount
    else:
        # Try variations
        for funded_name, amount in funding_map.items():
            # Check if the core project name matches
            clean_project = project.replace('Project', '').strip()
            clean_funded = funded_name.replace('Project', '').strip()
            
            if clean_project in clean_funded or clean_funded in clean_project:
                if amount > 0:
                    matches.append({'name': project, 'funding': amount})
                    total += amount
                break

# Remove duplicate matches
unique_matches = []
seen = set()
for m in matches:
    if m['name'] not in seen:
        unique_matches.append(m)
        seen.add(m['name'])

result = {
    'num_projects': len(unique_matches),
    'total_funding': total,
    'projects': unique_matches
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
