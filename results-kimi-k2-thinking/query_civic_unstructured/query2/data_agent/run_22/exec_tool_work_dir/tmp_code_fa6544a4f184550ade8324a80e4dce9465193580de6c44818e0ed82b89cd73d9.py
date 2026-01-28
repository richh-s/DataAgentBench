code = """import json

civic_path = var_functions.query_db_6
funding_path = var_functions.query_db_8

with open(civic_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding_data = json.load(f)

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Check if document mentions park and 2022 completion
    if 'Park' in text and 'completed' in text.lower() and '2022' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Look for lines with Park that are likely project names
            if 'Park' in line and len(line) < 100:
                # Skip metadata lines
                if 'updates' not in line.lower() and 'schedule' not in line.lower():
                    if line not in park_projects:
                        park_projects.append(line)

# Match with funding records
matched_amounts = []
for project in park_projects:
    proj_lower = project.lower()
    for fund in funding_data:
        fund_name = fund['Project_Name'].lower()
        # Simple name matching
        if proj_lower == fund_name or fund_name.startswith(proj_lower):
            matched_amounts.append(int(fund['Amount']))

total = sum(matched_amounts)
result = {'total_funding': total, 'park_projects': len(park_projects), 'funding_matches': len(matched_amounts)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
