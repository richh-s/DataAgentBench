code = """import json

funding_data = json.load(open(str(var_functions.query_db:5)))
civic_docs = json.load(open(str(var_functions.query_db:6)))

funding_map = {}
for item in funding_data:
    funding_map[item['Project_Name']] = int(item['Amount'])

design_projs = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 10 and not line.startswith('Page'):
                design_projs.add(line.replace('•', '').strip())

count = 0
for proj in design_projs:
    for funded_name, amt in funding_map.items():
        if amt > 50000:
            p_lower = proj.lower()
            f_lower = funded_name.lower()
            if p_lower in f_lower or f_lower in p_lower:
                if abs(len(proj) - len(funded_name)) < 35:
                    count += 1
                    break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
