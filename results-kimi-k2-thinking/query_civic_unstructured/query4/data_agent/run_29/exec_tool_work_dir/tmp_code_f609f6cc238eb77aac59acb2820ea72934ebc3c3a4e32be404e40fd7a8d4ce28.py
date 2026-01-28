code = """import json, os, re

files = os.listdir('.')
funding_file = None
civic_file = None

for f in files:
    if 'query_db' in f:
        if '44' in f or '46' in f:
            funding_file = f
        else:
            civic_file = f

print('Files:', funding_file, civic_file)

with open(funding_file, 'r') as f:
    funding = json.load(f)

with open(civic_file, 'r') as f:
    civic = json.load(f)

funding_dict = {}
for item in funding:
    funding_dict[item['Project_Name']] = int(item['Amount'])

patterns = ['2022-Spring', '2022 March', '2022 April', '2022 May', 'Spring 2022']

spring_projects = []
for doc in civic:
    text = doc.get('text', '')
    for pattern in patterns:
        if pattern.lower() in text.lower():
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if line and len(line) > 10 and '.' not in line[:2]:
                    if line.istitle() and line not in [p['name'] for p in spring_projects]:
                        spring_projects.append({'name': line})
            break

matched = []
total = 0
for proj in spring_projects:
    name = proj['name']
    if name in funding_dict:
        matched.append([name, funding_dict[name]])
        total += funding_dict[name]
    else:
        for funded_name, amount in funding_dict.items():
            if name.lower() in funded_name.lower():
                matched.append([name, amount])
                total += amount
                break

count = len(matched)
formatted = str(total)
result = 'Projects started in Spring 2022: ' + str(count) + '. Total funding: $' + formatted

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
