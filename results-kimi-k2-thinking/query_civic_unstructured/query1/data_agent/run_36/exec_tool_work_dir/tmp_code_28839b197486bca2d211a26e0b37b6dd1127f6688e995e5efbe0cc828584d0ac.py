code = """import json

# Load funding data
funding_file = var_functions.query_db:4
with open(funding_file) as f:
    funding_data = json.load(f)

# Load civic docs
civic_file = var_functions.query_db:28
with open(civic_file) as f:
    civic_docs = json.load(f)

# Filter funding
high_funding = []
for record in funding_data:
    if record.get('Amount'):
        try:
            amount = int(record['Amount'])
            if amount > 50000:
                high_funding.append(record)
        except:
            pass

# Extract design projects (manual list from document review)
capital_design_projects = [
    '2022 Morning View Resurfacing & Storm Drain Improvements',
    'PCH Median Improvements Project',
    'Westward Beach Road Repair Project',
    'Westward Beach Road Drainage Improvements Project',
    'Clover Heights Storm Drainage Improvements',
    'Latigo Canyon Road Retaining Wall Repair Project',
    'Storm Drain Master Plan',
    'Trancas Canyon Park Upper and Lower Slopes Repair',
    'Civic Center Water Treatment Facility Phase 2',
    'Permanent Skate Park',
    'PCH at Trancas Canyon Road Right Turn Lane',
    'Outdoor Warning Signs',
    'Malibu Bluffs Park South Walkway Repairs',
    'Trancas Canyon Park Playground',
    'Malibu Canyon Road Traffic Study'
]

# Match with funding
matches = []
for design in capital_design_projects:
    design_lower = design.lower()
    for fund in high_funding:
        fund_lower = fund['Project_Name'].lower()
        if design_lower in fund_lower or fund_lower in design_lower:
            matches.append(design)
            break

# Additional check for partial matches
for fund in high_funding:
    fund_name = fund['Project_Name'].lower()
    if 'design' in fund_name and any(word in fund_name for word in ['road', 'park', 'drainage', 'bridge', 'storm']):
        if 'capital' in fund_name or 'improvement' in fund_name:
            matches.append(fund['Project_Name'])

# Count unique matches
unique_matches = list(set(matches))

result = {'count': len(unique_matches)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': [{'count': '276'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
