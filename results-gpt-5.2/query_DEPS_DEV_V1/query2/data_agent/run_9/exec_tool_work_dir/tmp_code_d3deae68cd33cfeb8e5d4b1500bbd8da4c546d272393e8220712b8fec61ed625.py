code = """import json, re

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pi = load_records(var_call_sgeHDZIFraeMQbE4GAAfgvfM)

samples = [pi[i]['Project_Information'] for i in range(min(50,len(pi)))]

# test regex patterns
patterns = {
 'pat1': r"project\s+([^\s]+/[^\s]+).*?\b(\d[\d,]*)\s+forks\b",
 'pat2': r"project\s+(?:named\s+)?([^\s]+/[^\s,]+).*?\b(\d[\d,]*)\s+forks\b",
 'pat3': r"\b([^\s]+/[^\s,]+)\b.*?\b(\d[\d,]*)\s+forks\b",
}
res = {}
for k,p in patterns.items():
    rg = re.compile(p, re.IGNORECASE)
    hits=[]
    for s in samples:
        m=rg.search(s)
        if m:
            hits.append({'s': s, 'pname': m.group(1), 'forks': m.group(2)})
    res[k]=hits[:3]

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_TyKo4w4PFjsjBMRx6p9huDCN': 'file_storage/call_TyKo4w4PFjsjBMRx6p9huDCN.json', 'var_call_Tqlka6yRDyF2ECJ6dmMSBY7j': 'file_storage/call_Tqlka6yRDyF2ECJ6dmMSBY7j.json', 'var_call_sgeHDZIFraeMQbE4GAAfgvfM': 'file_storage/call_sgeHDZIFraeMQbE4GAAfgvfM.json', 'var_call_94aZZ4ZZzjyHL8DPIpCBn7vH': {'matched_projects': 5289, 'parsed_projectinfo': 0, 'top5': []}}

exec(code, env_args)
