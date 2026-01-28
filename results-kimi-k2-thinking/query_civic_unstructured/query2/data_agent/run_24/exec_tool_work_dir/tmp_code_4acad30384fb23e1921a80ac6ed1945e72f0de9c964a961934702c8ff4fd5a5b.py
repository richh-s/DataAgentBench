code = """import json

# Load funding data
funding_records = json.load(open('/tmp/tmptjtu3_1d.json'))

# Create mapping of project names to amounts
funding_dict = {}
for f in funding_records:
    funding_dict[f['Project_Name'].lower()] = int(f['Amount'])

print('Loaded %d funding records' % len(funding_dict))

# Park projects completed in 2022 (from civic docs)
park_projects_2022 = [
    'Bluffs Park Shade Structure',  # Completed November 2022
    'Broad Beach Road Water Quality Repair',  # Completed November 2022
    'Point Dume Walkway Repairs'  # Completed November 2022
]

# Calculate total funding
total_funding = 0
matched_projects = []

for project in park_projects_2022:
    project_lower = project.lower()
    if project_lower in funding_dict:
        amount = funding_dict[project_lower]
        total_funding += amount
        matched_projects.append({'project': project, 'amount': amount})
        print('Found: %s - $%d' % (project, amount))
    else:
        print('Not found in funding: %s' % project)

# Also check for partial matches
print('\nChecking for partial matches...')
for f in funding_records:
    name = f['Project_Name'].lower()
    if 'bluffs park' in name and 'shade' in name:
        if 'Bluffs Park Shade Structure' not in [p['project'] for p in matched_projects]:
            amount = int(f['Amount'])
            total_funding += amount
            matched_projects.append({'project': 'Bluffs Park Shade Structure', 'amount': amount})
            print('Partial match: %s - $%d' % (f['Project_Name'], amount))
    elif 'broad beach' in name and 'water quality' in name:
        if 'Broad Beach Road Water Quality Repair' not in [p['project'] for p in matched_projects]:
            amount = int(f['Amount'])
            total_funding += amount
            matched_projects.append({'project': 'Broad Beach Road Water Quality Repair', 'amount': amount})
            print('Partial match: %s - $%d' % (f['Project_Name'], amount))
    elif 'point dume' in name and 'walkway' in name:
        if 'Point Dume Walkway Repairs' not in [p['project'] for p in matched_projects]:
            amount = int(f['Amount'])
            total_funding += amount
            matched_projects.append({'project': 'Point Dume Walkway Repairs', 'amount': amount})
            print('Partial match: %s - $%d' % (f['Project_Name'], amount))

# Remove duplicates and finalize
final_projects = {}
for p in matched_projects:
    final_projects[p['project']] = p['amount']

final_total = sum(final_projects.values())
final_list = [{'project': k, 'amount': v} for k, v in final_projects.items()]

result = {
    'total_funding': final_total,
    'projects': final_list,
    'project_count': len(final_list)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs'], 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json'}

exec(code, env_args)
