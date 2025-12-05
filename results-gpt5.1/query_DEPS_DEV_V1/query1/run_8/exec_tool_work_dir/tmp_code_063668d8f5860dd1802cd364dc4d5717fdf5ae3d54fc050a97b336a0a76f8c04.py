code = """import json, pandas as pd
from pathlib import Path

file1 = Path(var_call_4oyI9xuUANUktpGYGKXBOECD)
file2 = Path(var_call_YJfHpRk4tzC33Fei8Tj15eFr)

data1 = json.loads(file1.read_text())
data2 = json.loads(file2.read_text())

df_pkg = pd.DataFrame(data1)
# keep only release versions and pick max Ordinal per (System, Name)
df_pkg['Ordinal'] = df_pkg['VersionInfo'].apply(lambda s: json.loads(s)['Ordinal'])
df_pkg['IsRelease'] = df_pkg['VersionInfo'].apply(lambda s: json.loads(s)['IsRelease'])

latest_release = df_pkg[df_pkg['IsRelease']].sort_values('Ordinal').groupby(['System','Name'], as_index=False).tail(1)[['System','Name','Version']]

# join with project_packageversion on System,Name,Version
proj = pd.DataFrame(data2)[['System','Name','Version','ProjectName']].drop_duplicates()
merged = latest_release.merge(proj, on=['System','Name','Version'], how='inner')

result = merged.to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_call_4oyI9xuUANUktpGYGKXBOECD': 'file_storage/call_4oyI9xuUANUktpGYGKXBOECD.json', 'var_call_YJfHpRk4tzC33Fei8Tj15eFr': 'file_storage/call_YJfHpRk4tzC33Fei8Tj15eFr.json'}

exec(code, env_args)
