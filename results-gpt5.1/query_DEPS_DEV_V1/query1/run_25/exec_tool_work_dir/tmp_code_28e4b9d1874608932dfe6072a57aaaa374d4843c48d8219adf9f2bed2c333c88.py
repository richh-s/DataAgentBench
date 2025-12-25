code = """import pandas as pd, json
import os

path = var_call_B2DybEJRJEJVmKVztz8A2BIF
with open(path) as f:
    data = json.load(f)

df = pd.DataFrame(data)
# keep only latest version per Name using VersionInfo if available later, but we only have Version here.
# Assume lexical max Version is latest.
latest = df.sort_values('Version').drop_duplicates(['System','Name'], keep='last')
latest = latest[latest['System']=='NPM'][['System','Name','Version']]

result = latest.to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_B2DybEJRJEJVmKVztz8A2BIF': 'file_storage/call_B2DybEJRJEJVmKVztz8A2BIF.json', 'var_call_lFVYvaUDRjkxTW2shNUSEEFW': ['project_info', 'project_packageversion']}

exec(code, env_args)
