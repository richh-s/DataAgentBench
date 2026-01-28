code = """import json
import re

# Load data
civic_docs = var_functions.query_db:22
funding = var_functions.query_db:5

# Handle file paths
if isinstance(civic_docs, str):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)
if isinstance(funding, str):
    with open(funding, 'r') as f:
        funding = json.load(f)

# Build funding map
funding_map = {rec['Project_Name'].strip().lower(): int(rec['Amount']) for rec in funding}

# Extract Spring 2022 projects
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    text_lower = text.lower()
    
    # Check for Spring 2022 mentions
    if any(indicator in text_lower for indicator in ['2022-spring', '2022-march', '2022-april', '2022-may']):
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line_lower = line.lower()
            
            if any(indicator in line_lower for indicator in ['2022-spring', '2022-march', '2022-april', '2022-may']):
                project_name = None
                
                # Look for project name before date line
                for j in range(i-1, max(i-5, -1), -1):
                    prev = lines[j].strip().replace('●', '').replace('■', '')
                    
                    # Filter out non-project lines
                    bad_terms = ['project schedule', 'updates:', 'complete design', 'advertise:', 'begin construction:']
                    if (len(prev) > 10 and prev[0].isupper() and 
                        not any(term in prev.lower() for term in bad_terms) and
                        not prev.startswith('(')):
                        project_name = prev
                        break
                
                if project_name and len(project_name) < 150:
                    key = project_name.lower()
                    amount = funding_map.get(key, 0)
                    
                    if amount == 0:
                        for funded_key, funded_amount in funding_map.items():
                            if funded_key in key or key in funded_key:
                                amount = funded_amount
                                break
                    
                    spring_projects.append({'name': project_name, 'funding': amount})

# Remove duplicates
unique = {}
for p in spring_projects:
    name = p['name']
    if name not in unique or p['funding'] > unique[name]['funding']:
        unique[name] = p

projects = list(unique.values())
count = len(projects)
total_funding = sum(p['funding'] for p in projects)

print('Spring 2022 Projects:', count)
print('Total Funding: $', total_funding)

result = {'project_count': count, 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
