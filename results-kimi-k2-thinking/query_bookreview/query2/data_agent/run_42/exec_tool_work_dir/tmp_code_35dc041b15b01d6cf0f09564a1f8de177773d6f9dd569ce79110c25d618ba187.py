code = """import json

with open(var_functions.query_db:6, 'r') as f:
    books_data = json.load(f)

with open(var_functions.query_db:8, 'r') as f:
    reviews_data = json.load(f)

print('Books loaded:', len(books_data))
print('Reviews loaded:', len(reviews_data))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['books_info'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
