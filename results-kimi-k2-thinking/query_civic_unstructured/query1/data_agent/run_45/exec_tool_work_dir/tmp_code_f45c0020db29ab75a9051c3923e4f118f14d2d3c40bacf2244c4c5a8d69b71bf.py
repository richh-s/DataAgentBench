code = """import json
import re

funding_file = var_functions.query_db:2
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

civic_file = var_functions.query_db:6
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

funding_map = {}
for f in funding_data:
    if float(f.get('Amount', 0)) > 50000:
        name = f['Project_Name']
        clean = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        funding_map[name] = float(f['Amount'])
        funding_map[clean] = float(f['Amount'])

capital_design = set()

for doc in civic_docs:
    text = doc.get('text', '')
    start = text.find('(Design)')
    if start > 0:
        segment = text[start:]
        end = segment.find('(Construction)')
        if end > 0:
            segment = segment[:end]
        
        for line in segment.split('\n'):
            line = line.strip()
            if line and len(line) > 10 and 'Page' not in line and 'Agenda' not in line:
                if 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line and 'fire' not in line:
                    capital_design.add(line)

count = 0
for proj in capital_design:
    proj_clean = re.sub(r'\s*\([^)]*\)\s*$', '', proj).strip()
    if proj in funding_map or proj_clean in funding_map:
        count += 1

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
