code = """import json

# Debug what's available
print("Debugging variable access...")
available = [name for name in dir() if 'query_db' in name]
print("Available query_db vars:", available)

# Try accessing directly
print("mongo result type:", type(var_functions.query_db:2))
print("funding result type:", type(var_functions.query_db:6))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
