code = """import json, re
path = var_call_4C61MtgpdwSLhWSyl0zVwwny
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)
# records is a list of dicts with ProjectName and Project_Information
proj_stats = {}
for r in records:
    pname = r.get('ProjectName')
    pinfo = r.get('Project_Information') or ''
    if not pname or not pinfo:
        continue
    s = pinfo.lower()
    # find number that corresponds to forks by looking for digits before 'fork'
    m = re.search(r"(\d+)(?=[^0-9]*forks?)", s)
    forks = None
    if m:
        try:
            forks = int(m.group(1))
        except:
            forks = None
    # fallback: look for 'fork count of' pattern
    if forks is None:
        m2 = re.search(r"forks count of\s*(\d+)", s)
        if m2:
            forks = int(m2.group(1))
    if forks is None:
        # try to find 'and X forks' pattern
        m3 = re.search(r"and\s*(\d+)\s*forks", s)
        if m3:
            forks = int(m3.group(1))
    if forks is None:
        continue
    # update max forks for project
    if pname in proj_stats:
        if forks > proj_stats[pname]['forks']:
            proj_stats[pname] = {'forks': forks, 'Project_Information': pinfo}
    else:
        proj_stats[pname] = {'forks': forks, 'Project_Information': pinfo}
# build sorted list
items = [(p, v['forks'], v['Project_Information']) for p,v in proj_stats.items()]
items.sort(key=lambda x: x[1], reverse=True)
top5 = items[:5]
# prepare output list of dicts
out = []
for p,f,pinfo in top5:
    out.append({'ProjectName': p, 'Forks': f, 'Project_Information': pinfo})
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_HEzdcz70IjrP9lRgEgpSAqfY': 'file_storage/call_HEzdcz70IjrP9lRgEgpSAqfY.json', 'var_call_XyVtwkmcTawWXvXXtuY1XOGs': 'file_storage/call_XyVtwkmcTawWXvXXtuY1XOGs.json', 'var_call_4C61MtgpdwSLhWSyl0zVwwny': 'file_storage/call_4C61MtgpdwSLhWSyl0zVwwny.json', 'var_call_NHugqj7ugVKcE6M5w7ByHebC': 'file_storage/call_NHugqj7ugVKcE6M5w7ByHebC.json', 'var_call_0Yio9djOf8WN2eIIwHwi7GWg': 'file_storage/call_0Yio9djOf8WN2eIIwHwi7GWg.json', 'var_call_jMQP6mA54MC2pwJLxqYCD0zQ': 'file_storage/call_jMQP6mA54MC2pwJLxqYCD0zQ.json'}

exec(code, env_args)
