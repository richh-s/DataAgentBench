code = """import json, re

funding = json.load(open(str(var_functions.query_db:2)))
civic = json.load(open(str(var_functions.query_db:6)))

fund_map = {}
for item in funding:
    if float(item['Amount']) > 50000:
        name = item['Project_Name']
        clean = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        fund_map[name] = float(item['Amount'])
        fund_map[clean] = float(item['Amount'])

capital_design = set()

for doc in civic:
    t = doc.get('text', '')
    in_design = False
    for line in t.split('\n'):
        line = line.strip()
        if 'Capital Improvement Projects (Design)' in line:
            in_design = True
        elif 'Capital Improvement Projects (Construction)' in line:
            in_design = False
        if in_design and line and len(line) > 15:
            if 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line and 'fire' not in line:
                if 'Page' not in line and 'Agenda' not in line:
                    if 'RECOMMENDED' not in line.upper():
                        capital_design.add(line)

count = 0
for proj in capital_design:
    clean_proj = re.sub(r'\s*\([^)]*\)\s*$', '', proj).strip()
    if proj in fund_map or clean_proj in fund_map:
        count += 1

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
