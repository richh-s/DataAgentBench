code = """import json, re

f = json.load(open(var_functions.query_db:2))
c = json.load(open(var_functions.query_db:6))

fund = {}
for x in f:
    if float(x['Amount']) > 50000:
        n = x['Project_Name']
        fund[n] = float(x['Amount'])
        fund[re.sub(r'\s*\([^)]*\)\s*$', '', n).strip()] = float(x['Amount'])

design = []
for d in c:
    txt = d.get('text', '')
    design_mode = False
    for line in txt.split('\n'):
        line = line.strip()
        if 'Capital Improvement Projects (Design)' in line:
            design_mode = True
        elif 'Capital Improvement Projects (Construction)' in line:
            design_mode = False
        if design_mode and line and len(line) > 10:
            if 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line and 'fire' not in line:
                if 'Page' not in line and 'Agenda' not in line and 'RECOMMENDED' not in line.upper():
                    if 'Updates:' not in line and 'Schedule:' not in line and not line.startswith('('):
                        design.append(line)

count = sum(1 for p in design if p in fund or re.sub(r'\s*\([^)]*\)\s*$', '', p).strip() in fund)

result = count
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
