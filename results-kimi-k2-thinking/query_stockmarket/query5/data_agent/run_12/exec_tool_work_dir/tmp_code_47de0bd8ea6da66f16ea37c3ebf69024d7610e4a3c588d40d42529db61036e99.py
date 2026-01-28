code = """import json

# Check the types and first few items of the stored results
nasdaq_cap_symbols = locals()['var_functions.query_db:0']
available_tables = locals()['var_functions.list_db:2']

print('__RESULT__:')
print(json.dumps({
    'nasdaq_cap_type': str(type(nasdaq_cap_symbols)),
    'nasdaq_cap_len': len(nasdaq_cap_symbols) if hasattr(nasdaq_cap_symbols, '__len__') else 'N/A',
    'nasdaq_cap_sample': str(nasdaq_cap_symbols[:200]) if isinstance(nasdaq_cap_symbols, str) else nasdaq_cap_symbols[:3],
    'available_tables_type': str(type(available_tables)),
    'available_tables_len': len(available_tables) if hasattr(available_tables, '__len__') else 'N/A',
    'available_tables_sample': str(available_tables[:200]) if isinstance(available_tables, str) else available_tables[:3]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
