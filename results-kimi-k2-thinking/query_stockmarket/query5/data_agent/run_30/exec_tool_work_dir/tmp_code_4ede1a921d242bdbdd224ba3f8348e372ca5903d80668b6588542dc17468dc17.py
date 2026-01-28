code = """# Read the result file from the first query
result_key = 'var_functions.query_db:0'
result_file = locals()[result_key]

# For now, let's just check what we have
print('__RESULT__:')
print(result_file)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
