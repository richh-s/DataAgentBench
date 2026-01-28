code = """import json

# Load the data from the files
funding_file = var_functions.query_db:8
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Show structure of funding data
print('Funding data sample:')
print(json.dumps(funding_data[:3], indent=2))

# Count total projects with > $50k funding
total_count = len(funding_data)
print('Total projects with > $50k funding:', total_count)

# Now let's look for projects with 'design' status
# For now, let's just do a simple keyword search in the text
civic_file = var_functions.query_db:10
with open(civic_file, 'r') as f:
    civic_docs_data = json.load(f)

# Search for projects mentioned in design context
keywords = ['(Design)', 'design phase', 'design plans', 'Complete Design']

print('Looking for design projects in civic documents...')
found_projects = set()

for doc in civic_docs_data:
    text = doc.get('text', '').lower()
    for proj in funding_data:
        proj_name = proj['Project_Name'].lower()
        # Check if project name appears in text AND design keywords appear
        if proj_name in text:
            for keyword in keywords:
                if keyword.lower() in text:
                    found_projects.add(proj['Project_Name'])
                    break

print('Found potentially relevant projects:', len(found_projects))
print('Sample:', list(found_projects)[:10])

# Count capital projects (not disaster)
capital_count = len([p for p in found_projects if not any(x in p.lower() for x in ['(fema', '(caljpia', '(caloes')])
print('Capital projects found:', capital_count)

result = {'count': capital_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
