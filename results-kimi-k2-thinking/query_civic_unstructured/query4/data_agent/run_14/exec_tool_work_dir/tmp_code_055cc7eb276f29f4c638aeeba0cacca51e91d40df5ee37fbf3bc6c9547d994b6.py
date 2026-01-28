code = """import json
import os

# Load civic documents data
civic_docs_key = 'var_functions.query_db:2'
civic_docs_data = locals().get(civic_docs_key)
if isinstance(civic_docs_data, str) and civic_docs_data.endswith('.json'):
    with open(civic_docs_data, 'r') as f:
        civic_docs_data = json.load(f)

# Load funding data  
funding_key = 'var_functions.query_db:5'
funding_data = locals().get(funding_key)
if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

print(f'Loaded {len(civic_docs_data)} documents and {len(funding_data)} funding records')

# Build funding lookup
funding_lookup = {}
for record in funding_data:
    name = record['Project_Name'].strip().lower()
    funding_lookup[name] = int(record['Amount'])

spring_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Check for Spring 2022 indicators
    if '2022-spring' in lower_text or '2022-march' in lower_text or '2022-april' in lower_text or '2022-may' in lower_text:
        lines = text.split('\n')
        for idx, line in enumerate(lines):
            lower_line = line.lower()
            if '2022-spring' in lower_line or '2022-march' in lower_line or '2022-april' in lower_line or '2022-may' in lower_line:
                # Look backwards for project name
                project_name = None
                for j in range(idx-1, max(idx-3, -1), -1):
                    prev = lines[j].strip().replace('●', '').replace('■', '').strip()
                    if prev and len(prev) > 8 and 'project schedule' not in prev.lower() and not prev.startswith('('):
                        project_name = prev
                        break
                
                if project_name:
                    # Get funding
                    amount = 0
                    key = project_name.lower()
                    if key in funding_lookup:
                        amount = funding_lookup[key]
                    else:
                        # Try partial matches
                        for funded_key, funded_amount in funding_lookup.items():
                            if funded_key in key or key in funded_key:
                                amount = funded_amount
                                break
                    
                    spring_projects.append({'name': project_name, 'funding': amount})

# Deduplicate
unique = {}
for p in spring_projects:
    name = p['name']
    if name not in unique or p['funding'] > 0:
        unique[name] = p

projects = list(unique.values())
count = len(projects)
total_funding = sum(p['funding'] for p in projects)

print(f'Found {count} Spring 2022 projects with ${total_funding} total funding')

result = {
    'project_count': count,
    'total_funding': total_funding,
    'projects': projects[:10]
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
