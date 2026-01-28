code = """import json
with open(var_call_4YGvoAEJSvPYrXfaQI54NaSp) as f:
    data = json.load(f)
sql = data.get('sql','')
print('__RESULT__:')
print(json.dumps({'sql': sql}))"""

env_args = {'var_call_0OQoxi0RGALCl4N4gLElsShB': 'file_storage/call_0OQoxi0RGALCl4N4gLElsShB.json', 'var_call_XsIeG3HYTleq4ExFbL3Whb4D': 'file_storage/call_XsIeG3HYTleq4ExFbL3Whb4D.json', 'var_call_LqvzNgaZ8GJ70dysxRhpBg4S': {'test': 1}, 'var_call_4YGvoAEJSvPYrXfaQI54NaSp': 'file_storage/call_4YGvoAEJSvPYrXfaQI54NaSp.json'}

exec(code, env_args)
