code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_bkWkGDC7kj1RleZwsV3M4Bm7)
rows = json.load(open(path))

df = pd.DataFrame(rows)
latest = df.sort_values('Version').drop_duplicates(subset=['System','Name'], keep='last')
latest_npm = latest[latest['System']=='NPM'][['System','Name','Version']]

result = latest_npm.to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_call_bkWkGDC7kj1RleZwsV3M4Bm7': 'file_storage/call_bkWkGDC7kj1RleZwsV3M4Bm7.json', 'var_call_HH8MNcR1jOmEYSt8hJQafXRf': ['project_info', 'project_packageversion']}

exec(code, env_args)
