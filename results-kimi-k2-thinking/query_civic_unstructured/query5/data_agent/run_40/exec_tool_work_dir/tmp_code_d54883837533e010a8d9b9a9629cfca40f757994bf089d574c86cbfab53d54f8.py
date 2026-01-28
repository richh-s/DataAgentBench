code = """import json

civic_docs_path = '/tmp/tmp2d2u8k1a.json'
funding_path = '/tmp/tmp0k5s9q8h.json'

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Build funding lookup dictionary
funding_lookup = {}
for rec in funding_data:
    name = rec.get('Project_Name', '')
    if name:
        funding_lookup[name] = int(rec.get('Amount', 0))

print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_data))
print('Funding lookup has', len(funding_lookup), 'entries')

# Initialize counters
total_funding = 0
disaster_projects = []

# Process documents
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Skip empty lines
        if len(line) < 5:
            continue
            
        # Look for disaster indicators
        if '(FEMA Project)' in line or '(CalJPIA Project)' in line or '(CalOES Project)' in line or 'FEMA/CalOES Project' in line:
            project_name = line
            
            # Look for start date
            start_date_found = ''
            for j in range(min(i+1, len(lines)), min(i+6, len(lines))):
                next_line = lines[j].strip().lower()
                if 'st:' in next_line or 'start:' in next_line:
                    start_date_found = lines[j].strip()
                    break
            
            # Check if started in 2022
            if '2022' in start_date_found:
                amount = funding_lookup.get(project_name, 0)
                if amount > 0:
                    total_funding += amount
                    disaster_projects.append({
                        'name': project_name,
                        'amount': amount,
                        'start': start_date_found
                    })

# Output result
result = {
    'total_funding': total_funding,
    'project_count': len(disaster_projects),
    'projects': disaster_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
