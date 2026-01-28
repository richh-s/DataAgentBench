code = """import json
# Check available storage variables and their types
vars_list = {k: type(v).__name__ for k,v in globals().items() if k.startswith('var_call_')}
print('__RESULT__:')
print(json.dumps(vars_list))"""

env_args = {'var_call_jzhQseUHxKXVBNdaUVsP8c9e': 'file_storage/call_jzhQseUHxKXVBNdaUVsP8c9e.json', 'var_call_Utur5J9BLQ3n16jKLtshjCae': 'file_storage/call_Utur5J9BLQ3n16jKLtshjCae.json'}

exec(code, env_args)
