code = """import json
import re

# Read the data files
civic_docs_path = 'var_functions.query_db:8'
funding_path = 'var_functions.query_db:5'

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print('Loaded %d civic documents' % len(civic_docs))
print('Loaded %d funding records' % len(funding_data))

# Build funding map
funding_map = {}
for record in funding_data:
    name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_map[name] = amount

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
            
        # Check if park-related
        has_park = 'park' in line.lower() or 'playground' in line.lower()
        
        # Check if looks like project name (not heading)
        is_valid = len(line) > 10
        is_not_heading = not any(h in line.lower() for h in ['capital improvement', 'disaster recovery', 'prepared by', 'approved by', 'recommended action', 'discussion:', 'subject:', 'public works', 'commission', 'agenda', 'page'])
        
        if has_park and is_valid and is_not_heading:
            # Look for completion in 2022 in context
            context_start = max(0, i-10)
            context_end = min(len(lines), i+10)
            context = ' '.join(lines[context_start:context_end]).lower()
            
            if 'completed' in context and '2022' in context:
                # Clean name
                clean_name = line.replace('(cid:190)', '').replace('(cid:131)', '').strip()
                
                # Find matching funding
                funding_amount = 0
                for funded_name in funding_map:
                    if (clean_name.lower() in funded_name.lower() or 
                        funded_name.lower() in clean_name.lower()):
                        funding_amount = funding_map[funded_name]
                        break
                
                park_projects.append({
                    'name': clean_name,
                    'funding': funding_amount
                })

# Remove duplicates
unique_projects = []
seen = set()
for proj in park_projects:
    if proj['name'] not in seen:
        unique_projects.append(proj)
        seen.add(proj['name'])

# Calculate total funding
total_funding = sum(p['funding'] for p in unique_projects)
project_count = len([p for p in unique_projects if p['funding'] > 0])

print('\nFound %d unique park projects completed in 2022' % len(unique_projects))
print('Projects with funding:')
for proj in unique_projects:
    if proj['funding'] > 0:
        print('- %s: $%d' % (proj['name'], proj['funding']))

print('\nTotal funding: $%d' % total_funding)

# Return result
result = {
    'total_funding': total_funding,
    'project_count': project_count
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
