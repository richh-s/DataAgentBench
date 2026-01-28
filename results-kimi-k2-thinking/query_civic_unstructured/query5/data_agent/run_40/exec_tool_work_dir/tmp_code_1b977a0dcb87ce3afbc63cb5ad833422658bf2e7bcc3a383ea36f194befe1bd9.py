code = """import json

# Create funding lookup
funding_lookup = {}
with open(var_functions.query_db_67, 'r') as f:
    for rec in json.load(f):
        name = rec.get('Project_Name','')
        if name:
            funding_lookup[name] = int(rec.get('Amount','0'))

# Process civic documents  
total = 0
count = 0

with open(var_functions.query_db_66, 'r') as f:
    for doc in json.load(f):
        txt = doc.get('text','')
        lines = txt.split('\n')
        
        for i,line in enumerate(lines):
            line = line.strip()
            if '(FEMA Project)' in line or '(CalJPIA Project)' in line or '(CalOES Project)' in line or 'FEMA/CalOES Project' in line:
                for j in range(i, min(i+6, len(lines))):
                    if '2022' in lines[j] and ('st:' in lines[j].lower() or 'start:' in lines[j].lower()):
                        amount = funding_lookup.get(line,0)
                        if amount>0:
                            total += amount
                            count += 1
                        break

result = {'total_funding':total, 'project_count':count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json'}

exec(code, env_args)
