code = """import json
import re

funding_data = locals()['var_functions.query_db:32']
with open(locals()['var_functions.query_db:6']) as f:
    civic_data = json.load(f)

funding_lookup = {}
for item in funding_data:
    name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[name] = amount
    base = name.split(' (')[0]
    funding_lookup[base] = amount

counter = 0
seen_projects = set()

design_header = 'Capital Improvement Projects (Design)'
cons_header = 'Capital Improvement Projects (Construction)'

for doc in civic_data:
    text = doc.get('text', '')
    design_start = text.find(design_header)
    if design_start >= 0:
        snippet = text[design_start:design_start+4000]
        cons_pos = snippet.find(cons_header)
        if cons_pos > 0:
            snippet = snippet[:cons_pos]
        
        lines = snippet.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) > 15 and 'Updates:' not in line and 'Schedule:' not in line:
                if not line.startswith('(') and not line.startswith('•'):
                    clean_name = line.rstrip('.,:;')
                    if clean_name in funding_lookup:
                        if funding_lookup[clean_name] > 50000 and clean_name not in seen_projects:
                            seen_projects.add(clean_name)
                            counter += 1

print('__RESULT__:')
print(counter)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
