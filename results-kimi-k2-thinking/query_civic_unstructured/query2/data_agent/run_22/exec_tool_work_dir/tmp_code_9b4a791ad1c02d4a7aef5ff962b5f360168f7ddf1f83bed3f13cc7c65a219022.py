code = """import json, re

civic_path = '/tmp/tmpnv0h5ejc.json'
funding_path = '/tmp/tmp4h4kth4b.json'

with open(civic_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding_data = json.load(f)

# Extract park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Pattern 1: Look for "Construction was completed" and "2022" near park names
    pattern1 = r'([A-Za-z\s]*Park[A-Za-z\s]*)[^\n]*Construction was completed[^\n]*2022'
    matches = re.finditer(pattern1, text, re.IGNORECASE)
    for m in matches:
        name = m.group(1).strip()
        if name and len(name) < 120 and name not in park_projects:
            park_projects.append(name)

# Also check Broad Beach Road Water Quality Repair mentioned as completed Nov 2022
# This is park-related infrastructure
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Broad Beach Road Water Quality Repair' in text and 'completed' in text.lower() and '2022' in text:
        if 'Broad Beach Road Water Quality Repair' not in park_projects:
            park_projects.append('Broad Beach Road Water Quality Repair')

# Match with funding records
total_funding = 0
matched_records = []

for project in park_projects:
    proj_lower = project.lower()
    
    for fund in funding_data:
        fund_name = fund['Project_Name'].lower()
        
        # Exact match or fund name starts with project name
        if proj_lower == fund_name or fund_name.startswith(proj_lower):
            amount = int(fund['Amount'])
            total_funding += amount
            matched_records.append({
                'project': project,
                'funding_id': fund['Funding_ID'],
                'amount': amount,
                'source': fund['Funding_Source']
            })

result = {
    'total_funding': total_funding,
    'matched_records': len(matched_records),
    'park_projects': park_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
