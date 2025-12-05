code = """import json, pandas as pd
from pathlib import Path

# Load full NPM release rows
path = Path(var_call_5OrxSyEs6MnaamORRvkWrCoU)
rows = json.loads(path.read_text())

df = pd.DataFrame(rows)
# keep latest per (System, Name) using UpstreamPublishedAt then Version then rn to break ties
latest = df.sort_values(['Name','UpstreamPublishedAt','Version','rn'], ascending=[True, False, False, True])
latest = latest.drop_duplicates(subset=['System','Name'], keep='first')

result = latest[['System','Name','Version']].to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_4BEVO5hAgGcLgquVMr5Bdrhu': ['project_info', 'project_packageversion'], 'var_call_5OrxSyEs6MnaamORRvkWrCoU': 'file_storage/call_5OrxSyEs6MnaamORRvkWrCoU.json'}

exec(code, env_args)
