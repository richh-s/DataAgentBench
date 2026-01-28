code = """import json

# Load data from files
civic_docs = json.load(open(var_functions.query_db:50))
funding = json.load(open(var_functions.query_db:60))

# Show data structure
print(f'Civic docs: {len(civic_docs)} documents')
print(f'Funding records: {len(funding)} records')
print(f'First civic doc keys: {list(civic_docs[0].keys()) if civic_docs else "None"}')
print(f'First funding record: {funding[0] if funding else "None"}')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': {'var_functions.list_db:0': "<class 'list'>", 'var_functions.query_db:2': "<class 'str'>", 'var_functions.query_db:4': "<class 'str'>"}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:52': [{'count': '500', 'total_amount': '28094000'}], 'var_functions.list_db:56': ['civic_docs'], 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
