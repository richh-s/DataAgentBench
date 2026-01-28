code = """import json
out = {"ok": True}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Bwf6IfMILxz6M6L9VEXSIh1T': 'file_storage/call_Bwf6IfMILxz6M6L9VEXSIh1T.json', 'var_call_fzLKq8IlpgPul9fghWeKKYUT': 'file_storage/call_fzLKq8IlpgPul9fghWeKKYUT.json'}

exec(code, env_args)
