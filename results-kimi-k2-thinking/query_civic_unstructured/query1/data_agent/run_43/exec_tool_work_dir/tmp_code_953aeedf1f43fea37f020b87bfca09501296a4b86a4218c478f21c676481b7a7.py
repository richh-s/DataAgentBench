code = """import json

funding_path = var_functions.query_db:5
civic_path = var_functions.query_db:6

funding_data = json.load(open(funding_path))
civic_data = json.load(open(civic_path))

funding = {item['Project_Name']: int(item['Amount']) for item in funding_data}

design_projects = set()
for doc in civic_data:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 10 and line[0].isalpha():
                design_projects.add(line)

count = 0
for proj in design_projects:
    for funded in funding:
        if funding[funded] > 50000:
            if proj.lower().find(funded.lower()) >= 0 or funded.lower().find(proj.lower()) >= 0:
                if abs(len(proj) - len(funded)) < 30:
                    count += 1
                    break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
