code = """import json, pandas as pd, re
from pathlib import Path

pkgs = json.loads(Path(var_call_w2G5KnCPUmoYjQN7aF6Mvv4s).read_text())
ppv = json.loads(Path(var_call_9bwkoIBz7v5d8EFe4O4rpQTo).read_text())
pi = json.loads(Path(var_call_VZkYE1PofTZx7ctQxHf8AGye).read_text())

pkgs_df = pd.DataFrame(pkgs)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

merged = pkgs_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

pi_df['Repo'] = pi_df['Project_Information'].str.extract(r'The project ([^ ]+/[^ ]+)')[0]
pi_df['Forks'] = pi_df['Project_Information'].str.extract(r'([0-9,]+) forks')[0].str.replace(',','').astype(float)

final = merged.merge(pi_df[['Repo','Forks']], left_on='ProjectName', right_on='Repo', how='left')

agg = final.groupby('ProjectName', as_index=False)['Forks'].max()

Top5 = agg.sort_values('Forks', ascending=False).head(5)

result = Top5.to_dict(orient='records')

import json as _j
out = _j.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_MAtCDUrvf8tmzLFUrkv05Meq': 'file_storage/call_MAtCDUrvf8tmzLFUrkv05Meq.json', 'var_call_5ktSNeYNX6BbEDqQ1dg9FYzg': ['project_info', 'project_packageversion'], 'var_call_w2G5KnCPUmoYjQN7aF6Mvv4s': 'file_storage/call_w2G5KnCPUmoYjQN7aF6Mvv4s.json', 'var_call_9bwkoIBz7v5d8EFe4O4rpQTo': 'file_storage/call_9bwkoIBz7v5d8EFe4O4rpQTo.json', 'var_call_VZkYE1PofTZx7ctQxHf8AGye': 'file_storage/call_VZkYE1PofTZx7ctQxHf8AGye.json'}

exec(code, env_args)
