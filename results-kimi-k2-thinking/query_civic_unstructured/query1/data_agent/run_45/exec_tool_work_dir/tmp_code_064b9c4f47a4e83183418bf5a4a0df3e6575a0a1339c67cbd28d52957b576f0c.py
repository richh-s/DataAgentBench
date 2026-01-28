code = """import json, re

f_file = var_functions.query_db:2
c_file = var_functions.query_db:6

with open(f_file) as f:
    funding = json.load(f)

with open(c_file) as f:
    civic = json.load(f)

fund_map = {}
for rec in funding:
    if float(rec['Amount']) > 50000:
        name = rec['Project_Name']
        clean = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        fund_map[name] = float(rec['Amount'])
        fund_map[clean] = float(rec['Amount'])

cap_design = []

for doc in civic:
    text = doc['text']
    # Find design projects section
    if '(Design)' in text:
        # Split by lines and find capital design projects  
        in_design = False
        for line in text.split('\n'):
            line = line.strip()
            if '(Design)' in line:
                in_design = True
            elif '(Construction)' in line:
                in_design = False
            
            if in_design and line and len(line) > 10:
                if 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line and 'fire' not in line:
                    if 'Page' not in line and 'Agenda' not in line and 'RECOMMENDED' not in line.upper():
                        # This is likely a project name
                        if 'Updates:' not in line and 'Schedule:' not in line and 'Capital Improvement' not in line:
                            cap_design.append(line)

# Count matches
count = 0
matched = []

for proj in cap_design:
    proj_clean = re.sub(r'\s*\([^)]*\)\s*$', '', proj).strip()
    if proj in fund_map or proj_clean in fund_map:
        count += 1
        amt = fund_map.get(proj) or fund_map.get(proj_clean)
        matched.append({'project': proj, 'amount': amt})

result = {'count': count, 'matched': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
