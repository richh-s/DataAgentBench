code = """import json

funding_file_path = var_functions.query_db:0
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

civic_file_path = var_functions.query_db:2
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

text = civic_docs[0]['text']

# Find design section start and end indices
design_start = text.find('Capital Improvement Projects (Design)')
construction_start = text.find('Capital Improvement Projects (Construction)')

project_names = []

if design_start >= 0 and construction_start > design_start:
    design_section = text[design_start:construction_start]
    lines = design_section.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        # Skip empty lines and markers
        if not line or line.startswith('(cid:') or line.startswith('Page'):
            continue
        # Check if next line indicates project updates
        if i + 1 < len(lines):
            next_line = lines[i+1]
            if 'Updates:' in next_line and '(cid:' in next_line:
                project_names.append(line)

# Remove duplicates
unique_projects = list(set(project_names))

# Now match with funding data
matching_funding = []
for project in unique_projects:
    for fund in funding_data:
        if fund['Project_Name'] == project and int(fund['Amount']) > 50000:
            matching_funding.append(fund)

result = {
    'design_projects': unique_projects,
    'design_projects_count': len(unique_projects),
    'matching_funding_count': len(matching_funding),
    'matching_projects': [f['Project_Name'] for f in matching_funding]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['civic_docs']}

exec(code, env_args)
