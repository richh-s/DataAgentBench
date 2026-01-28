code = """# Check all available variables
all_vars = [k for k in locals().keys() if not k.startswith('__')]
print('Available variables:', all_vars[:10])  # First 10 to avoid clutter

# Look for query-related variables
query_vars = [k for k in all_vars if 'query' in str(k)]
print('Query variables:', query_vars)

# Let's directly reference the likely variable names
cpc_var_name = 'var_functions.query_db_26'
level5_var_name = 'var_functions.query_db_28'

print(f'CPC var exists: {cpc_var_name in all_vars}')
print(f'Level5 var exists: {level5_var_name in all_vars}')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
