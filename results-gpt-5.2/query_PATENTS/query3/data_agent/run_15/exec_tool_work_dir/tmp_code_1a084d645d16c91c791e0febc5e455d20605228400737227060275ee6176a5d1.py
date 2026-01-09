code = """import json, re

uc_path = var_call_j55SyTVQyBw0aAybXsyxCaAM
with open(uc_path, 'r', encoding='utf-8') as f:
    uc_rows = json.load(f)

pub_re = re.compile(r"pub\. number\s+([A-Z]{2,}-[0-9A-Z]+(?:-[A-Z][0-9])?)", re.I)
fallback_re = re.compile(r"\b([A-Z]{2,}-\d{7,}-[A-Z]\d)\b")

uc_pubs=set()
for r in uc_rows:
    txt=r.get('Patents_info','') or ''
    m=pub_re.search(txt)
    if m: uc_pubs.add(m.group(1))
    for mm in fallback_re.findall(txt):
        uc_pubs.add(mm)

# normalize keys without hyphen before kind (e.g., US-2022074631-A1)

def norm(p):
    return re.sub(r"-([A-Z]\d)$", r"\1", p)

uc_norm=set([norm(p) for p in uc_pubs])

cit_path = var_call_KJ7mredPpIpCLZFg4dHYGs9s
with open(cit_path, 'r', encoding='utf-8') as f:
    citing_rows = json.load(f)

matched=[]
for r in citing_rows[:5000]:
    cstr=r.get('citation')
    if not cstr or cstr.strip() in ('','[]'): continue
    try:
        cites=json.loads(cstr)
    except: continue
    for c in cites:
        pn=(c.get('publication_number') or '') if isinstance(c,dict) else ''
        if pn in uc_pubs or norm(pn) in uc_norm:
            matched.append({'citing': r.get('Patents_info','')[:120], 'cited': pn})
            break

print('__RESULT__:')
print(json.dumps({'uc_pub_sample': sorted(list(uc_pubs))[:20], 'match_count_5000': len(matched), 'match_sample': matched[:5]}))"""

env_args = {'var_call_RXZxPa6ek2GtXCBDhmGKF66H': ['publicationinfo'], 'var_call_xRaFlt6HbwpuEGgcKr0x8ZXF': ['cpc_definition'], 'var_call_j55SyTVQyBw0aAybXsyxCaAM': 'file_storage/call_j55SyTVQyBw0aAybXsyxCaAM.json', 'var_call_zqNKJTMEJLBC8OYNvbOYtOK0': {'uc_pub_count': 59}, 'var_call_KJ7mredPpIpCLZFg4dHYGs9s': 'file_storage/call_KJ7mredPpIpCLZFg4dHYGs9s.json', 'var_call_gTbEbPoeoJQcPiupxFUywacn': {'pairs': [], 'pair_count': 0, 'assignee_count': 0}}

exec(code, env_args)
