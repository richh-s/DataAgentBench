code = """import json, pandas as pd
path = var_call_ihWrHeK6Dx4zWUpc34rvCaiX
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
latest = df.sort_values('Version').drop_duplicates(subset=['Name'], keep='last')
result = latest[['Name','Version']].to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_ihWrHeK6Dx4zWUpc34rvCaiX': 'file_storage/call_ihWrHeK6Dx4zWUpc34rvCaiX.json', 'var_call_EG9snxTVWGRTx2lcll9tAiWt': ['project_info', 'project_packageversion'], 'var_call_SIb6qL46UP70DZFfFGqS3byq': 'file_storage/call_SIb6qL46UP70DZFfFGqS3byq.json'}

exec(code, env_args)
