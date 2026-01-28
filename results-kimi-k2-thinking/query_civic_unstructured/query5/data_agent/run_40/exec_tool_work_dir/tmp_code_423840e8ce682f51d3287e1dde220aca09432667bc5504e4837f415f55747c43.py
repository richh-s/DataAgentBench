code = """import json

# Build funding lookup
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
total = 0
count = 0

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

for doc in civic_docs:
    txt = doc.get('text', '')
    lines = txt.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Check disaster indicators
        if '(FEMA Project)' in line or '(CalJPIA Project)' in line or '(CalOES Project)' in line or 'FEMA/CalOES Project' in line:
            # Look for 2022 start
            found = False
            for j in range(i, min(len(lines), i+6)):
                ctx = lines[j]
                if '2022' in ctx and ('st:' in ctx.lower() or 'start:' in ctx.lower()):
                    found = True
                    break
            
            if found:
                amount = funding_map.get(line, 0)
                if amount > 0:
                    total += amount
                    count += 1

result = {'total_funding': total, 'project_count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json'}

exec(code, env_args)
