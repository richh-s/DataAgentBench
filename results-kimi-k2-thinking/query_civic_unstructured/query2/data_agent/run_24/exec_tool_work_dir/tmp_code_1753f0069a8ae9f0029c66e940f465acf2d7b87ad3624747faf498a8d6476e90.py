code = """import json

# Load data
civic_docs = json.load(open('/tmp/tmpw8a01a0z.json'))
funding = json.load(open('/tmp/tmptjtu3_1d.json'))

# Find park projects completed in 2022
projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line in lines:
        line_lower = line.lower().strip()
        if 'completed' in line_lower and '2022' in line and 'park' in line_lower:
            if len(line) > 10:
                projects_2022.append(line.strip())

print('Found projects:', len(projects_2022))

# Extract specific project names
names = []
for p in projects_2022:
    if 'bluffs park shade' in p.lower():
        names.append('Bluffs Park Shade Structure')
    if 'marie canyon green' in p.lower():
        names.append('Marie Canyon Green Streets')
    if 'broad beach road water quality' in p.lower():
        names.append('Broad Beach Road Water Quality Repair')
    if 'point dume walkway' in p.lower():
        names.append('Point Dume Walkway Repairs')

# Match with funding
funding_lookup = {f['Project_Name'].lower(): int(f['Amount']) for f in funding}

# Also check if these specific park projects exist in funding database
known_park_projects = [
    'Bluffs Park Shade Structure',
    'Marie Canyon Green Streets', 
    'Broad Beach Road Water Quality Repair',
    'Point Dume Walkway Repairs'
]

total = 0
matched = []

for name in known_park_projects:
    if name.lower() in funding_lookup:
        amount = funding_lookup[name.lower()]
        total += amount
        matched.append({'name': name, 'amount': amount})

result = {'total_funding': total, 'projects': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
