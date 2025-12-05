code = """import json, pandas as pd
from pathlib import Path

file_path = Path(var_call_MAtCDUrvf8tmzLFUrkv05Meq)
data = json.loads(file_path.read_text())

df = pd.DataFrame(data)

df['vi'] = df['VersionInfo'].apply(json.loads)
filtered = df[(df['vi'].apply(lambda x: x.get('IsRelease', False))) & df['Licenses'].str.contains('"MIT"', regex=False)]

result = filtered[['System','Name','Version']].drop_duplicates().to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_MAtCDUrvf8tmzLFUrkv05Meq': 'file_storage/call_MAtCDUrvf8tmzLFUrkv05Meq.json', 'var_call_5ktSNeYNX6BbEDqQ1dg9FYzg': ['project_info', 'project_packageversion']}

exec(code, env_args)
