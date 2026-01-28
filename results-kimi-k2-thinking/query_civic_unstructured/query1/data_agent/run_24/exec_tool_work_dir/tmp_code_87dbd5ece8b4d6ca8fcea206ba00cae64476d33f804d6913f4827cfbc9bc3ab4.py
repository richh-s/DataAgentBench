code = """import json

# Load data files
with open(var_functions.query_db:6) as f:
    funding = json.load(f)

with open(var_functions.query_db:5) as f:
    civic_docs = json.load(f)

# Get funding records > $50,000
funding_over_50k = [r for r in funding if int(r['Amount']) > 50000]

# Extract design status capital projects from civic documents
design_capital = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    parts = text.split('Capital Improvement Projects (Design)')
    if len(parts) > 1:
        section = parts[1]
        for line in section.split('\n'):
            line = line.strip()
            if line and not line.startswith('(') and not line.startswith('Capital'):
                if 'To:' not in line and 'From:' not in line and len(line) > 5:
                    design_capital.append(line)

# Remove duplicates
design_capital = list(set(design_capital))

# Count matches
matched = 0
for proj in design_capital:
    for fund in funding_over_50k:
        fund_name = fund['Project_Name']
        if proj == fund_name or fund_name.startswith(proj + ' '):
            matched += 1
            break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
