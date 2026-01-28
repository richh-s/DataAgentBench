code = """import json, os
files = os.listdir('.')
print('Files:', files)

# Load one file at a time to avoid syntax issues
funding_file = None
civic_file = None

for f in files:
    if 'query_db' in f:
        if '44' in f:
            funding_file = f
        elif '15' in f or '18' in f or '24' in f:
            civic_file = f

print('Funding:', funding_file)
print('Civic:', civic_file)

with open(funding_file) as f:
    funding = json.load(f)

with open(civic_file) as f:
    civic = json.load(f)

print('Records:', len(funding), len(civic))

# Create funding lookup
funding_dict = {}
for item in funding:
    funding_dict[item['Project_Name']] = int(item['Amount'])

# Find Spring 2022 projects
spring = []
for doc in civic:
    text = doc.get('text', '')
    low = text.lower()
    if '2022' in low and ('spring' in low or 'march' in low or 'april' in low or 'may' in low):
        for line in text.split('\n'):
            line = line.strip()
            if line and line.istitle() and len(line) > 15:
                names = [p['name'] for p in spring]
                if line not in names:
                    spring.append({'name': line})

print('Spring projects found:', len(spring))

# Match with funding
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
print('Matched projects:', count)
print('Total funding:', total)

result = 'Projects started in Spring 2022: ' + str(count) + '. Total funding: $' + str(total)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
