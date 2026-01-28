code = """import json

# Read funding data
with open(var_functions.query_db:8, 'r') as f:
    funding = json.load(f)

# Read civic documents
with open(var_functions.query_db:10, 'r') as f:
    civic_docs = json.load(f)

print('Funding records:', len(funding))
print('Civic documents:', len(civic_docs))

# Combine all civic text
all_text = ' '.join([doc.get('text', '') for doc in civic_docs])

# Find projects in design section
design_start = all_text.find('Capital Improvement Projects (Design)')
construction_start = all_text.find('Capital Improvement Projects (Construction)')

if design_start > 0 and construction_start > 0:
    design_section = all_text[design_start:construction_start]
else:
    design_section = all_text

# Check which funded projects are in design section
capital_count = 0
capital_projects = []

for item in funding:
    proj_name = item['Project_Name']
    # Skip disaster projects
    if any(x in proj_name for x in ['(FEMA', '(CalJPIA', '(CalOES']):
        continue
    # Check if mentioned in design section
    if proj_name in design_section:
        capital_count += 1
        capital_projects.append(proj_name)

print('Found capital design projects:', capital_count)
print('Projects:', capital_projects[:10])

result = {'count': capital_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
