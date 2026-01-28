code = """import json, re

f_file = var_functions.query_db:2
with open(f_file) as file1:
    funding = json.load(file1)

c_file = var_functions.query_db:6
with open(c_file) as file2:
    civic = json.load(file2)

fund_map = {}
for rec in funding:
    amt = float(rec['Amount'])
    if amt > 50000:
        name = rec['Project_Name']
        clean = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        fund_map[name] = amt
        fund_map[clean] = amt

capital_design = []

for doc in civic:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design = False
    
    for line in lines:
        line = line.strip()
        if 'Capital Improvement Projects (Design)' in line:
            in_design = True
        elif 'Capital Improvement Projects (Construction)' in line:
            in_design = False
        
        if in_design and line and len(line) > 15:
            if 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line and 'fire' not in line:
                if 'Page' not in line and 'Agenda' not in line and 'RECOMMENDED' not in line.upper():
                    if 'Updates:' not in line and 'Schedule:' not in line and 'Capital Improvement' not in line:
                        capital_design.append(line)

count = 0
for proj in capital_design:
    proj_clean = re.sub(r'\s*\([^)]*\)\s*$', '', proj).strip()
    if proj in fund_map or proj_clean in fund_map:
        count += 1

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
