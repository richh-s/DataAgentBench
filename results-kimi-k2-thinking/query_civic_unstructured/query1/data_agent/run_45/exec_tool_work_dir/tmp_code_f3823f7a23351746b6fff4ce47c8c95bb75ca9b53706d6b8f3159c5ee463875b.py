code = """import json, re

with open(str(var_functions.query_db:2), 'r') as f:
    funding = json.load(f)

with open(str(var_functions.query_db:6), 'r') as f:
    civic = json.load(f)

fund = {}
for item in funding:
    if float(item['Amount']) > 50000:
        fund[item['Project_Name']] = float(item['Amount'])

cap_design = set()
for doc in civic:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        for line in text.split('\n'):
            line = line.strip()
            if line and 'FEMA' not in line and 'CalOES' not in line and len(line) > 10:
                if 'Page' not in line and 'Agenda' not in line:
                    cap_design.add(line)

count = sum(1 for p in cap_design if p in fund or re.sub(r'\s*\([^)]*\)\s*$', '', p).strip() in fund)

print('__RESULT__')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
