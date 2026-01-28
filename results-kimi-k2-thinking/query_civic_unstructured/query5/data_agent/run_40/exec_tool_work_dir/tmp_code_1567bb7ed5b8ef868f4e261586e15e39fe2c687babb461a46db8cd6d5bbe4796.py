code = """import json

# Get the stored data paths
civic_docs_path = '/tmp/tmprp5f5z5k.json'
funding_path = '/tmp/tmp0k5s9q8h.json'

# Load the data
with open(civic_docs_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding_data = json.load(f)

# Build lookup: project name -> funding amount
funding_lookup = {}
for rec in funding_data:
    name = rec.get('Project_Name', '')
    if name:
        funding_lookup[name] = int(rec.get('Amount', 0))

# Find disaster projects with 2022 start date
total_funding = 0
found_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Check if this is a disaster project
        is_disaster = False
        if '(FEMA Project)' in line:
            is_disaster = True
        elif '(CalJPIA Project)' in line:
            is_disaster = True
        elif '(CalOES Project)' in line:
            is_disaster = True
        elif 'FEMA/CalOES Project' in line:
            is_disaster = True
        
        if is_disaster:
            project_name = line
            
            # Look for 2022 start date in nearby lines
            found_2022 = False
            for j in range(max(0, i-2), min(len(lines), i+6)):
                nearby_line = lines[j]
                if '2022' in nearby_line and ('st:' in nearby_line.lower() or 'start:' in nearby_line.lower()):
                    found_2022 = True
                    break
            
            if found_2022:
                amount = funding_lookup.get(project_name, 0)
                if amount > 0:
                    total_funding += amount
                    found_projects.append({'name': project_name, 'funding': amount})

# Return final result
output = {
    'total_funding': total_funding,
    'project_count': len(found_projects)
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
