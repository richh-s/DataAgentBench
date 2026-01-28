code = """import json
import re

# Access the stored variables using the available keys

# Get funding data
funding_data = var_functions.query_db__0
print('Funding data type:', type(funding_data))
print('Funding records count:', len(funding_data))

# Get civic docs data
civic_docs_data = var_functions.query_db__4
print('Civic docs data type:', type(civic_docs_data)) 
print('Civic docs count:', len(civic_docs_data))

# Show sample data
print('\nSample funding records:')
for i, record in enumerate(funding_data[:5]):
    print(f"  {record['Project_Name']} - {record['Funding_Source']} - ${record['Amount']}")

print('\nSample civic doc:')
print(f"  Filename: {civic_docs_data[0]['filename']}")
print(f"  Text preview: {civic_docs_data[0]['text'][:200]}...")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
