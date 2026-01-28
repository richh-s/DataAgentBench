code = """import json
import re

# Access the funding data from storage
funding_data = var_functions.query_db:5

# Access the civic docs data from storage  
civic_docs_data = var_functions.query_db:8

print('Funding records count:', len(funding_data))
print('First 3 funding records:')
for record in funding_data[:3]:
    print(f"  {record['Project_Name']}: ${record['Amount']}")

print('\nCivic docs count:', len(civic_docs_data))
print('First doc keys:', list(civic_docs_data[0].keys()))

# Look at the structure of the text
sample_text = civic_docs_data[0]['text'][:2000]
print('\nFirst ~500 chars of text:')
print(sample_text[:500])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
