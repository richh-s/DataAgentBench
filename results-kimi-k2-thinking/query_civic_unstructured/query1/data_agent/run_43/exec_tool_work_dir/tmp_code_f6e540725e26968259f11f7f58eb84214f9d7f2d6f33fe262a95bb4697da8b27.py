code = """import json

# Load funding data
with open(var_functions.query_db:5) as f:
    funding = json.load(f)

# Load civic documents
with open(var_functions.query_db:6) as f:
    docs = json.load(f)

# Count funding records > 50000
large_funding = [item for item in funding if int(item['Amount']) > 50000]

# Process civic documents - find capital design projects
design_project_names = set()
for doc in docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text:
        for line in text.split('\n'):
            line = line.strip()
            if len(line) > 5 and not line.startswith('Page'):
                design_project_names.add(line.replace('• ', ''))

# Build funding lookup
funding_lookup = {item['Project_Name']: int(item['Amount']) for item in large_funding}

# Match and count
count = 0
for design in design_project_names:
    for funded in funding_lookup:
        if design.lower() in funded.lower() or funded.lower() in design.lower():
            if abs(len(design) - len(funded)) < 40:
                count += 1
                break

print('__RESULT__:')
print(json.dumps({'count_final': count, 'design_projects_total': len(design_project_names), 'large_funding_total': len(large_funding)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
