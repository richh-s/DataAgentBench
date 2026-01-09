code = """import json, re

src = var_call_LmPNLM924ObwyafyS5MXax8F
if isinstance(src, str):
    with open(src,'r',encoding='utf-8') as f:
        docs=json.load(f)
else:
    docs=src

year_pat=re.compile(r"\b(19\d{2}|20\d{2})\b")

def infer_year(text):
    head=text[:2000]
    years=[int(m.group(1)) for m in year_pat.finditer(head)]
    if not years:
        return None
    if 2016 in years:
        return 2016
    return max(years)

cands=[]
for d in docs:
    title=d['filename'][:-4]
    t=d.get('text','') or ''
    if 'physical activity' in t.lower() or 'physical activity' in title.lower():
        yr=infer_year(t)
        if yr==2016:
            cands.append(title)

print('__RESULT__:')
print(json.dumps({'count':len(cands),'titles':sorted(set(cands))[:50]}))"""

env_args = {'var_call_urqQvPDDNTuisiC9AaBv7TRX': 'file_storage/call_urqQvPDDNTuisiC9AaBv7TRX.json', 'var_call_lRDmaLR0wnwMoQWFAwDd3Sla': 'file_storage/call_lRDmaLR0wnwMoQWFAwDd3Sla.json', 'var_call_rKHf4c5jlJWu2hhYx2qpXXGw': [], 'var_call_LmPNLM924ObwyafyS5MXax8F': 'file_storage/call_LmPNLM924ObwyafyS5MXax8F.json'}

exec(code, env_args)
