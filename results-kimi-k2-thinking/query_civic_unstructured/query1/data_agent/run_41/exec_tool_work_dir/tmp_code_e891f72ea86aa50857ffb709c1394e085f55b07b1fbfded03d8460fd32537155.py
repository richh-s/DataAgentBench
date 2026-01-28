code = """import json, re

funding_data = locals()['var_functions.query_db:32']
civic_path = locals()['var_functions.query_db:6']

with open(civic_path) as f:
    civic_data = json.load(f)

funding_lookup = {}
for item in funding_data:
    name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[name] = amount
    base = name.split(' (')[0]
    funding_lookup[base] = amount

found = 0
added = set()

design_marker = 'Capital Improvement Projects (Design)'
construction_marker = 'Capital Improvement Projects (Construction)'

for doc in civic_data:
    text = doc.get('text', '')
    begin = text.find(design_marker)
    if begin >= 0:
        part = text[begin:begin+4000]
        end = part.find(construction_marker)
        if end > 0:
            part = part[:end]
        
        for line in part.split('\n'):
            line = line.strip()
            if len(line) > 15 and 'Updates:' not in line and 'Schedule:' not in line:
                if not line.startswith('(') and not line.startswith('•'):
                    clean = line.rstrip('.,:;')
                    if clean in funding_lookup and funding_lookup[clean] > 50000 and clean not in added:
                        added.add(clean)
                        found += 1

print('__RESULT__:')
print(found)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
