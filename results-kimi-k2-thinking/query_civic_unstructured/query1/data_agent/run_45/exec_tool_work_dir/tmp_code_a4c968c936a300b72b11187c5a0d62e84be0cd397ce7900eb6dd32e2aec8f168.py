code = """import json, re

funding = json.load(open(var_functions.query_db:2)) 
civic = json.load(open(var_functions.query_db:6))

fund = {item['Project_Name']: float(item['Amount']) for item in funding if float(item['Amount']) > 50000}

cap_design = []
for doc in civic:
    if 'Capital Improvement Projects (Design)' in doc.get('text', ''):
        text = doc['text']
        for line in text.split('\n'):
            line = line.strip()
            if len(line) > 15 and 'FEMA' not in line and 'CalOES' not in line and 'fire' not in line:
                if 'Page' not in line and 'Agenda' not in line and 'RECOMMENDED' not in line.upper():
                    if 'Updates:' not in line and 'Schedule:' not in line:
                        cap_design.append(line)

count = 0
for proj in cap_design:
    clean = re.sub(r'\s*\([^)]*\)\s*$', '', proj).strip() 
    if proj in fund or clean in fund:
        count += 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
