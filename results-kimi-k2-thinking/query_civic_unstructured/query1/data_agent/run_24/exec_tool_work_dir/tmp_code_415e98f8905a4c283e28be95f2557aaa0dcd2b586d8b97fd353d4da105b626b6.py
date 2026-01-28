code = """import json

# Simple approach - load data and match
funding_path = locals()['var_functions.query_db:6']
civic_path = locals()['var_functions.query_db:64']

with open(funding_path) as f:
    funding = json.load(f)

with open(civic_path) as f:
    civic_docs = json.load(f)

# Get all funding > 50k
funding_names = set(r['Project_Name'] for r in funding if int(r['Amount']) > 50000)

# Extract design section project names (simple heuristic)
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        # Get section and split lines
        section = text.split('Capital Improvement Projects (Design)')[1].split('DISCUSSION')[0]
        for line in section.split('\n'):
            line = line.strip()
            # Skip empty and marker lines
            if line and not line.startswith('(') and not line.startswith('Capital'):
                # Simple filter: not metadata, reasonable length
                if 'To:' not in line and len(line) > 10:
                    design_projects.append(line)

# Remove duplicates
design_projects = list(set(design_projects))

# Count matches
matched = 0
for proj in design_projects:
    for fund_name in funding_names:
        if proj == fund_name or fund_name.startswith(proj + ' '):
            matched += 1
            break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
