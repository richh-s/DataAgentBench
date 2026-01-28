code = """import json, os, re

# Load funding data
funding_file = locals()['var_functions.query_db:0']
civic_file = locals()['var_functions.query_db:1']

with open(funding_file) as f:
    funding_data = json.load(f)
with open(civic_file) as f:
    civic_data = json.load(f)

# Create lookup for projects > $50K
funding_lookup = {}
for item in funding_data:
    amt = int(item['Amount'])
    if amt > 50000:
        funding_lookup[item['Project_Name']] = amt

# Find projects
design_projects = set()

for doc in civic_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Check for capital projects in design
    if 'Capital Improvement Projects (Design)' in text:
        start = text.find('(Design)') + 8
        section = text[start:]
        
        # Find section end
        ends = [section.find('Capital Improvement Projects (Construction)'),
                section.find('Capital Improvement Projects (Not Started)'),
                section.find('Disaster Recovery Projects')]
        ends = [e for e in ends if e > 0]
        end = min(ends) if ends else len(section)
        section = section[:end]
        
        # Extract project names
        for line in section.split('\n'):
            line = line.strip()
            if len(line) > 5 and not line.startswith('(') and not line.startswith('-') and not line.startswith('•'):
                if line in funding_lookup:
                    design_projects.add(line)

# Return the count
count = len(design_projects)

print('__RESULT__:')
print(json.dumps({'count': count, 'projects': sorted(list(design_projects))}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:24': {'funding_records': 276, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}}

exec(code, env_args)
