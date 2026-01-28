code = """import json
import re

# Access the funding data from storage using locals()
funding_result = locals()['var_functions.query_db:5']
civic_docs_result = locals()['var_functions.query_db:8']

# Parse the funding data (it's a list of dicts)
print('Type of funding_result:', type(funding_result))
print('Funding records count:', len(funding_result))
print('First 3 funding records:')
for i, record in enumerate(funding_result[:3]):
    print(f"  {i+1}. {record['Project_Name']}: ${record['Amount']}")

print('\nType of civic_docs_result:', type(civic_docs_result))
print('Civic docs count:', len(civic_docs_result))
print('First doc keys:', list(civic_docs_result[0].keys()))

# Extract a sample of text to understand structure
sample_text = civic_docs_result[0]['text'][:1000]
print('\nSample text excerpt:')
print(sample_text[:500])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
