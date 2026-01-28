code = """import json, os, re

# Load funding data
funding_path = locals().get('var_functions.query_db:12')
with open(funding_path) as f:
    funding = json.load(f)

# Load civic documents
civic_path = locals().get('var_functions.query_db:14')
with open(civic_path) as f:
    civic_docs = json.load(f)

print(f'Funding records: {len(funding)}')
print(f'Civic documents: {len(civic_docs)}')

# Identify disaster-related projects from funding names (those with FEMA/CalOES/CalJPIA)
disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'recovery', 'fire']
disaster_funding = []

for record in funding:
    name_lower = record['Project_Name'].lower()
    if any(keyword in name_lower for keyword in disaster_keywords):
        disaster_funding.append(record)

print(f'Potential disaster funding records: {len(disaster_funding)}')

# Show a few examples
print('Sample disaster projects:')
for rec in disaster_funding[:10]:
    print(f"- {rec['Project_Name']}: ${rec['Amount']}")

print('__RESULT__:')
print(json.dumps({
    'funding_total': len(funding),
    'civic_docs_total': len(civic_docs),
    'disaster_funding_count': len(disaster_funding)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': {'success': True, 'num_docs': 5}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
