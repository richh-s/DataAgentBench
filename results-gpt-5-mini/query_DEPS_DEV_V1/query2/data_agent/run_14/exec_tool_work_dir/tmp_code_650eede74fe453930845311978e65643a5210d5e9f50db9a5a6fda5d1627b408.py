code = """import json, re
# load files
fp_pkg = var_call_TiqTJ2qgioCLSYHkIik7ZSys
fp_ppv = var_call_zgk2eTfGFhkYDiYaitJ8dius
fp_pi = var_call_nEOU6Ai0AzaSOEKqCfkdZI6n
with open(fp_pkg, 'r', encoding='utf-8') as f:
    pkg = json.load(f)
with open(fp_ppv, 'r', encoding='utf-8') as f:
    ppv = json.load(f)
with open(fp_pi, 'r', encoding='utf-8') as f:
    pi = json.load(f)
# Build set of triples from pkg
triples = set((r['System'], r['Name'], r['Version']) for r in pkg)
# Filter ppv for those triples and ProjectType GITHUB
matched = [r for r in ppv if (r['System'], r['Name'], r['Version']) in triples and r.get('ProjectType','').upper() == 'GITHUB']
# Get unique ProjectNames
proj_names = sorted(set(r['ProjectName'] for r in matched))
# Prepare regex patterns to extract forks
pat1 = re.compile(r"([0-9][0-9,]*)\s+forks", re.IGNORECASE)
pat2 = re.compile(r"forked\s+([0-9][0-9,]*)\s+times", re.IGNORECASE)
# Map projectname to best (max) forks and store matched Project_Information
proj_map = {}
for name in proj_names:
    best_forks = None
    best_info = None
    for entry in pi:
        info = entry.get('Project_Information','')
        if name in info:
            m = pat1.search(info)
            if not m:
                m = pat2.search(info)
            if m:
                num = int(m.group(1).replace(',',''))
            else:
                # try to find last number before 'fork' words
                m2 = re.search(r"([0-9][0-9,]*)\D*$", info)
                if m2:
                    try:
                        num = int(m2.group(1).replace(',',''))
                    except:
                        num = 0
                else:
                    num = 0
            if best_forks is None or num > best_forks:
                best_forks = num
                best_info = info
    if best_forks is not None:
        proj_map[name] = {'ProjectName': name, 'Forks': best_forks, 'Project_Information': best_info}
# Now get top 5 by Forks
top5 = sorted(proj_map.values(), key=lambda x: x['Forks'], reverse=True)[:5]
# Prepare output list
out = []
for p in top5:
    out.append({'ProjectName': p['ProjectName'], 'Forks': p['Forks'], 'Project_Information': p['Project_Information']})
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Tg084gBAp439zBv6nyGVDZv7': ['packageinfo'], 'var_call_JC9jizmvdS8ELnpNsf7ahvqd': ['project_info', 'project_packageversion'], 'var_call_TiqTJ2qgioCLSYHkIik7ZSys': 'file_storage/call_TiqTJ2qgioCLSYHkIik7ZSys.json', 'var_call_wlXtcY4UuYpOaXxovR9Mjzpi': 'file_storage/call_wlXtcY4UuYpOaXxovR9Mjzpi.json', 'var_call_zgk2eTfGFhkYDiYaitJ8dius': 'file_storage/call_zgk2eTfGFhkYDiYaitJ8dius.json', 'var_call_nEOU6Ai0AzaSOEKqCfkdZI6n': 'file_storage/call_nEOU6Ai0AzaSOEKqCfkdZI6n.json'}

exec(code, env_args)
