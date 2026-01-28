code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:4
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic docs
civic_file = var_functions.query_db:16
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print('Funding records:', len(funding_data))
print('Civic docs:', len(civic_docs))

# Filter funding > 50000
high_funding = [f for f in funding_data if f.get('Amount') and int(f['Amount']) > 50000]
print('High funding records:', len(high_funding))

# Extract design projects
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    # Look for design section
    design_start = text.lower().find('capital improvement projects (design)')
    if design_start >= 0:
        # Get section
        section = text[design_start:design_start+2000]
        # Find end
        construction = section.lower().find('capital improvement projects (construction)')
        if construction > 0:
            section = section[:construction]
        # Split lines
        for line in section.split('\n'):
            line = line.strip()
            if len(line) > 5 and not any(s in line.lower() for s in ['design', 'capital improvement', 'updates:', 'project schedule']):
                design_projects.append(line)

print('Design projects candidates:', len(design_projects))

# Match
matches = 0
for design in design_projects:
    design_lower = design.lower()
    for fund in high_funding:
        fund_lower = fund['Project_Name'].lower()
        if design_lower in fund_lower or fund_lower in design_lower:
            matches += 1
            break

result = {'count': matches}
print('Matches found:', matches)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
