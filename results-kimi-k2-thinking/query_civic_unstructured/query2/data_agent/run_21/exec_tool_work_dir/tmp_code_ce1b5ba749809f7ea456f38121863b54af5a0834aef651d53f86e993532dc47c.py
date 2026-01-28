code = """import json

# Load funding data
f_path = locals()['var_functions.query_db:10']
with open(f_path, 'r') as f:
    funding = json.load(f)

# Load civic docs
c_path = locals()['var_functions.query_db:11']  
with open(c_path, 'r') as f:
    civic = json.load(f)

print('Data loaded')

# Extract all park projects from funding data
park_projects = []
for item in funding:
    if 'park' in item['Project_Name'].lower():
        park_projects.append({
            'name': item['Project_Name'],
            'amount': int(item['Amount'])
        })

print('Park projects in funding data:', len(park_projects))

# Find completed 2022 park projects from civic docs
completed_2022 = []
for doc in civic:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for project names with park
    for i, line in enumerate(lines):
        l = line.lower()
        if 'park' in l and len(line.strip()) > 5:
            # Check nearby lines for 2022 completion
            for j in range(i-2, i+4):
                if 0 <= j < len(lines):
                    nl = lines[j].lower()
                    if '2022' in nl and 'completed' in nl:
                        completed_2022.append(line.strip())
                        break

print('2022 completed park projects:', len(completed_2022))

# Match and calculate funding
total = 0
matched = []
for project in park_projects:
    for completed in completed_2022:
        if project['name'].lower() in completed.lower() or completed.lower() in project['name'].lower():
            matched.append(project)
            total += project['amount']
            break

print('Matched projects:', len(matched))
print('Total funding:', total)

for p in matched:
    print(' ', p['name'], ':', p['amount'])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
