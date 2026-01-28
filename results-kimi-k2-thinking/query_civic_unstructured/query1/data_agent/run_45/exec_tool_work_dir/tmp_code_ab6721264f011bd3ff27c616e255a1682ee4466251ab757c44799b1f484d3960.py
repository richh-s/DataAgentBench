code = """import json, re

f_file = var_functions.query_db:2
c_file = var_functions.query_db:6

with open(f_file) as f:
    funding = json.load(f)

with open(c_file) as f:
    civic = json.load(f)

fund_map = {}
for rec in funding:
    amt = float(rec.get('Amount', 0))
    if amt > 50000:
        name = rec['Project_Name']
        clean = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        fund_map[name] = amt
        fund_map[clean] = amt

cap_design = set()

for doc in civic:
    text = doc.get('text', '')
    start = text.find('(Design)')
    if start > 0:
        segment = text[start:]
        end = segment.find('(Construction)')
        if end > 0:
            segment = segment[:end]
        
        for line in segment.split('\n'):
            line = line.strip()
            if len(line) > 10 and 'Page' not in line and 'Agenda' not in line:
                if 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line and 'fire' not in line:
                    cap_design.add(line)

count = 0
for proj in cap_design:
    proj_clean = re.sub(r'\s*\([^)]*\)\s*$', '', proj).strip()
    if proj in fund_map or proj_clean in fund_map:
        count += 1

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
