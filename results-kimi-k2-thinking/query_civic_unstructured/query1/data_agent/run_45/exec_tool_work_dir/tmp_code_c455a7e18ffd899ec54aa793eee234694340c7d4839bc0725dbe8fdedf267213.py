code = """import json, re

funding_path = var_functions.query_db:2
civic_path = var_functions.query_db:6

funding_file = open(funding_path, 'r')
funding_data = json.load(funding_file)
funding_file.close()

civic_file = open(civic_path, 'r')
civic_data = json.load(civic_file)
civic_file.close()

fund_map = {}
for rec in funding_data:
    amount = float(rec['Amount'])
    if amount > 50000:
        name = rec['Project_Name']
        clean = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        fund_map[name] = amount
        fund_map[clean] = amount

project_lines = []
for doc in civic_data:
    text = doc.get('text', '')
    is_design = False
    for line in text.split('\n'):
        line = line.strip()
        if len(line) > 15:
            if 'FEMA' in line or 'CalOES' in line or 'CalJPIA' in line or 'fire' in line:
                continue
            if 'Design' in text and 'Page' not in line and 'Agenda' not in line:
                if 'RECOMMENDED' not in line.upper() and 'Updates:' not in line and 'Schedule:' not in line:
                    project_lines.append(line)

count = 0
for proj in project_lines:
    clean_proj = re.sub(r'\s*\([^)]*\)\s*$', '', proj).strip()
    if proj in fund_map or clean_proj in fund_map:
        count += 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
