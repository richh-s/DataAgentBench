code = """import json

# Load civic documents
civic_path = var_functions.query_db_58
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_path = var_functions.query_db_59
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Build funding lookup
funding_lookup = {}
for rec in funding_data:
    name = rec.get('Project_Name', '')
    if name:
        funding_lookup[name] = int(rec.get('Amount', 0))

# Process documents
total = 0
count = 0
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Check disaster markers
        markers = ['(FEMA Project)', '(CalJPIA Project)', '(CalOES Project)', 'FEMA/CalOES Project']
        is_disaster = any(m in line for m in markers)
        
        if is_disaster:
            # Look for 2022 start
            found_2022 = False
            for j in range(max(0,i-2), min(len(lines), i+6)):
                ctx = lines[j]
                if '2022' in ctx and ('st:' in ctx.lower() or 'start:' in ctx.lower()):
                    found_2022 = True
                    break
            
            if found_2022:
                amount = funding_lookup.get(line, 0)
                if amount > 0:
                    total += amount
                    count += 1
                    projects.append({'name': line, 'funding': amount})

result = {'total_funding': total, 'project_count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json'}

exec(code, env_args)
