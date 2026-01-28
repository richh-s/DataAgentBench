code = """import json

funding_data = json.load(open(var_functions.query_db:5))
civic_docs = json.load(open(var_functions.query_db:6))

funding_map = {}
for item in funding_data:
    funding_map[item['Project_Name']] = int(item['Amount'])

design_projects = set()
for doc in civic_docs:
    text = doc['text']
    if 'Capital Improvement Projects' in text and 'Design' in text:
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 10:
                if 'Page' not in line and 'Schedule' not in line:
                    design_projects.add(line)

count = 0
for proj in design_projects:
    for funded in funding_map:
        if funding_map[funded] > 50000:
            if proj.lower() in funded.lower() or funded.lower() in proj.lower():
                if abs(len(proj) - len(funded)) < 30:
                    count += 1
                    break

result = dict(count=count)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
