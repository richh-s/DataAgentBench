code = """import json

# Access the stored result
result_key = 'var_functions.query_db:2'
result_var = locals()[result_key]

output = f"Type: {type(result_var)}\nValue: {str(result_var)[:300]}"

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
