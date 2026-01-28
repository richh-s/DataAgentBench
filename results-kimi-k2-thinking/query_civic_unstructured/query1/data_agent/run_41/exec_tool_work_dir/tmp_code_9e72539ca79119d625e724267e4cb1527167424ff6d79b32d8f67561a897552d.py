code = """import json, re

funding_data = locals()['var_functions.query_db:32']
civic_path = locals()['var_functions.query_db:6']

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

funding_lookup = {}
for item in funding_data:
    name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[name] = amount
    base = name.split(' (')[0]
    funding_lookup[base] = amount

count = 0
seen = set()

for doc in civic_data:
    text = doc.get('text', '')
    design_idx = text.find('Capital Improvement Projects (Design)')
    if design_idx >= 0:
        design_part = text[design_idx:design_idx+4000]
        cons_idx = design_part.find('Capital Improvement Projects (Construction)')
        if cons_idx > 0:
            design_part = design_part[:cons_idx]
        
        for line in design_part.split('\n'):
            line = line.strip()
            if len(line) > 15 and not line.startswith('(') and 'Updates:' not in line:
                if 'Project Schedule:' not in line and 'Design:' not in line:
                    clean = line.rstrip('.,:;')
                    if clean in funding_lookup and funding_lookup[clean] > 50000:
                        if clean not in seen:
                            seen.add(clean)
                            count = count + 1

print('__RESULT__:')
print(str(count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
