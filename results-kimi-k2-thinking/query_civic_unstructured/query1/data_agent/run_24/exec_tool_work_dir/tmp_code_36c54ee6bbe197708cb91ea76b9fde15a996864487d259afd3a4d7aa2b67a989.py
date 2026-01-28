code = """import json

# Load data
funding_file = var_functions.query_db:6
civic_file = var_functions.query_db:5

funding_data = json.load(open(funding_file))
civic_docs = json.load(open(civic_file))

# Get funding > 50k
high_funding_names = set(r['Project_Name'] for r in funding_data if int(r['Amount']) > 50000)

# Extract design projects
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        section = text.split('Capital Improvement Projects (Design)')[1]
        lines = section.split('\n')
        for line in lines[2:100]:
            line = line.strip()
            if line and not line.startswith('(') and not line.startswith('Capital'):
                if 'To:' not in line and 'From:' not in line and len(line) > 5:
                    design_projects.append(line)

# Remove duplicates
design_projects = list(set(design_projects))

# Count matches
matches = 0
for proj in design_projects:
    if proj in high_funding_names:
        matches += 1
    else:
        for fn in high_funding_names:
            if fn.startswith(proj + ' '):
                matches += 1
                break

print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
