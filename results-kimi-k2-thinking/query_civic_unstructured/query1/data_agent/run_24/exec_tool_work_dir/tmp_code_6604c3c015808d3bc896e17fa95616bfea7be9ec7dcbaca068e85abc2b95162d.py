code = """import json

# Get file paths
funding_file = locals()['var_functions.query_db:6']
civic_file = locals()['var_functions.query_db:5']

# Read data
with open(funding_file) as f:
    funding = json.load(f)

with open(civic_file) as f:
    civic_docs = json.load(f)

# Filter funding > 50k
funding_names = set(r['Project_Name'] for r in funding if int(r['Amount']) > 50000)

design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        parts = text.split('Capital Improvement Projects (Design)', 1)[1]
        for line in parts.split('\n')[2:10]:
            line = line.strip()
            if line and not line.startswith('(') and not line.startswith('Capital'):
                if 'To:' not in line and 'From:' not in line:
                    design_projects.append(line)

# Remove duplicates
design_projects = list(set(design_projects))

# Count matches
match_count = 0
for proj in design_projects:
    if proj in funding_names or any(fn.startswith(proj + ' ') for fn in funding_names):
        match_count += 1

print('__RESULT__:')
print(json.dumps(match_count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
