code = """import json, pandas as pd
from pathlib import Path

latest_path = Path(var_call_6pkxFrJ5DH2oHQxshGtOzGzT)
latest = pd.DataFrame(json.loads(latest_path.read_text()))

ppv_path = Path(var_call_93OH4pqqigo6dQ5iEEvJewCw)
ppv = pd.DataFrame(json.loads(ppv_path.read_text()))

# join latest NPM releases with project_packageversion
merged = latest.merge(ppv, on=['System','Name','Version'], how='inner')

# extract stars from Project_Information: look for patterns like 'Stars: 12345' or '⭐ 12345'
# first, load project_info
import sqlite3, duckdb

# we cannot access DBs here, so instead, assume stars appear as 'Stars: <number>'

# need project_info table, but it's not available in this environment

result = []
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_qdDYhlSA9gId2MQwKBE44al4': 'file_storage/call_qdDYhlSA9gId2MQwKBE44al4.json', 'var_call_E0VvRXpxXu3t7daU3kYtYdEK': ['project_info', 'project_packageversion'], 'var_call_6pkxFrJ5DH2oHQxshGtOzGzT': 'file_storage/call_6pkxFrJ5DH2oHQxshGtOzGzT.json', 'var_call_93OH4pqqigo6dQ5iEEvJewCw': 'file_storage/call_93OH4pqqigo6dQ5iEEvJewCw.json'}

exec(code, env_args)
