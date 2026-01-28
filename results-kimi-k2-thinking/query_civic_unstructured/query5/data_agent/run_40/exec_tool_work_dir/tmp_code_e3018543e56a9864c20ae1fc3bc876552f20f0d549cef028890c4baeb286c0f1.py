code = """import json

# Build funding lookup from stored path
funding_path = locals()['var_functions.query_db:67']
funding_map = {}

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
    
for rec in funding_data:
    name = rec.get('Project_Name')
    amount = rec.get('Amount')
    if name and amount:
        funding_map[name] = int(amount)

# Process civic documents
civic_path = locals()['var_functions.query_db:66']
total_funding = 0
project_count = 0

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)
    
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Check if disaster project
        is_disaster = '(FEMA Project)' in line or '(CalJPIA Project)' in line or '(CalOES Project)' in line or 'FEMA/CalOES Project' in line
        
        if is_disaster:
            # Look for 2022 start date in nearby lines
            found_2022 = False
            for j in range(i, min(i+6, len(lines))):
                ctx = lines[j]
                if '2022' in ctx and ('st:' in ctx.lower() or 'start:' in ctx.lower()):
                    found_2022 = True
                    break
            
            if found_2022:
                amount = funding_map.get(line, 0)
                if amount > 0:
                    total_funding += amount
                    project_count += 1

result = {'total_funding': total_funding, 'project_count': project_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json'}

exec(code, env_args)
