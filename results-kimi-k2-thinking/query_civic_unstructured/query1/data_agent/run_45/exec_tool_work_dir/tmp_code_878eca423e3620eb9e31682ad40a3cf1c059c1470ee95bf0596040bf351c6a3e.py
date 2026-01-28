code = """import json, re
funding_path = var_functions.query_db:2
civic_path = var_functions.query_db:6

with open(funding_path) as f:
    funding_data = json.load(f)

with open(civic_path) as f:
    civic_data = json.load(f)

fund_dict = {}
for item in funding_data:
    amt = float(item['Amount'])
    if amt > 50000:
        name = item['Project_Name']
        clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        fund_dict[name] = amt
        fund_dict[clean_name] = amt

capital_design_set = set()
for doc in civic_data:
    text = doc.get('text', '')
    design_section = False
    for line in text.split('\n'):
        line = line.strip()
        if 'Capital Improvement Projects (Design)' in line:
            design_section = True
        elif 'Capital Improvement Projects (Construction)' in line:
            design_section = False
        if design_section and line and len(line) > 15:
            if 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line and 'fire' not in line:
                if 'Page' not in line and 'Agenda' not in line and 'RECOMMENDED' not in line.upper():
                    if 'Updates:' not in line and 'Schedule:' not in line and 'Capital Improvement' not in line:
                        if not line.startswith('('):
                            capital_design_set.add(line)

count = 0
for proj in capital_design_set:
    proj_clean = re.sub(r'\s*\([^)]*\)\s*$', '', proj).strip()
    if proj in fund_dict or proj_clean in fund_dict:
        count += 1

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
