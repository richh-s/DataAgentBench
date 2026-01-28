code = """import json
import re

# Load funding data
funding_file = 'var_functions.query_db:10_funding.json'
with open('func_response.json', 'r') as f:
    resp = json.load(f)
    funding_path = resp.get('var_functions.query_db:10')
    civic_path = resp.get('var_functions.query_db:11')

# Read funding data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Read civic docs data
with open(civic_path, 'r') as f:
    civic_data = json.load(f)

print(f"Funding records: {len(funding_data)}")
print(f"Civic docs: {len(civic_data)}")
print("Sample funding projects:", [f['Project_Name'] for f in funding_data[:10]])
print("\nSample civic doc text snippet:")
print(civic_data[0]['text'][:1000])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
