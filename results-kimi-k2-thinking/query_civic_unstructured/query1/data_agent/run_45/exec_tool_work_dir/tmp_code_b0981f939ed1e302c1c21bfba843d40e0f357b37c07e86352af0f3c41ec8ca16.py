code = """import json, re

funding_path = var_functions.query_db:2
civic_path = var_functions.query_db:6

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

fund_dict = {}
for item in funding_data:
    amt = float(item['Amount'])
    if amt > 50000:
        name = item['Project_Name']
        fund_dict[name] = amt

cap_design = []
for doc in civic_docs:
    t = doc.get('text', '')
    design_started = False
    for line in t.split('\n'):
        line = line.strip()
        if 'Capital Improvement Projects (Design)' in line:
            design_started = True
        elif 'Capital Improvement Projects (Construction)' in line:
            break
        if design_started and line and len(line) > 15 and 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line:
            if 'Page' not in line and 'Agenda' not in line and 'RECOMMENDED' not in line.upper():
                if 'Updates:' not in line and 'Schedule:' not in line:
                    cap_design.append(line)

count = 0
for proj in cap_design:
    if proj in fund_dict:
        count += 1
    else:
        clean = re.sub(r'\s*\([^)]*\)\s*$', '', proj).strip()
        if clean in fund_dict:
            count += 1

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
