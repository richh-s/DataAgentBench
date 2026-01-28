code = """import json

# Get data
civic_docs_key = 'var_functions.query_db:22'
funding_key = 'var_functions.query_db:28'

civic_docs_data = locals().get(civic_docs_key)
funding_data = locals().get(funding_key)

# Handle file paths
if isinstance(civic_docs_data, str):
    with open(civic_docs_data, 'r') as f:
        civic_docs_data = json.load(f)

if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Build funding lookup
funding_map = {}
for record in funding_data:
    funding_map[record['Project_Name'].strip().lower()] = int(record['Amount'])

print('Funding map size:', len(funding_map))

# Track Spring 2022 projects
spring_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    text_lower = text.lower()
    
    # Check for Spring 2022 indicators
    if any(indicator in text_lower for indicator in ['2022-spring', '2022-march', '2022-april', '2022-may']):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line_lower = line.lower()
            if any(indicator in line_lower for indicator in ['2022-spring', '2022-march', '2022-april', '2022-may']):
                project_name = None
                for j in range(i-1, max(i-5, -1), -1):
                    prev = lines[j].strip().replace('●', '').replace('■', '').strip()
                    
                    # Simple heuristics for project names
                    if (prev and len(prev) > 10 and prev[0].isupper() and 
                        'project schedule' not in prev.lower() and 'updates:' not in prev.lower() and
                        not prev.startswith('(') and len(prev) < 150):
                        project_name = prev
                        break
                
                if project_name:
                    key = project_name.lower()
                    funding_amount = funding_map.get(key, 0)
                    
                    if funding_amount == 0:
                        for funded_key, amount in funding_map.items():
                            if funded_key in key or key in funded_key:
                                funding_amount = amount
                                break
                    
                    spring_projects.append({'name': project_name, 'funding': funding_amount, 'doc': doc.get('filename', '')})

print('Total mentions found:', len(spring_projects))

# Deduplicate
unique = {}
for p in spring_projects:
    name = p['name']
    if name not in unique or p['funding'] > unique[name]['funding']:
        unique[name] = p

projects = list(unique.values())
count = len(projects)
total_funding = sum(p['funding'] for p in projects)

print('Final count:', count, 'Total funding:', total_funding)

result = {'project_count': count, 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
