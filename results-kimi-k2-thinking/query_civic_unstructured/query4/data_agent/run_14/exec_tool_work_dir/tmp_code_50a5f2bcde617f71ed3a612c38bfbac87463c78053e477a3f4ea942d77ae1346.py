code = """import json
import os

# Get data from storage
civic_docs_data = locals().get('var_functions.query_db:2')
funding_data = locals().get('var_functions.query_db:5')

# Handle if data is file path
if isinstance(civic_docs_data, str) and civic_docs_data.endswith('.json'):
    with open(civic_docs_data, 'r') as f:
        civic_docs_data = json.load(f)

if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

print('Data loaded successfully')

# Build funding lookup map
funding_lookup = {}
for record in funding_data:
    key = record['Project_Name'].strip().lower()
    funding_lookup[key] = int(record['Amount'])

print(f'Funding map has {len(funding_lookup)} entries')

spring_2022_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    if not text:
        continue
        
    text_lower = text.lower()
    
    # Check for Spring 2022 dates
    if ('2022-spring' in text_lower or '2022-march' in text_lower or 
        '2022-april' in text_lower or '2022-may' in text_lower):
        
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line_lower = line.lower()
            if ('2022-spring' in line_lower or '2022-march' in line_lower or 
                '2022-april' in line_lower or '2022-may' in line_lower):
                
                # Look backwards for project name
                project_name = None
                for j in range(i-1, max(i-4, -1), -1):
                    prev = lines[j].strip()
                    clean = prev.replace('●', '').replace('■', '').strip()
                    
                    if (clean and len(clean) > 8 and 
                        'project schedule' not in clean.lower() and
                        'updates:' not in clean.lower() and
                        not clean.startswith('(')):
                        project_name = clean
                        break
                
                if project_name and len(project_name) < 200:
                    # Get funding amount
                    amount = 0
                    key = project_name.lower()
                    
                    if key in funding_lookup:
                        amount = funding_lookup[key]
                    else:
                        # Try partial match
                        for funded_key, funded_amount in funding_lookup.items():
                            if funded_key in key or key in funded_key:
                                amount = funded_amount
                                break
                    
                    spring_2022_projects.append({'name': project_name, 'funding': amount})

print(f'Found {len(spring_2022_projects)} project mentions')

# Remove duplicates
unique = {}
for p in spring_2022_projects:
    name = p['name']
    if name not in unique or p['funding'] > 0:
        unique[name] = p

projects = list(unique.values())
count = len(projects)
total_funding = sum(p['funding'] for p in projects)

print(f'Final: {count} projects, ${total_funding} total funding')

result = {'project_count': count, 'total_funding': total_funding}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
