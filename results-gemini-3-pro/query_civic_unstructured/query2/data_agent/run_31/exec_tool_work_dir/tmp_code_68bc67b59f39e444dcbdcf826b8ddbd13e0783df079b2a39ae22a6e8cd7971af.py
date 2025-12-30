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

# Broadened regex
# Catch "Repairs completed", "Work completed", "Installation completed"
# Ensure "2022" follows
completion_pat = re.compile(r'(construction|project|repairs|work|installation)\s+(was\s+)?completed.*?2022', re.IGNORECASE)
notice_pat = re.compile(r'notice\s+of\s+completion.*?2022', re.IGNORECASE)

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
        seg = txt[s:e]
        
        is_park = 'park' in n.lower() or 'park' in seg.lower()
        
        if is_park:
            # Check completion
            if completion_pat.search(seg) or notice_pat.search(seg):
                rel.add(n)

tot = sum(int(f_map[n]) for n in rel)
print("__RESULT__:")
print(json.dumps({"total": tot, "projects": list(rel)}))"""

env_args = {'var_function-call-11325768186704868544': ['Funding'], 'var_function-call-11325768186704870109': ['civic_docs'], 'var_function-call-61089627249181938': 'file_storage/function-call-61089627249181938.json', 'var_function-call-61089627249180915': 'file_storage/function-call-61089627249180915.json', 'var_function-call-3346348138217610157': {'total': 118000, 'projects': ['Permanent Skate Park', 'Bluffs Park Shade Structure']}, 'var_function-call-17565848284776164481': {'total': 21000, 'projects': ['Bluffs Park Shade Structure']}}

exec(code, env_args)
