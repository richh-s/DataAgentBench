code = """import json
f_file = open(var_functions.query_db:5)
funding_data = json.load(f_file)
f_file.close()
c_file = open(var_functions.query_db:6)
civic_docs = json.load(c_file)
c_file.close()

funding_map = {item['Project_Name']: int(item['Amount']) for item in funding_data}

design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 10 and not line.startswith('Page'):
                design_projects.add(line.replace('•', '').strip())

count = 0
for proj in design_projects:
    for funded_name, amount in funding_map.items():
        if amount > 50000:
            p = proj.lower()
            f = funded_name.lower()
            if p in f or f in p:
                count += 1
                break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
