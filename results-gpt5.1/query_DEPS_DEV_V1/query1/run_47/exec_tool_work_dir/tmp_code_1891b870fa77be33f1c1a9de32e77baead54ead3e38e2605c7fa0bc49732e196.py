code = """import json, re, pandas as pd
from pathlib import Path

latest_payload = json.load(open(Path(var_call_ZpqN5BHtvyNhxnZjmCOgxrk5)))
latest_npm = pd.DataFrame(latest_payload['latest_npm'])

ppv = pd.read_json(open(Path(var_call_3vXIqN8gaiCpnqSc61aiPrBy)))
pi = pd.read_json(open(Path(var_call_3GyBAbzdzrYLy51Wg9ku8Qcc)))

# filter to latest versions present in project_packageversion
merged = ppv.merge(latest_npm, on=['System','Name','Version'])

# extract repo name from Project_Information
pi['Repo'] = pi['Project_Information'].str.extract(r'The project ([^ ]+/[^ ]+)')
pi['Stars'] = pi['Project_Information'].str.extract(r'(\d[\d,]*) stars')[0].str.replace(',','').astype(float)

full = merged.merge(pi[['Repo','Stars']], left_on='ProjectName', right_on='Repo', how='left')

# get top 5 by stars
full = full.dropna(subset=['Stars'])

top5 = full.sort_values('Stars', ascending=False).drop_duplicates(subset=['Name']).head(5)

result = top5[['Name','Version','ProjectName','Stars']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_bkWkGDC7kj1RleZwsV3M4Bm7': 'file_storage/call_bkWkGDC7kj1RleZwsV3M4Bm7.json', 'var_call_HH8MNcR1jOmEYSt8hJQafXRf': ['project_info', 'project_packageversion'], 'var_call_MU6UKkmM9MPShKlvzhI4ASaq': 'file_storage/call_MU6UKkmM9MPShKlvzhI4ASaq.json', 'var_call_3vXIqN8gaiCpnqSc61aiPrBy': 'file_storage/call_3vXIqN8gaiCpnqSc61aiPrBy.json', 'var_call_3GyBAbzdzrYLy51Wg9ku8Qcc': 'file_storage/call_3GyBAbzdzrYLy51Wg9ku8Qcc.json', 'var_call_ZpqN5BHtvyNhxnZjmCOgxrk5': 'file_storage/call_ZpqN5BHtvyNhxnZjmCOgxrk5.json'}

exec(code, env_args)
