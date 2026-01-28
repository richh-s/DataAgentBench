code = """import json

# Load all data
funding_path = var_functions.query_db:6
civic_path = var_functions.query_db:5

with open(funding_path) as f:
    funding = json.load(f)

with open(civic_path) as f:
    civic_docs = json.load(f)

# Step 1: Get funding amounts > 50000
high_funding = []
for r in funding:
    if int(r['Amount']) > 50000:
        high_funding.append(r)

funding_names = set(x['Project_Name'] for x in high_funding)

# Step 2: Extract design projects from civic documents
design_proj = []
for doc in civic_docs:
    if 'Capital Improvement Projects (Design)' in doc.get('text', ''):
        txt = doc['text']
        parts = txt.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            section = parts[1]
            # Get first 50 lines of this section
            lines = section.split('\n')[2:50]
            for line in lines:
                line = line.strip()
                if line and not line.startswith('(') and ':' not in line:
                    if 'To:' not in line and 'From:' not in line and 'Date' not in line:
                        design_proj.append(line)

# Remove duplicates
design_proj = list(set(design_proj))

# Step 3: Count matches
matches = 0
for proj in design_proj:
    for fund in funding_names:
        if proj == fund or fund.startswith(proj + ' '):
            matches += 1
            break

print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
