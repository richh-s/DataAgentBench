code = """import json

stockinfo_path = locals()['var_functions.query_db:0']
tables_path = locals()['var_functions.query_db:4']

with open(stockinfo_path, 'r') as f:
    stockinfo_data = json.load(f)

with open(tables_path, 'r') as f:
    tables_data = json.load(f)

result = {
    'stockinfo_count': len(stockinfo_data),
    'tables_count': len(tables_data),
    'sample_stockinfo': stockinfo_data[:3],
    'sample_tables': tables_data[:3]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
