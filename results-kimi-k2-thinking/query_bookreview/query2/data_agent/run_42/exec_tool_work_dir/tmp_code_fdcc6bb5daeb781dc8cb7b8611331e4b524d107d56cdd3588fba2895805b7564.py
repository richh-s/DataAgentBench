code = """import json

books_var = locals()['var_functions.query_db:6']
reviews_var = locals()['var_functions.query_db:8']

result = {'books_type': str(type(books_var)), 'reviews_type': str(type(reviews_var))}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['books_info'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
