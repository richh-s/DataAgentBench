code = """import json, os

# Debug: Check what files exist
print('Files in /tmp:')
for f in os.listdir('/tmp'):
    if f.endswith('.json'):
        print('  ', f)

# Get actual paths
civic_path = None
funding_path = None

for f in os.listdir('/tmp'):
    if 'civic' in f.lower() or 'agenda' in f.lower():
        civic_path = os.path.join('/tmp', f)
    elif 'funding' in f.lower():
        funding_path = os.path.join('/tmp', f)

print('\nCivic path:', civic_path)
print('Funding path:', funding_path)

# Load data
if civic_path and funding_path:
    with open(civic_path) as f:
        civic_docs = json.load(f)
    with open(funding_path) as f:
        funding_data = json.load(f)
    
    print('\nLoaded', len(civic_docs), 'civic docs')
    print('Loaded', len(funding_data), 'funding records')
    
    # Build funding map
    funding_map = {}
    for rec in funding_data:
        name = rec.get('Project_Name', '')
        if name:
            funding_map[name] = int(rec.get('Amount', 0))
    
    # Search for disaster projects starting 2022
    total = 0
    projects = []
    
    for doc in civic_docs:
        txt = doc.get('text', '')
        lines = txt.split('\n')
        
        for i in range(len(lines)):
            line = lines[i].strip()
            if not line:
                continue
            
            # Check disaster markers
            markers = ['(FEMA Project)', '(CalJPIA Project)', '(CalOES Project)', 'FEMA/CalOES Project']
            is_disaster = any(m in line for m in markers)
            
            if is_disaster:
                # Look for 2022 start
                has_2022 = False
                for j in range(max(0,i-2), min(len(lines), i+6)):
                    context = lines[j]
                    if '2022' in context and ('st:' in context.lower() or 'start:' in context.lower()):
                        has_2022 = True
                        break
                
                if has_2022:
                    amt = funding_map.get(line, 0)
                    if amt:
                        total += amt
                        projects.append({'name': line, 'amount': amt})
    
    result = {'total_funding': total, 'project_count': len(projects)}
    print('__RESULT__:')
    print(json.dumps(result))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'Files not found'}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
