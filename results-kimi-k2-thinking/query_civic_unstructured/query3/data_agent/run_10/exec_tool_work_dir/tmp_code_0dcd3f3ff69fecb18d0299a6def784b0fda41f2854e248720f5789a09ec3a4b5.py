code = """import json
import re

# Load funding data
with open('funding_data.json', 'r') as f:
    funding_data = json.load(f)

# Load civic docs data
with open('civic_docs_emergency_fema.json', 'r') as f:
    civic_docs_data = json.load(f)

print('Funding records count:', len(funding_data))
print('Civic docs count:', len(civic_docs_data))

# Show some sample funding records
print('\nSample funding records:')
for i, record in enumerate(funding_data[:5]):
    print(f"{i+1}. {record['Project_Name']} - {record['Funding_Source']} - ${record['Amount']}")

# Show some sample civic docs
print('\nSample civic docs:')
for i, doc in enumerate(civic_docs_data[:2]):
    print(f"\nDoc {i+1}: {doc['filename']}")
    print(f"Text preview: {doc['text'][:500]}...")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
