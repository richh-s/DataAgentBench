code = """print("__RESULT__:")
print(locals().get('var_function-call-8192239243877575471'))"""

env_args = {'var_function-call-8192239243877575471': 'file_storage/function-call-8192239243877575471.json'}

exec(code, env_args)
