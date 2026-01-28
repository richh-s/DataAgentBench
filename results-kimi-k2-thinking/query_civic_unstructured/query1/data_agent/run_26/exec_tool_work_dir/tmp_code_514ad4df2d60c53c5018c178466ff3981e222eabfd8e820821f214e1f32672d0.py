code = """import json

# Load funding data (> $50K)
funding_file = var_functions.query_db:0
civic_file = var_functions.query_db:20

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Build funded projects dict
funded = {}
for rec in funding_data:
    funded[rec['Project_Name'].lower()] = int(rec['Amount'])

# Parse design projects
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            design_part = parts[1].split('Capital Improvement Projects (Construction)')[0]
            lines = [l.strip() for l in design_part.split('\n') if l.strip()]
            for line in lines:
                if len(line) > 5 and '▪' not in line and 'Updates:' not in line and 'Project Schedule:' not in line and 'Page' not in line and 'RECOMMENDED' not in line and 'DISCUSSION' not in line:
                    design_projects.append(line)

# Count matches
count = 0
for proj in design_projects:
    proj_lower = proj.lower()
    if proj_lower in funded and funded[proj_lower] > 50000:
        count += 1

print('__RESULT__:')
print(json.dumps({'design_capital_projects': len(set(design_projects)), 'count_with_funding_over_50000': count}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
