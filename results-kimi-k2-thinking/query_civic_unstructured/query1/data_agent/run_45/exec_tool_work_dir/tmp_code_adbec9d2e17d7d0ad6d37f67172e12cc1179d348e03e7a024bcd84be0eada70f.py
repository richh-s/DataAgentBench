code = """import json, re

funding_file_path = str(var_functions.query_db:2)
civic_file_path = str(var_functions.query_db:6)

with open(funding_file_path) as f:
    funding = json.load(f)

with open(civic_file_path) as f:
    civic = json.load(f)

fund_map = {}
for item in funding:
    amount = float(item['Amount'])
    if amount > 50000:
        name = item['Project_Name']
        clean = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        fund_map[name] = amount
        fund_map[clean] = amount

capital_design_projects = []

for doc in civic:
    t = doc.get('text', '')
    for line in t.split('\n'):
        line = line.strip()
        if 'Capital Improvement Projects (Design)' in t:
            if len(line) > 15 and 'FEMA' not in line and 'CalOES' not in line:
                if 'Page' not in line and 'Agenda' not in line:
                    if 'RECOMMENDED' not in line.upper() and 'Updates:' not in line:
                        capital_design_projects.append(line)

count = 0
for p in capital_design_projects:
    pc = re.sub(r'\s*\([^)]*\)\s*$', '', p).strip()
    if p in fund_map or pc in fund_map:
        count += 1

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
