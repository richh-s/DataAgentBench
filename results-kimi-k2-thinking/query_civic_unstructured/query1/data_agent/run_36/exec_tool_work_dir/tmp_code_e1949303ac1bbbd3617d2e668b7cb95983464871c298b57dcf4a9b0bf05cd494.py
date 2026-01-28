code = """import json, re

# Load data
funding_file = var_functions.query_db:4
with open(funding_file) as f:
    funding_data = json.load(f)

civic_file = var_functions.query_db:28
with open(civic_file) as f:
    civic_docs = json.load(f)

# Get funding > $50,000
high_funding = [f for f in funding_data if f.get('Amount') and int(f['Amount']) > 50000]

# Extract design projects from civic docs
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    # Find design section
    match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Disaster Recovery Projects|$)', text, re.IGNORECASE | re.DOTALL)
    if match:
        section = match.group(1)
        lines = section.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) > 5 and not any(s in line[:20].lower() for s in ['capital', 'design', 'updates', 'project schedule', 'subject', 'cid']):
                if line not in ['•', '●', '■', '□']:
                    design_projects.append(line)

# Match
matches = []
for proj in design_projects:
    proj_lower = proj.lower()
    for fund in high_funding:
        fund_lower = fund['Project_Name'].lower()
        if proj_lower in fund_lower or fund_lower in proj_lower:
            matches.append(proj)
            break

result = {'count': len(set(matches))}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': [{'count': '276'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
