code = """import json, re

# Read data from files
funding_path = locals()['var_functions.query_db:6']
civic_path = locals()['var_functions.query_db:5']

with open(funding_path) as f:
    funding = json.load(f)

with open(civic_path) as f:
    civic_docs = json.load(f)

# Filter funding > 50k
high_funding = [r for r in funding if int(r['Amount']) > 50000]
high_funding_names = set(r['Project_Name'] for r in high_funding)

# Extract design capital projects
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for design section
    if 'Capital Improvement Projects (Design)' in text:
        # Extract all sections that list projects
        blocks = text.split('Capital Improvement Projects (Design)')[1:]
        for block in blocks:
            # Split by lines and identify project names
            lines = block.split('\n')
            in_projects = False
            for line in lines:
                line = line.strip()
                if line and not line.startswith('Capital Improvement Projects') and not line.startswith('(') and len(line) > 10:
                    # Heuristic: project names tend to be title-like without certain keywords
                    if not any(kw in line.lower() for kw in ['to:', 'from:', 'date:', 'subject:', 'recommended', 'action', 'discussion']):
                        design_projects.append(line)

# Remove duplicates
design_projects = list(set(design_projects))

# Match with funding
matches = 0
for dp in design_projects:
    for hf in high_funding:
        if dp == hf['Project_Name'] or hf['Project_Name'].startswith(dp + ' '):
            matches += 1
            break

print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
