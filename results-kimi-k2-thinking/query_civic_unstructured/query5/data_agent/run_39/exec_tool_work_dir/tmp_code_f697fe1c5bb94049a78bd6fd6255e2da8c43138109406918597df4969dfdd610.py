code = """import json
import re

# Get the file paths from storage
funding_path = globals()['var_functions.query_db:2']
civic_path = globals()['var_functions.query_db:6']

print('Loading funding data...')
with open(funding_path, 'r') as f:
    funding = json.load(f)

print('Loading civic docs...')
with open(civic_path, 'r') as f:
    civic = json.load(f)

print(f'Loaded {len(funding)} funding records, {len(civic)} civic docs')

# Find disaster projects in funding data
disaster_projs = []
for rec in funding:
    name = rec.get('Project_Name', '')
    if any(x in name for x in ['(FEMA', '(CalOES', '(CalJPIA', 'FEMA', 'Fire', 'Emergency']):
        disaster_projs.append({
            'name': name,
            'amt': int(rec.get('Amount', 0)),
            'src': rec.get('Funding_Source')
        })

# Combine civic document text
all_text = '\n'.join([doc.get('text', '') for doc in civic])

# Find projects with 2022 references
proj_2022 = []
for proj in disaster_projs:
    name = proj['name']
    base = name.split('(')[0].strip()
    
    # Check for 2022 reference in context
    for search_name in [name, base]:
        if search_name in all_text:
            idx = all_text.find(search_name)
            context = all_text[max(0, idx-200):min(len(all_text), idx+200)]
            
            if '2022' in context:
                lower = context.lower()
                if any(x in lower for x in ['completed', 'completion', 'start', 'begin', 'construction']):
                    proj_2022.append(proj)
                    break

# Remove duplicates
unique = []
seen = set()
for p in proj_2022:
    if p['name'] not in seen:
        unique.append(p)
        seen.add(p['name'])

# Calculate total
total = sum(p['amt'] for p in unique)

result = {'total_funding': total, 'count': len(unique), 'projects': unique}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'test': True, 'funding_count': 0, 'civic_count': 0}}

exec(code, env_args)
