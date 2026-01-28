code = """import json
# Access results from storage
stockinfo_data = locals()['var_functions.query_db:2']
stocktables_data = locals()['var_functions.list_db:5']

print('__RESULT__:')
print(json.dumps({
    'stockinfo_type': str(type(stockinfo_data)),
    'stockinfo_length': len(stockinfo_data) if isinstance(stockinfo_data, list) else 0,
    'stocktables_type': str(type(stocktables_data)),
    'stocktables_length': len(stocktables_data) if isinstance(stocktables_data, list) else 0,
    'stockinfo_sample': stockinfo_data[:2] if isinstance(stockinfo_data, list) else None,
    'stocktables_sample': stocktables_data[:2] if isinstance(stocktables_data, list) else None
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:5']}

exec(code, env_args)
