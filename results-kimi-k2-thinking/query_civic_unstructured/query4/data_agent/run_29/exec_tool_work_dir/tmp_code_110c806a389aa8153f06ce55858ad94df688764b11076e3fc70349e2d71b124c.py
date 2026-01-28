code = """import json, os, re

# Get data files
files = os.listdir('.')
funding_file = [f for f in files if 'query_db' in f and any(n in f for n in ['14','28','44','46'])][0]
civic_file = [f for f in files if 'query_db' in f and f != funding_file][0]

with open(funding_file) as f:
    funding = json.load(f)

with open(civic_file) as f:
    civic = json.load(f)

# Build funding lookup
funding_dict = {}
for item in funding:
    funding_dict[item['Project_Name']] = int(item['Amount'])

# Find Spring 2022 projects
spring = []
patterns = ['2022-Spring','2022 March','2022 April','2022 May','Spring 2022','March 2022','April 2022','May 2022']

for doc in civic:
    text = doc.get('text','')
    low = text.lower()
    for pat in patterns:
        if pat.lower() in low:
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if line and len(line) > 10 and (line.istitle() or (line[0].isupper() and len(line.split()) > 2)):
                    names = [p['name'] for p in spring]
                    if line not in names:
                        spring.append({'name': line})
            break

# Match
matched = []
total = 0
for p in spring:
    name = p['name']
    if name in funding_dict:
        matched.append([name, funding_dict[name]])
        total += funding_dict[name]
    else:
        for funded, amount in funding_dict.items():
            if name.lower() in funded.lower() or funded.lower() in name.lower():
                if len(name) > 15:
                    matched.append([name, amount])
                    total += amount
                    break

count = len(matched)
formatted = "{:,}".format(total)
result = "Projects started in Spring 2022: " + str(count) + ". Total funding: $" + formatted

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
