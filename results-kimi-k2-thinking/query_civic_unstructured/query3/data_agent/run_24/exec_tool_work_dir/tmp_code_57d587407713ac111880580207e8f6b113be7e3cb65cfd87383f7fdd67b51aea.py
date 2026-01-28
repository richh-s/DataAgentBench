code = """import json

# Load funding data
funding_file = var_functions.query_db:18
print('Loading funding from:', funding_file)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print('Funding records:', len(funding_data))

# Show sample funding records
print('\nSample funding records:')
for i in range(5):
    if i < len(funding_data):
        rec = funding_data[i]
        print(f"Project: {rec['Project_Name'][:50]} | Source: {rec['Funding_Source']} | Amount: {rec['Amount']}")

# Filter for FEMA/emergency related funding
fema_emergency_funding = []
for rec in funding_data:
    proj_name = rec['Project_Name'].lower()
    if 'fema' in proj_name or 'emergency' in proj_name:
        fema_emergency_funding.append({
            'Project_Name': rec['Project_Name'],
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount'])
        })

print(f'\nFound {len(fema_emergency_funding)} FEMA/emergency funding records')
print('\nFEMA/Emergency funding:')
for rec in fema_emergency_funding[:10]:
    print(f"- {rec['Project_Name'][:50]} | ${rec['Amount']:,} | {rec['Funding_Source']}")

# Also check for projects that might be disaster recovery
potential_disaster = []
for rec in funding_data:
    proj_name = rec['Project_Name'].lower()
    if 'fema' in proj_name or 'emergency' in proj_name or 'oise' in proj_name or 'oia' in proj_name:
        potential_disaster.append(rec)

print(f'\nTotal potential disaster/emergency projects: {len(potential_disaster)}')

result = {
    'fema_emergency_funding': fema_emergency_funding,
    'potential_disaster_count': len(potential_disaster)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
