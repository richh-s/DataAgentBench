code = """import json

funding_path = var_functions.query_db_67
civic_path = var_functions.query_db_66

funding_lookup = {}
with open(funding_path, 'r') as f:
    data = json.load(f)
    for item in data:
        name = item.get('Project_Name', '')
        if name:
            funding_lookup[name] = int(item.get('Amount', 0))

total_funding = 0
project_count = 0

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)
    
for doc in civic_docs:
    txt = doc.get('text', '')
    lines = txt.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if '(FEMA Project)' in line or '(CalJPIA Project)' in line or '(CalOES Project)' in line or 'FEMA/CalOES Project' in line:
            for j in range(i, min(i+6, len(lines))):
                ctx = lines[j]
                if '2022' in ctx and ('st:' in ctx.lower() or 'start:' in ctx.lower()):
                    amount = funding_lookup.get(line, 0)
                    if amount > 0:
                        total_funding += amount
                        project_count += 1
                    break

output = {'total_funding': total_funding, 'project_count': project_count}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json'}

exec(code, env_args)
