code = """import json
import re

# Read all civic documents
with open(locals()['var_functions.query_db:42'], 'r') as f:
    civic_docs = json.load(f)

# Read all funding data  
with open(locals()['var_functions.query_db:36'], 'r') as f:
    funding_data = json.load(f)

print('Documents:', len(civic_docs))
print('Funding records:', len(funding_data))

# Create funding lookup (lowercase names)
funding_map = {}
for item in funding_data:
    name = item['Project_Name'].lower().strip()
    funding_map[name] = int(item['Amount'])

# Find Spring 2022 projects (March, April, May, or "Spring" with 2022)
spring_projects = set()  # Use set to avoid duplicates

for doc in civic_docs:
    text = doc.get('text', '').lower()
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip metadata lines
        if not line or line.startswith('(') or line.startswith('cid:') or line.startswith('_'):
            continue
            
        # Look for construction start indicators with 2022
        if 'begin construction' in line and '2022' in line:
            # Check if it's Spring timeframe
            if 'spring' in line or 'march' in line or 'april' in line or 'may' in line:
                # Find project name (look backwards)
                for j in range(i-1, max(0, i-15), -1):
                    prev = lines[j].strip()
                    if (prev and not prev.startswith('(') and 
                        'cid:' not in prev and '_' not in prev and
                        'capital improvement' not in prev.lower() and
                        'design' not in prev.lower() and
                        len(prev) < 100):
                        spring_projects.add(prev)
                        break

print('Spring 2022 projects:', len(spring_projects))
print('Project names:', list(spring_projects))

# Match with funding
matches = []
total_funds = 0
seen = set()

for proj in spring_projects:
    proj_key = proj.lower()
    if proj_key in funding_map and proj_key not in seen:
        amount = funding_map[proj_key]
        matches.append({'name': proj, 'funding': amount})
        total_funds += amount
        seen.add(proj_key)

print('Matched projects:', len(matches))
print('Total funding:', total_funds)

result = {'count': len(matches), 'total': total_funds, 'projects': matches}
print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json'}

exec(code, env_args)
