code = """path = locals().get('var_function-call-7498192109235549923')
print(f"Type: {type(path)}")
print(f"Value: {path}")
print("__RESULT__:")
print("done")"""

env_args = {'var_function-call-7498192109235549923': 'file_storage/function-call-7498192109235549923.json'}

exec(code, env_args)
