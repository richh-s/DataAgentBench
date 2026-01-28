code = """import json

# Access the stored results
list_db_result = locals()['var_functions.list_db:0']
author_query_result = locals()['var_functions.query_db:2']

# Print the results to see what we're working with
print('List DB Result:', json.dumps(list_db_result))
print('Author Query Result:', json.dumps(author_query_result))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.query_db:2': [{'author_id': '218'}]}

exec(code, env_args)
