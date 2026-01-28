code = """import json

# Load the data files
civic_docs = json.load(open(locals()['var_functions.query_db:66'], 'r'))
funding_records = json.load(open(locals()['var_functions.query_db:67'], 'r'))

# Build funding lookup
funding_lookup = {}
for rec in funding_records:
    if 'Project_Name' in rec and 'Amount' in rec:
        funding_lookup[rec['Project_Name']] = int(rec['Amount'])

# Process documents
total = 0
count = 0

for doc in civic_docs:
    txt = doc.get('text', '')
    lines = txt.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Check disaster markers
        disaster = False
        if '(FEMA' in line:
            disaster = True
        elif 'CalJPIA' in line:
            disaster = True
        elif 'CalOES' in line:
            disaster = True
            
        if disaster:
            # Look for 2022 in context
            for j in range(i, min(i+6, len(lines))):
                ctx = lines[j]
                if '2022' in ctx:
                    lower = ctx.lower()
                    if 'st:' in lower or 'start:' in lower:
                        amt = funding_lookup.get(line, 0)
                        if amt > 0:
                            total = total + amt
                            count = count + 1
                        break

result = {'total_funding': total, 'project_count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json'}

exec(code, env_args)
