code = """import json

# Load funding data
funding_path = var_functions.query_db:5
with open(funding_path) as f:
    funding_records = json.load(f)

# Load civic documents
civic_path = var_functions.query_db:6
with open(civic_path) as f:
    civic_docs = json.load(f)

# Build funding map
funding_map = {}
for item in funding_records:
    funding_map[item['Project_Name']] = int(item['Amount'])

# Extract projects from documents
project_list = []
for doc in civic_docs:
    text = doc.get('text', '')
    parts = text.split('Capital Improvement Projects')
    for section in parts[1:]:
        lines = section.split('\n')
        for line in lines:
            line = line.strip()
            if line and len(line) > 10 and 'Project' not in line and 'Schedule' not in line:
                if 'Design' in section[:500]:
                    project_list.append({'name': line, 'status': 'design', 'type': 'capital'})

# Count design projects with funding > 50000
count = 0
matches = []
design_names = set()

for p in project_list:
    if p['status'] == 'design' and p['name'] not in design_names:
        design_names.add(p['name'])
        for funded_name, amount in funding_map.items():
            if amount > 50000:
                if p['name'].lower() in funded_name.lower() or funded_name.lower() in p['name'].lower():
                    if abs(len(p['name']) - len(funded_name)) < 30:
                        count += 1
                        matches.append({'project': p['name'], 'amount': amount, 'funded_as': funded_name})
                        break

result = {'count': count, 'matches': matches[:15]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
