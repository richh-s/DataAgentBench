code = """import json
import re

fp = locals()['var_function-call-61089627249181938']
dp = locals()['var_function-call-61089627249180915']

with open(fp, 'r') as f:
    funding = json.load(f)
with open(dp, 'r') as f:
    docs = json.load(f)

f_map = {x['Project_Name']: x['Amount'] for x in funding}
p_names = sorted(list(f_map.keys()), key=len, reverse=True)
rel = set()

for d in docs:
    txt = d['text']
    occs = []
    for n in p_names:
        pat = re.compile(re.escape(n), re.IGNORECASE)
        for m in pat.finditer(txt):
            occs.append((m.start(), n))
    occs.sort(key=lambda x: x[0])
    
    for i in range(len(occs)):
        s, n = occs[i]
        e = occs[i+1][0] if i+1 < len(occs) else len(txt)
        seg = txt[s:e].lower()
        
        is_park = 'park' in n.lower() or 'park' in seg
        is_comp = False
        
        for l in seg.splitlines():
            if '2022' in l:
                if 'design' in l and 'complete' in l:
                    continue
                if 'construction' in l and ('complete' in l or 'completed' in l):
                    is_comp = True
                    break
                if 'completed' in l and 'design' not in l:
                    is_comp = True
                    break
                if 'notice of completion' in l:
                    is_comp = True
                    break
        
        if is_park and is_comp:
            rel.add(n)

tot = sum(int(f_map[n]) for n in rel)
print("__RESULT__:")
print(json.dumps({"total": tot, "projects": list(rel)}))"""

env_args = {'var_function-call-11325768186704868544': ['Funding'], 'var_function-call-11325768186704870109': ['civic_docs'], 'var_function-call-61089627249181938': 'file_storage/function-call-61089627249181938.json', 'var_function-call-61089627249180915': 'file_storage/function-call-61089627249180915.json'}

exec(code, env_args)
