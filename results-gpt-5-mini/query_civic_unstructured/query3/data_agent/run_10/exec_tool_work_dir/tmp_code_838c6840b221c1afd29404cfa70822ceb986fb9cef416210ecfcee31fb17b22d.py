code = """import json

print('__RESULT__:')
print(json.dumps({'var1_type': type(var_call_lzuql9XO4mip4vcz5jSfIR6d).__name__, 'var2_type': type(var_call_OTWLMZF2U2vjKkDgiSiAfRbv).__name__}))"""

env_args = {'var_call_OTWLMZF2U2vjKkDgiSiAfRbv': 'file_storage/call_OTWLMZF2U2vjKkDgiSiAfRbv.json', 'var_call_lzuql9XO4mip4vcz5jSfIR6d': 'file_storage/call_lzuql9XO4mip4vcz5jSfIR6d.json'}

exec(code, env_args)
