code = """import json
import re

civic_docs_path = '/tmp/tmp2d2u8k1a.json'
funding_path = '/tmp/tmp0k5s9q8h.json'

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print('Loaded files')
print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_data))

# Create funding lookup
funding_lookup = {}
for record in funding_data:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_lookup[project_name] = amount

# Find disaster projects that started in 2022
total_funding = 0
found_projects = []

# Look for patterns in the text
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check if line is a project name (disaster projects have specific suffixes)
        if ('(FEMA Project)' in line or 
            '(CalJPIA Project)' in line or 
            '(CalOES Project)' in line or
            'FEMA/CalOES Project' in line):
            
            project_name = line
            # Look for start date in following lines (up to 5 lines ahead)
            start_date = ''
            for j in range(i+1, min(i+6, len(lines))):
                next_line = lines[j].strip()
                if 'st:' in next_line.lower() or 'start:' in next_line.lower():
                    start_date = next_line
                    break
            
            # Check if project started in 2022
            if '2022' in start_date:
                amount = funding_lookup.get(project_name, 0)
                if amount > 0:
                    total_funding += amount
                    found_projects.append({
                        'name': project_name,
                        'amount': amount,
                        'start': start_date
                    })

print('\nFound projects:', len(found_projects))
print('Total funding:', total_funding)

for p in found_projects:
    print('  ' + p['name'] + ': $' + str(p['amount']))

result = {
    'total_funding': total_funding,
    'project_count': len(found_projects),
    'projects': found_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
