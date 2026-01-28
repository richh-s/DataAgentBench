code = """import json

# Load data from stored file paths
civic_docs = json.load(open('/tmp/tmpw8a01a0z.json'))
funding_records = json.load(open('/tmp/tmptjtu3_1d.json'))

print('Loaded data')
print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_records))

# Parse to find park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line in lines:
        line_lower = line.lower().strip()
        # Check for completed park projects with 2022
        if 'completed' in line_lower and '2022' in line and 'park' in line_lower:
            if len(line) > 10:  # Skip very short lines
                park_projects_2022.append(line.strip())

print('Found {} park projects'.format(len(park_projects_2022)))

# Check specifically for Bluffs Park Shade Structure which appears in sample
bluffs_park_found = False
marie_canyon_found = False
broad_beach_found = False
point_dume_found = False

for proj in park_projects_2022:
    if 'bluffs park shade' in proj.lower():
        bluffs_park_found = True
    if 'marie canyon green' in proj.lower():
        marie_canyon_found = True
    if 'broad beach road water quality' in proj.lower():
        broad_beach_found = True
    if 'point dume walkway' in proj.lower():
        point_dume_found = True

print('Bluffs Park found:', bluffs_park_found)
print('Marie Canyon found:', marie_canyon_found)
print('Broad Beach found:', broad_beach_found)
print('Point Dume found:', point_dume_found)

# Check funding for these projects
target_projects = [
    'Bluffs Park Shade Structure',
    'Marie Canyon Green Streets',
    'Broad Beach Road Water Quality Repair',
    'Point Dume Walkway Repairs'
]

funding_dict = {}
for f in funding_records:
    funding_dict[f['Project_Name'].lower()] = int(f['Amount'])

total_funding = 0
found_projects = []

for target in target_projects:
    if target.lower() in funding_dict:
        amount = funding_dict[target.lower()]
        total_funding += amount
        found_projects.append({'name': target, 'amount': amount})

result = {
    'total_funding': total_funding,
    'matching_projects': found_projects,
    'projects_found_in_docs': len(park_projects_2022)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
