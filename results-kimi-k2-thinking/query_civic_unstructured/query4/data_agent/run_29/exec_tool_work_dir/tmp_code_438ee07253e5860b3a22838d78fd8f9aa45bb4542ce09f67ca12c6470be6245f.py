code = """import json, os, re

files = os.listdir('.')
funding_file = None
civic_file = None

for f in files:
    if 'query' in f:
        if '44' in f or '46' in f:
            funding_file = f
        else:
            civic_file = f

print('Files:', funding_file, civic_file)

# Load funding data
with open(funding_file, 'r') as f:
    funding = json.load(f)

# Load civic documents
with open(civic_file, 'r') as f:
    civic = json.load(f)

# Create funding lookup
funding_dict = {}
for item in funding:
    funding_dict[item['Project_Name']] = int(item['Amount'])

# Define Spring 2022 patterns
patterns = ['2022-Spring','2022 March','2022 April','2022 May','Spring 2022','March 2022','April 2022','May 2022','2022-March','2022-April']

# Find Spring 2022 projects
spring_ids = []
for i, doc in enumerate(civic):
    text = doc.get('text','')
    text_lower = text.lower()
    for pattern in patterns:
        if pattern.lower() in text_lower:
            spring_ids.append(i)
            break

print('Docs with Spring 2022 mentions:', len(spring_ids))

# Extract project names from these docs
spring_projects = []
for idx in spring_ids:
    text = civic[idx].get('text','')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        if line.startswith('Page') or 'Agenda' in line:
            continue
        if line.istitle():
            names = [p['name'] for p in spring_projects]
            if line not in names:
                spring_projects.append({'name': line})

print('Spring projects found:', len(spring_projects))

# Match with funding
matched = []
total = 0
for proj in spring_projects:
    name = proj['name']
    if name in funding_dict:
        amount = funding_dict[name]
        matched.append([name, amount])
        total += amount
    else:
        for funded_name, amount in funding_dict.items():
            if name.lower() in funded_name.lower() or funded_name.lower() in name.lower():
                if len(name) > 15 and len(funded_name) > 15:
                    matched.append([name, amount])
                    total += amount
                    break

# Format result
project_count = len(matched)
formatted_total = "{:,}".format(total)
result = "Projects started in Spring 2022: " + str(project_count) + ". Total funding: $" + formatted_total

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
