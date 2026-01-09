code = """import json, re

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pi = load_records(var_call_sgeHDZIFraeMQbE4GAAfgvfM)

s = pi[1]['Project_Information']
# show last 120 chars and try find 'fork'
idx = s.lower().find('fork')
context = s[max(0,idx-40):min(len(s), idx+40)] if idx!=-1 else None

# try number-forks regex
a = re.findall(r"(\d[\d,]*)\s+fork", s, flags=re.IGNORECASE)

print('__RESULT__:')
print(json.dumps({'sample': s, 'fork_index': idx, 'context': context, 'numforks': a}))"""

env_args = {'var_call_TyKo4w4PFjsjBMRx6p9huDCN': 'file_storage/call_TyKo4w4PFjsjBMRx6p9huDCN.json', 'var_call_Tqlka6yRDyF2ECJ6dmMSBY7j': 'file_storage/call_Tqlka6yRDyF2ECJ6dmMSBY7j.json', 'var_call_sgeHDZIFraeMQbE4GAAfgvfM': 'file_storage/call_sgeHDZIFraeMQbE4GAAfgvfM.json', 'var_call_94aZZ4ZZzjyHL8DPIpCBn7vH': {'matched_projects': 5289, 'parsed_projectinfo': 0, 'top5': []}, 'var_call_fk0nI4Y3bxKhZ3pa7NVhE0RA': {'pat1': [], 'pat2': [], 'pat3': []}}

exec(code, env_args)
