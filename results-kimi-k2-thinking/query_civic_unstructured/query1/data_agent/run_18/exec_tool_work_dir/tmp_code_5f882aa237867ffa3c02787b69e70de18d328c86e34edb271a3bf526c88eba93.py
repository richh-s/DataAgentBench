code = """import json
import re

# Load funding data from file
funding_path = var_functions.query_db_120
with open(funding_path) as f:
    funding_data = json.load(f)

# Load civic documents from file  
civic_path = var_functions.query_db_121
with open(civic_path) as f:
    civic_docs = json.load(f)

# Get list of funded project names
funded_names = [item['Project_Name'] for item in funding_data]

print('Funding projects loaded:', len(funded_names))
print('Civic docs loaded:', len(civic_docs))

# Show first few funded names
print('Sample funded projects:', funded_names[:5])

result = {'funding_count': len(funded_names), 'civic_count': len(civic_docs)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:51': 'file_storage/functions.query_db:51.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.list_db:90': ['Funding'], 'var_functions.list_db:91': ['civic_docs'], 'var_functions.execute_python:96': {'funding_count': 276, 'civic_count': 5}, 'var_functions.query_db:102': [{'count': '276'}], 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:106': 'file_storage/functions.query_db:106.json', 'var_functions.query_db:107': 'file_storage/functions.query_db:107.json', 'var_functions.query_db:110': 'file_storage/functions.query_db:110.json', 'var_functions.query_db:111': 'file_storage/functions.query_db:111.json', 'var_functions.query_db:114': 'file_storage/functions.query_db:114.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json', 'var_functions.query_db:117': 'file_storage/functions.query_db:117.json', 'var_functions.query_db:120': 'file_storage/functions.query_db:120.json', 'var_functions.query_db:121': 'file_storage/functions.query_db:121.json'}

exec(code, env_args)
