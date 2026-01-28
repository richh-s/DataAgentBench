code = """import json, os

# Load civic documents
civic_path = 'var_functions.query_db:20'
funding_path = 'var_functions.query_db:5'

with open(civic_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding_recs = json.load(f)

# Build funding map
funding = {}
for rec in funding_recs:
    funding[rec['Project_Name']] = int(rec['Amount'])

# Find park projects completed in 2022
projects = []

for doc in civic_docs:
    lines = doc['text'].splitlines()
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) > 10 and ('park' in line.lower() or 'playground' in line.lower()):
            # Check context
            start = max(0, i-8)
            end = min(len(lines), i+10)
            ctx = ' '.join(lines[start:end]).lower()
            if 'completed' in ctx and '2022' in ctx:
                clean = line.replace('(cid:190)', '').replace('(cid:131)', '').strip()
                projects.append(clean)

# Remove duplicates
unique = list(set(projects))

# Calculate funding
total = 0
for proj in unique:
    if proj in funding:
        total += funding[proj]
    else:
        # Partial match
        for funded in funding:
            if proj.lower() in funded.lower():
                total += funding[funded]
                break

result = '$' + str(total)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
