code = """import json, pandas as pd
from pathlib import Path

latest_file = Path(var_call_76sOfFkAL4zLZnH6T42uaDCQ)
with open(latest_file, 'r') as f:
    latest = pd.DataFrame(json.load(f))

ppv_file = Path(var_call_uoQRuun1PVbiSJwHIMTbo7C6)
with open(ppv_file, 'r') as f:
    ppv = pd.DataFrame(json.load(f))

merged = latest.merge(ppv, on=['System','Name','Version'])

pi_file = Path(var_call_ycx82RJ2J2D6698vHytNrp5p)
with open(pi_file, 'r') as f:
    pi = pd.DataFrame(json.load(f))

import re

projects = []
stars = []
for info in pi['Project_Information']:
    m = re.search(r"project ([^\s/]+/[^\s]+)|named ([^\s/]+/[^\s]+)|under the name ([^\s/]+/[^\s,]+)", info)
    if m:
        repo = next(g for g in m.groups() if g)
        sm = re.search(r"(\d[\d,]*) stars", info)
        star = int(sm.group(1).replace(',', '')) if sm else 0
        projects.append(repo)
        stars.append(star)

pi_parsed = pd.DataFrame({'ProjectName': projects, 'Stars': stars}).drop_duplicates('ProjectName')

full = merged.merge(pi_parsed, on='ProjectName')
top5 = full.sort_values('Stars', ascending=False).head(5)[['Name','Version','Stars']]
result = top5.to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_yPpXlVfm6ScbUH2S2tJxhtOl': ['project_info', 'project_packageversion'], 'var_call_81KwFwNqlKOKOn9C6KRVZwE3': 'file_storage/call_81KwFwNqlKOKOn9C6KRVZwE3.json', 'var_call_76sOfFkAL4zLZnH6T42uaDCQ': 'file_storage/call_76sOfFkAL4zLZnH6T42uaDCQ.json', 'var_call_uoQRuun1PVbiSJwHIMTbo7C6': 'file_storage/call_uoQRuun1PVbiSJwHIMTbo7C6.json', 'var_call_ycx82RJ2J2D6698vHytNrp5p': 'file_storage/call_ycx82RJ2J2D6698vHytNrp5p.json'}

exec(code, env_args)
