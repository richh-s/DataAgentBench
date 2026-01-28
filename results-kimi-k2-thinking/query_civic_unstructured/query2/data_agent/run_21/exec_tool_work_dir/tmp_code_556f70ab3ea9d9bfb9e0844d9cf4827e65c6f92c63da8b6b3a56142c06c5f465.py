code = """import json

# Load funding data
funding_path = locals()['var_functions.query_db:10']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic docs data  
civic_path = locals()['var_functions.query_db:11']
with open(civic_path, 'r') as f:
    civic_data = json.load(f)

print('Loaded funding records:', len(funding_data))
print('Loaded civic docs:', len(civic_data))

# First, let's look for park projects in funding data
park_funding = []
for item in funding_data:
    if 'park' in item['Project_Name'].lower():
        park_funding.append(item)

print('\nPark-related funding records:', len(park_funding))
print('Sample:', [p['Project_Name'] for p in park_funding[:10]])

# Now find park projects completed in 2022 from civic docs
completed_2022_parks = []

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line_lower = line.lower()
        
        # Check if this line mentions park
        if 'park' in line_lower:
            # Check nearby lines for 2022 completion
            for j in range(max(0, i-2), min(len(lines), i+5)):
                check_line = lines[j].lower()
                
                # Look for 2022 completion indicators
                if '2022' in check_line and ('completed' in check_line or 'completion' in check_line):
                    # Extract project name (usually the line with 'Park' in it)
                    project_name = line.strip()
                    if len(project_name) > 5 and not project_name.startswith('('):
                        completed_2022_parks.append({
                            'name': project_name,
                            'status': lines[j].strip(),
                            'matched_amount': None
                        })
                        break

print('\nPark projects completed in 2022 found:', len(completed_2022_parks))
for p in completed_2022_parks[:10]:
    print('  -', p['name'])
    print('    Status:', p['status'])
    print()"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
