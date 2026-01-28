code = """import json, re

f = open('file_storage/functions.query_db:2.json', 'r')
civic_docs = json.load(f)
f.close()

f2 = open('file_storage/functions.query_db:20.json', 'r')
funding_data = json.load(f2)
f2.close()

park_projects_2022_names = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        park_keywords = ['Park', 'playground', 'walkway', 'Bluffs Park']
        if any(kw in line for kw in park_keywords) and len(line) < 100:
            search_window = '\n'.join(lines[max(0,i-5):min(len(lines), i+8)])
            if '2022' in search_window and ('completed' in search_window.lower() or 'completion' in search_window.lower()):
                project_name = line
                if project_name not in [p for p in park_projects_2022_names]:
                    park_projects_2022_names.append(project_name)

total_funding = 0
matching_funds = []

for project_name in park_projects_2022_names:
    for fund in funding_data:
        if fund['Project_Name'] and project_name.lower() in fund['Project_Name'].lower():
            amount = int(fund['Amount'])
            total_funding += amount
            matching_funds.append({'project': project_name, 'funded_project': fund['Project_Name'], 'amount': amount})

result = {
    'park_projects_2022': park_projects_2022_names,
    'matching_funds': matching_funds,
    'total_funding_check': sum(f['amount'] for f in matching_funds)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json'], 'var_functions.execute_python:8': {'path': 'file_storage/functions.query_db:2.json'}, 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:12': 'Loaded 5 documents', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
