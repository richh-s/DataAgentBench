code = """import json

# Access the storage variables correctly
books_result = locals().get('var_functions.query_db:6')
reviews_result = locals().get('var_functions.query_db:8')
print('Books result type:', type(books_result))
print('Reviews result type:', type(reviews_result))
print('Books result (first 200 chars):', str(books_result)[:200])
print('Reviews result (first 200 chars):', str(reviews_result)[:200])"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['books_info'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
