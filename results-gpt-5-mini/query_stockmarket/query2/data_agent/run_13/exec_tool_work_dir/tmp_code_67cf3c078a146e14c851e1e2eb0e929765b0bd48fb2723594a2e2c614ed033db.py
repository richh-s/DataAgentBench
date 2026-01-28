code = """import json
etf_path = var_call_Jmo2Rsfw5M21fWP4GV1aAB4V
tables_path = var_call_0iEfjRTHDhO80I1pTTWbbo9M
with open(etf_path, 'r') as f:
    etfs = json.load(f)
with open(tables_path, 'r') as f:
    tabs = json.load(f)
common = [s for s in etfs if s in tabs]
print('__RESULT__:')
print(json.dumps(common))"""

env_args = {'var_call_gCLBSTPQ665qBJjIJTfQJYcH': 'file_storage/call_gCLBSTPQ665qBJjIJTfQJYcH.json', 'var_call_Jmo2Rsfw5M21fWP4GV1aAB4V': 'file_storage/call_Jmo2Rsfw5M21fWP4GV1aAB4V.json', 'var_call_0iEfjRTHDhO80I1pTTWbbo9M': 'file_storage/call_0iEfjRTHDhO80I1pTTWbbo9M.json'}

exec(code, env_args)
