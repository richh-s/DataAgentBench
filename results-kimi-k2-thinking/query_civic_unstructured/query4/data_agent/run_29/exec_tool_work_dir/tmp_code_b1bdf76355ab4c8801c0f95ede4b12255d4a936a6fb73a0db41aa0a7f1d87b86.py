code = """import json, os

files = os.listdir('.')
funding_file = [f for f in files if 'query_db' in f and any(str(n) in f for n in [14,28,44,46])][0]
civic_file = [f for f in files if 'query_db' in f and f != funding_file][0]

with open(funding_file) as f:
    funding = json.load(f)

with open(civic_file) as f:
    civic = json.load(f)

funding_dict = {}
for item in funding:
    funding_dict[item['Project_Name']] = int(item['Amount'])

spring_projects = []
for doc in civic:
    text = doc.get('text','')
    if '2022' in text and ('Spring' in text or 'March' in text or 'April' in text or 'May' in text):
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and line.istitle() and len(line) > 10:
                names = [p['name'] for p in spring_projects]
                if line not in names:
                    spring_projects.append({'name': line})

matched = []
total = 0
for proj in spring_projects:
    name = proj['name']
    if name in funding_dict:
        matched.append([name, funding_dict[name]])
        total += funding_dict[name]
    else:
        for funded, amount in funding_dict.items():
            if name.lower() in funded.lower():
                if len(name) > 15:
                    matched.append([name, amount])
                    total += amount
                    break

count = len(matched)
formatted = str(total)
result = 'Projects started in Spring 2022: ' + str(count) + '. Total funding: $' + formatted

print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
