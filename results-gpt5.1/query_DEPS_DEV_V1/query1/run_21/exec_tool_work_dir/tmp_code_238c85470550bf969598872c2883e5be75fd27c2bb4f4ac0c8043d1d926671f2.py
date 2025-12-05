code = """import json, pandas as pd, os
from itertools import groupby

path = var_call_jjj8X2PBEdMvJqjdKtB1SLHz
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# sort by Name, UpstreamPublishedAt desc isn't present, so just keep first occurrence per Name assuming it's latest due to query order
latest = df.drop_duplicates(subset=['Name'], keep='first')
latest_npm = latest[['System','Name','Version']]
result = latest_npm.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jjj8X2PBEdMvJqjdKtB1SLHz': 'file_storage/call_jjj8X2PBEdMvJqjdKtB1SLHz.json', 'var_call_fIlM10O9K2O4WChXcOhhBjv9': ['project_info', 'project_packageversion']}

exec(code, env_args)
