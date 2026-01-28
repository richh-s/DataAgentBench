code = """import json
import re

funding_data = locals()['var_functions.query_db:32']
with open(locals()['var_functions.query_db:6'], 'r') as f:
    civic_data = json.load(f)

funding_lookup = {}
for item in funding_data:
    name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[name] = amount
    base = name.split(' (')[0]
    funding_lookup[base] = amount

design_section_start = 'Capital Improvement Projects (Design)'
cons_section_start = 'Capital Improvement Projects (Construction)'
seen = set()

count = 0

for doc in civic_data:
    text = doc.get('text', '')
    design_pos = text.find(design_section_start)
    if design_pos > 0:
        section = text[design_pos:design_pos+5000]
        cons_pos = section.find(cons_section_start)
        if cons_pos > 0:
            section = section[:cons_pos]
        
        lines = section.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) > 15:
                if 'Updates:' not in line and 'Project Schedule:' not in line:
                    if not line.startswith('(') and not line.startswith('•'):
                        clean = line.rstrip('.,:;')
                        if clean in funding_lookup:
                            amount = funding_lookup[clean]
                            if amount > 50000 and clean not in seen:
                                seen.add(clean)
                                count = count + 1

print('__RESULT__:')
print(count)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
