code = """import json

# Access the stored results from previous queries
civic_docs_result = var_functions.query_db:50
funding_result = var_functions.query_db:60

print('Types:')
print(f'civic_docs_result type: {type(civic_docs_result)}')
print(f'funding_result type: {type(funding_result)}')

# If these are file paths, load them
if isinstance(civic_docs_result, str) and '.json' in civic_docs_result:
    with open(civic_docs_result, 'r') as f:
        civic_docs = json.load(f)
    print(f'Loaded {len(civic_docs)} civic documents')
else:
    civic_docs = civic_docs_result if isinstance(civic_docs_result, list) else []

if isinstance(funding_result, str) and '.json' in funding_result:
    with open(funding_result, 'r') as f:
        funding_data = json.load(f)
    print(f'Loaded {len(funding_data)} funding records')
else:
    funding_data = funding_result if isinstance(funding_result, list) else []

# Show first record of each
if civic_docs:
    print(f'\nFirst civic doc keys: {list(civic_docs[0].keys())}')
    print(f'First civic doc filename: {civic_docs[0].get("filename")}')

if funding_data:
    print(f'\nFirst funding record: {funding_data[0]}')

result = {'civic_docs': len(civic_docs), 'funding_records': len(funding_data)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': {'var_functions.list_db:0': "<class 'list'>", 'var_functions.query_db:2': "<class 'str'>", 'var_functions.query_db:4': "<class 'str'>"}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:52': [{'count': '500', 'total_amount': '28094000'}], 'var_functions.list_db:56': ['civic_docs'], 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
