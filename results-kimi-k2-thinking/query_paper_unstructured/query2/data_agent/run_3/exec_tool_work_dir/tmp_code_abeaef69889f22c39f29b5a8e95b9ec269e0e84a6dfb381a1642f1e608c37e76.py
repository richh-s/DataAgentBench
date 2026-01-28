code = """import json

# The result from the query is stored in a variable
# Let's check what we have access to
citations_data = var_functions.query_db:2

print('__RESULT__:')
print(json.dumps(str(type(citations_data))))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
