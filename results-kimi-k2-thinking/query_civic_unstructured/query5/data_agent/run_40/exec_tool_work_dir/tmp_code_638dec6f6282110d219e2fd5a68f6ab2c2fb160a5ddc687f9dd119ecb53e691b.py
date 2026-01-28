code = """import json, re

# Load funding data to build lookup
civic_docs_data = json.load(open(locals()['var_functions.query_db:66'], 'r'))
funding_data = json.load(open(locals()['var_functions.query_db:67'], 'r'))

funding_lookup = {rec['Project_Name']: int(rec['Amount']) for rec in funding_data if rec.get('Project_Name')}

# Find disaster projects that started in 2022
total = 0
count = 0

for doc in civic_docs_data:
    txt = doc.get('text', '')
    lines = txt.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if '(FEMA' in line or 'CalJPIA' in line or 'CalOES' in line:
            # Look for 2022 start date
            for j in range(i, min(i+6, len(lines))):
                ctx = lines[j]
                if '2022' in ctx:
                    lower = ctx.lower()
                    if 'st:' in lower or 'start:' in lower:
                        amount = funding_lookup.get(line, 0)
                        if amount > 0:
                            total += amount
                            count += 1
                        break

result = {'total_funding': total, 'project_count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json'}

exec(code, env_args)
