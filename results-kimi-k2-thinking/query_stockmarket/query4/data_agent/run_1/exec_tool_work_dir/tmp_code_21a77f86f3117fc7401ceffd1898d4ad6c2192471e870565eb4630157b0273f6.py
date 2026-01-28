code = """# First check what's stored in the variable
result_var = locals()['var_functions.query_db:0']
print("__RESULT__:")
print(json.dumps({"type": str(type(result_var)), "length": len(str(result_var)) if hasattr(str(result_var), '__len__') else 0, "preview": str(result_var)[:200]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
