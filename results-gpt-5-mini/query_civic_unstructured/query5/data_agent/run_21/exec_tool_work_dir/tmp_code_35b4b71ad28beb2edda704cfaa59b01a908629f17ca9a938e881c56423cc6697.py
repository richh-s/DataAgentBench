code = """import json
print("__RESULT__:")
print(json.dumps({"v1": type(var_call_eA0xJZWygM8q62BlCiIPmWwv).__name__, "v2": type(var_call_CVAV72xeKdGMECzEU9GvpR7x).__name__}))"""

env_args = {'var_call_9m8TflfbCJWo96QQhMCIesyq': ['civic_docs'], 'var_call_eA0xJZWygM8q62BlCiIPmWwv': 'file_storage/call_eA0xJZWygM8q62BlCiIPmWwv.json', 'var_call_81lfzMGYLNjxzefeEW7o1uY3': ['Funding'], 'var_call_CVAV72xeKdGMECzEU9GvpR7x': 'file_storage/call_CVAV72xeKdGMECzEU9GvpR7x.json'}

exec(code, env_args)
