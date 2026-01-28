code = """import json, re, os

# Access the file paths stored in variables
funding_path = locals()['var_functions.query_db:6']
civic_path = locals()['var_functions.query_db:8']

# Load the data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Build funding map for amounts > 50000
funding_projects = {}
for record in funding_data:
    amt = int(record['Amount'])
    if amt > 50000:
        name = record['Project_Name']
        # Clean the name for matching
        clean_key = name.lower()
        funding_projects[clean_key] = name

# Extract capital design projects from civic documents
design_projects = set()
for doc in civic_data:
    text = doc.get('text', '')
    # Find design section
    design_idx = text.find('Capital Improvement Projects (Design)')
    if design_idx == -1:
        continue
    constr_idx = text.find('Capital Improvement Projects (Construction)', design_idx)
    if constr_idx == -1:
        constr_idx = len(text)
    
    design_section = text[design_idx:constr_idx]
    lines = design_section.split('\n')
    for line in lines:
        line = line.strip()
        if len(line) > 10 and not line.startswith('(') and 'Capital Improvement' not in line:
            # Skip disaster projects
            if 'FEMA' in line or 'CalOES' in line or 'CalJPIA' in line:
                continue
            # Check for infrastructure keywords
            if any(kw in line.lower() for kw in ['road','park','drain','bridge','facility','system','plan','structure','study','improvements','repairs','street','water','traffic']):
                design_projects.add(line)

# Count matches with funding >= 50000
count = 0
for proj in design_projects:
    proj_key = proj.lower()
    # Try to find matching funding
    for fund_key in funding_projects:
        if proj_key in fund_key or fund_key in proj_key:
            count += 1
            break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
