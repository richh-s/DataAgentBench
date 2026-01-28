code = """import json

# Load data files
with open('/tmp/tmp2d2u8k1a.json', 'r') as f:
    civic_docs = json.load(f)

with open('/tmp/tmp0k5s9q8h.json', 'r') as f:
    funding_data = json.load(f)

# Build funding map
funding_map = {}
for record in funding_data:
    name = record.get('Project_Name', '')
    if name:
        funding_map[name] = int(record.get('Amount', 0))

# Find disaster projects starting in 2022
total = 0
disaster_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Check for disaster project indicators
        has_fema = '(FEMA Project)' in line
        has_caljpia = '(CalJPIA Project)' in line
        has_calo = '(CalOES Project)' in line
        has_fema_calo = 'FEMA/CalOES Project' in line
        
        is_disaster = has_fema or has_caljpia or has_calo or has_fema_calo
        
        if is_disaster:
            proj_name = line
            
            # Search for start date in next lines
            start_line = ''
            for j in range(i+1, min(i+5, len(lines))):
                next_line = lines[j].strip()
                if 'st:' in next_line.lower() or 'start;' in next_line.lower() or 'start:' in next_line.lower():
                    start_line = next_line
                    break
            
            # Check for 2022 start
            if '2022' in start_line:
                amount = funding_map.get(proj_name, 0)
                if amount > 0:
                    total += amount
                    disaster_projects.append({
                        'name': proj_name,
                        'amount': amount,
                        'details': start_line
                    })

# Output
print('__RESULT__:')
print(json.dumps({
    'total_funding': total,
    'count': len(disaster_projects),
    'projects': disaster_projects
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
