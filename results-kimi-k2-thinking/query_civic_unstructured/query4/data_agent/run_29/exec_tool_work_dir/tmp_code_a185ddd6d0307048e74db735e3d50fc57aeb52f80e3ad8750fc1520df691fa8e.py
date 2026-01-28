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

print('Loading:', funding_file, civic_file)

with open(funding_file, 'r') as f:
    funding = json.load(f)

with open(civic_file, 'r') as f:
    civic = json.load(f)

funding_dict = {}
for item in funding:
    funding_dict[item['Project_Name']] = int(item['Amount'])

patterns = ['2022-Spring','2022 March','2022 April','2022 May','Spring 2022']

spring_projects = []
for doc in civic:
    text = doc.get('text','')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        if line.startswith('Page') or 'Agenda' in line:
            continue
        is_project = line.istitle() or (line[0].isupper() and len(line.split()) > 2)
        if is_project:
            context = '\n'.join(lines[i:i+8])
            for pattern in patterns:
                if pattern.lower() in context.lower():
                    names = [p['name'] for p in spring_projects]
                    if line not in names:
                        spring_projects.append({'name': line})
                    break

matched = []
total_funding = 0
for proj in spring_projects:
    name = proj['name']
    if name in funding_dict:
        amount = funding_dict[name]
        matched.append({'project': name, 'funding': amount})
        total_funding = total_funding + amount
    else:
        for funded_name, amount in funding_dict.items():
            if name.lower() in funded_name.lower() or funded_name.lower() in name.lower():
                if len(name) > 15:
                    matched.append({'project': name, 'funding': amount})
                    total_funding = total_funding + amount
                    break

count = len(matched)
funding_formatted = "{:,}".format(total_funding)
result = "Projects started in Spring 2022: " + str(count) + ". Total funding: $" + funding_formatted

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
