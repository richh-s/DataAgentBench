code = """import json, os

files = os.listdir('.')
funding_file = [f for f in files if 'query_db' in f and '44' in f][0]
civic_file = [f for f in files if 'query_db' in f and '15' in f][0]

with open(funding_file) as f:
    funding = json.load(f)

with open(civic_file) as f:
    civic = json.load(f)

funding_dict = {}
for item in funding:
    funding_dict[item['Project_Name']] = int(item['Amount'])

spring = []
for doc in civic:
    text = doc.get('text', '')
    if '2022' in text and 'Spring' in text:
        for line in text.split('\n'):
            line = line.strip()
            if line and line.istitle() and len(line) > 10:
                names = [p['name'] for p in spring]
                if line not in names:
                    spring.append({'name': line})

matched = []
total = 0
for p in spring:
    name = p['name']
    if name in funding_dict:
        matched.append([name, funding_dict[name]])
        total += funding_dict[name]
    else:
        for funded, amount in funding_dict.items():
            if name.lower() in funded.lower() and len(name) > 15:
                matched.append([name, amount])
                total += amount
                break

count = len(matched)
result = 'Projects: ' + str(count) + ', Funding: $' + str(total)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
