code = """import json, re
raw = var_call_C8L5zhLal1Zk1ENuLjD2VCfK
if isinstance(raw, str):
    with open(raw,'r',encoding='utf-8') as f:
        docs=json.load(f)
else:
    docs=raw

projects=set()
for d in docs:
    lines=d.get('text','').splitlines()
    for i,line in enumerate(lines):
        if re.search(r'\bBegin\s+Construction\s*:\s*Spring\s+2022\b', line, flags=re.I):
            j=i-1
            while j>=0:
                s=lines[j].strip()
                if s and not re.search(r'^(\(cid:|\u2022|\*|\-|\d+\.|Page\s+\d+|Agenda Item|\(cid)', s):
                    break
                j-=1
            if j>=0:
                name=lines[j].strip()
                if not re.search(r'^(Project Schedule|Estimated Schedule|Updates|Capital Improvement Projects|Disaster Projects|Disaster Recovery Projects)', name, flags=re.I):
                    projects.add(name)

print('__RESULT__:')
print(json.dumps({'projects':sorted(projects), 'count':len(projects)}))"""

env_args = {'var_call_voCW34f5mhpr4lBcDrP0GdJi': ['Funding'], 'var_call_beaAEvwBIwRzy1HcSw5H4XHD': ['civic_docs'], 'var_call_sir3H7yoilAVtxp9uzAjCNCs': 'file_storage/call_sir3H7yoilAVtxp9uzAjCNCs.json', 'var_call_1OKkPLKGhwTNK2ZpwqZXJyH2': {'projects': [], 'count': 0}, 'var_call_C8L5zhLal1Zk1ENuLjD2VCfK': 'file_storage/call_C8L5zhLal1Zk1ENuLjD2VCfK.json'}

exec(code, env_args)
