code = """import json

# Load funding data
f = open('/tmp/tmpck2j5x7i.json', 'r')
funding_records = json.load(f)
f.close()

# Build funding lookup
funding_lookup = {}
for record in funding_records:
    if 'Project_Name' in record and 'Amount' in record:
        funding_lookup[record['Project_Name']] = int(record['Amount'])

# Load and process civic documents
f = open('/tmp/tmpj2m5b1a0.json', 'r')
civic_docs = json.load(f)
f.close()

# Find disaster projects starting in 2022
total_funding = 0
project_count = 0

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
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
            # Look for 2022 start date
            for j in range(i, min(len(lines), i+6)):
                context = lines[j]
                if '2022' in context:
                    lower = context.lower()
                    if 'st:' in lower or 'start:' in lower:
                        amount = funding_lookup.get(line, 0)
                        if amount > 0:
                            total_funding += amount
                            project_count += 1
                        break

result = {'total_funding': total_funding, 'project_count': project_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json', 'var_functions.execute_python:92': {'status': 'checked'}}

exec(code, env_args)
