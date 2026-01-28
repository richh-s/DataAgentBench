code = """# Check the type and content of the stored results
nyse_stocks_data = locals()['var_functions.query_db:0']
available_tables_data = locals()['var_functions.list_db:2']

print('__RESULT__:')
print({
    'nyse_stocks_type': str(type(nyse_stocks_data)),
    'available_tables_type': str(type(available_tables_data)),
    'nyse_stocks_preview': str(nyse_stocks_data)[:200] if isinstance(nyse_stocks_data, str) else 'Not a string',
    'available_tables_preview': str(available_tables_data)[:200] if isinstance(available_tables_data, str) else 'Not a string'
})"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
