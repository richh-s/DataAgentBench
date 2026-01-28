code = """import json

# Access funding data directly from storage
funding_info = locals()['var_functions.query_db:5']
civic_info = locals()['var_functions.query_db:12']

print('__RESULT__:')
print(json.dumps({
    'funding_type': str(type(funding_info)),
    'civic_type': str(type(civic_info)),
    'funding_length': len(str(funding_info)),
    'civic_length': len(str(civic_info))
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
