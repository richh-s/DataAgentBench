code = """import json
path = var_call_RrmAuwXmqg52X8TuT8IIP0jf
with open(path,'r',encoding='utf-8') as f:
    docs=json.load(f)

names=set()
needle='Begin Construction: Spring 2022'
for d in docs:
    txt=d.get('text','')
    idx=txt.lower().find(needle.lower())
    if idx==-1:
        continue
    prefix=txt[:idx]
    lines=[ln.strip() for ln in prefix.splitlines() if ln.strip()]
    # find nearest preceding line that looks like a project title (not bullet, not contains ':')
    for cand in reversed(lines[-50:]):
        if ':' in cand:
            continue
        if cand.startswith('(cid') or cand.startswith('•') or cand.startswith('-') or cand.startswith('–'):
            continue
        if len(cand)<4 or len(cand)>120:
            continue
        low=cand.lower()
        if low.startswith('project schedule') or low.startswith('estimated schedule'):
            continue
        if 'capital improvement projects' in low or 'disaster projects' in low:
            continue
        names.add(cand)
        break

import json as _json
print('__RESULT__:')
print(_json.dumps({'projects':sorted(names),'count':len(names)}))"""

env_args = {'var_call_GU7TOrWp60QnSxcfBDDbjJb3': ['civic_docs'], 'var_call_oT345mwgQj4Nim0YXkOkj7b9': ['Funding'], 'var_call_4kyFbfoBMGRtUpextA1f4p3h': 'file_storage/call_4kyFbfoBMGRtUpextA1f4p3h.json', 'var_call_RrmAuwXmqg52X8TuT8IIP0jf': 'file_storage/call_RrmAuwXmqg52X8TuT8IIP0jf.json'}

exec(code, env_args)
