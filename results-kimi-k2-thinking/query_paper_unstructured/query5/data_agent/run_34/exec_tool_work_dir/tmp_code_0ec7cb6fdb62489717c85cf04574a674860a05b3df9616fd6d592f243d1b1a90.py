code = """temp_var = "var_functions.query_db:2"
papers_data_key = temp_var.replace(".", "_").replace(":", "_")
print("__RESULT__:")
print(papers_data_key)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
