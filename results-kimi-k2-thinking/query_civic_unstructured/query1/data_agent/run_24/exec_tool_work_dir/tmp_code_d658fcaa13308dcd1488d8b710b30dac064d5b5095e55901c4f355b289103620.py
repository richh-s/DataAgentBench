code = """import json

# Get the file paths from the variable storage
funding_file = locals()['var_functions.query_db:6']
civic_file = locals()['var_functions.query_db:5']

# Read funding data
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Filter for funding > 50000
high_funding = [item for item in funding_data if int(item['Amount']) > 50000]

# Read civic documents
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Extract design status capital projects
design_capital_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    # Find design section header
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start >= 0:
        # Get the section until next major heading
        section = text[design_start:]
        # Find end of section (next capital projects heading)
        next_section = section.find('\n\nCapital Improvement Projects (')
        if next_section > 0:
            section = section[:next_section]
        
        # Get lines and filter for project names
        lines = section.split('\n')
        for line in lines:
            line = line.strip()
            if line and not line.startswith('Capital Improvement Projects') and not line.startswith('('):
                design_capital_projects.append(line)

# Remove duplicates
design_capital_projects = list(set(design_capital_projects))

# Count matches
matched = 0
for project_name in design_capital_projects:
    for funding_item in high_funding:
        funding_name = funding_item['Project_Name']
        if project_name == funding_name or funding_name.startswith(project_name + ' '):
            matched += 1
            break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
