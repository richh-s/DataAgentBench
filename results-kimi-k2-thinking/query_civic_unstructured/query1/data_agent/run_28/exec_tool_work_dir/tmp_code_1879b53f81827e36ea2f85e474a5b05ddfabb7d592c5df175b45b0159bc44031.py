code = """import json
import re

# Access the results from storage using the variable names provided
funding_data = var_functions_query_db_5
civic_docs_data = var_functions_query_db_8

# Check the funding data
print('Funding records count:', len(funding_data))
print('First 3 funding records:')
for i, record in enumerate(funding_data[:3]):
    print(f"  {i+1}. {record['Project_Name']}: ${record['Amount']}")

# Check the civic docs data  
print('\nCivic docs count:', len(civic_docs_data))
print('First doc keys:', list(civic_docs_data[0].keys()))

# Extract sample text to see structure
sample_text = civic_docs_data[0]['text']
print('\nSample text excerpt (first 500 chars):')
print(sample_text[:500])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
