code = """import json

# Read the query results from the file
with open('var_functions.query_db:2', 'r') as f:
    data = json.load(f)

# Check the structure of CPC codes
sample_cpc = data[0]['cpc']
print('Sample CPC field:', sample_cpc[:200])

# Parse it as JSON
import ast
cpc_list = ast.literal_eval(sample_cpc)
print('\nFirst CPC entry:', cpc_list[0] if cpc_list else 'No CPC')
print('Sample CPC codes:', [item['code'] for item in cpc_list[:3]] if cpc_list else 'None')

# Check grant dates
print('\nSample grant dates:')
for i in range(min(5, len(data))):
    print(f"  {i+1}. {data[i]['grant_date']}")

# Check patents_info for country codes
print('\nSample patents_info:')
for i in range(min(5, len(data))):
    print(f"  {i+1}. {data[i]['Patents_info'][:100]}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
