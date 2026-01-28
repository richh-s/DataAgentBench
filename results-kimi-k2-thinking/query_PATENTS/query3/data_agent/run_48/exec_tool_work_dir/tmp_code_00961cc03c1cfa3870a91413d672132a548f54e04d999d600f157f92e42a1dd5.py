code = """import json

# Access the stored result
result_key = 'var_functions.query_db:2'
result_var = locals()[result_key]

print(f"Type of result_var: {type(result_var)}")
print(f"Value of result_var: {str(result_var)[:200]}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
