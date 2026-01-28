code = """import json, re

civic_docs = json.load(open('var_functions.query_db_6'))
funding = json.load(open('var_functions.query_db_8'))

park_projects = []
matches = []

for doc in civic_docs:
    text = doc.get('text', '')
    for line in text.split('\n'):
        line = line.strip()
        if 'Park' in line and 'completed' in text.lower() and '2022' in text:
            if len(line) < 120 and 'update' not in line.lower():
                park_projects.append(line)
                break

for project in park_projects:
    pl = project.lower()
    for f in funding:
        fl = f['Project_Name'].lower()
        if pl == fl:
            matches.append(int(f['Amount']))

total = sum(matches)
print('__RESULT__:')
print(json.dumps({'total_funding': total, 'matched': len(matches)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
