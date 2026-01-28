code = """import json, re
path = var_call_dUI72YM2tUPWqWc9noXwOSUb
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

candidates = []
keywords = [r"physical activity", r"activity", r"activity tracking", r"activity tracker", r"exercise", r"fitness", r"activity trackers"]
for r in records:
    title = r.get('title','')
    low = title.lower()
    if any(kw in low for kw in [k.lower() for k in keywords]):
        candidates.append({'title': title, 'total_citations': int(r.get('total_citations',0))})

# deduplicate
seen = set(); uniq = []
for c in candidates:
    if c['title'] not in seen:
        seen.add(c['title']); uniq.append(c)

import json
print("__RESULT__:")
print(json.dumps(uniq))"""

env_args = {'var_call_R3Jsc9jJ2f081nEgJYmXt0we': 'file_storage/call_R3Jsc9jJ2f081nEgJYmXt0we.json', 'var_call_CRWoBTvRBnOAaxGATytfY7eg': [], 'var_call_DX5qm54njXAG3VA8Ns0XT0CT': 'file_storage/call_DX5qm54njXAG3VA8Ns0XT0CT.json', 'var_call_oa0IkubHrYmUaxkc3inyJOzE': [], 'var_call_ypSCdY3MpucsmohKpzfZVJau': 'file_storage/call_ypSCdY3MpucsmohKpzfZVJau.json', 'var_call_zeocturV7lV5Q3GfltpOhPo8': [], 'var_call_nX85GeNenY1UOFZPNHgqMvho': ['Citations', 'sqlite_sequence'], 'var_call_dUI72YM2tUPWqWc9noXwOSUb': 'file_storage/call_dUI72YM2tUPWqWc9noXwOSUb.json'}

exec(code, env_args)
