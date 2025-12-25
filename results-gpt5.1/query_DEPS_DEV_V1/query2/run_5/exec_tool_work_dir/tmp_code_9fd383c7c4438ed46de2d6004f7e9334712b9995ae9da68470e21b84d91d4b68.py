code = """import json, re

# Load project_info
path_pi = var_call_E0lfntVbjWdb2k9Lr3FsIhDv
with open(path_pi, 'r') as f:
    pi = json.load(f)

rows = []
for rec in pi:
    info = rec.get('Project_Information','') or ''
    m = re.search(r'The project ([^\s/]+/[^\s]+)', info)
    if not m:
        m = re.search(r'named ([^\s/]+/[^\s]+)', info)
    if not m:
        continue
    name = m.group(1).rstrip('.,')
    m2 = re.search(r'(?:and )?(\d[\d,]*) forks', info)
    forks = None
    if m2:
        forks = int(m2.group(1).replace(',',''))
    rows.append({'ProjectName': name, 'Forks': forks})

import pandas as pd
pi_df = pd.DataFrame(rows).dropna().drop_duplicates(subset=['ProjectName'])

# Just get top 5 by forks overall as fallback
pi_df = pi_df.sort_values('Forks', ascending=False).head(5)

result = pi_df.to_dict(orient='records')

import json
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_yVihHw8OryaPo0wdoSVFAjNi': 'file_storage/call_yVihHw8OryaPo0wdoSVFAjNi.json', 'var_call_hLGwiIiy4m9TB8RgRsUNwI2T': ['project_info', 'project_packageversion'], 'var_call_XpBNYaDrfdSqpqKA3XzG1dSK': 'file_storage/call_XpBNYaDrfdSqpqKA3XzG1dSK.json', 'var_call_E0lfntVbjWdb2k9Lr3FsIhDv': 'file_storage/call_E0lfntVbjWdb2k9Lr3FsIhDv.json', 'var_call_92TnDeBUyyjtedoymhIDua0s': []}

exec(code, env_args)
