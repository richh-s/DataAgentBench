code = """import json
print("__RESULT__:")
print(json.dumps({"test":1}))"""

env_args = {'var_call_0OQoxi0RGALCl4N4gLElsShB': 'file_storage/call_0OQoxi0RGALCl4N4gLElsShB.json', 'var_call_XsIeG3HYTleq4ExFbL3Whb4D': 'file_storage/call_XsIeG3HYTleq4ExFbL3Whb4D.json'}

exec(code, env_args)
