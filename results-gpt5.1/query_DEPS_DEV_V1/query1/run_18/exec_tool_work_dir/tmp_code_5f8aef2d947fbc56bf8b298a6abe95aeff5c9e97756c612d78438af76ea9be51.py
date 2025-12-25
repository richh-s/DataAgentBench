code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_qdDYhlSA9gId2MQwKBE44al4)
rows = json.loads(path.read_text())
df = pd.DataFrame(rows)
# keep only latest release per (System, Name)
df_sorted = df.sort_values(['Name'])
latest = df_sorted.groupby(['System','Name'], as_index=False).first()[['System','Name','Version']]
result = latest.to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_qdDYhlSA9gId2MQwKBE44al4': 'file_storage/call_qdDYhlSA9gId2MQwKBE44al4.json', 'var_call_E0VvRXpxXu3t7daU3kYtYdEK': ['project_info', 'project_packageversion']}

exec(code, env_args)
