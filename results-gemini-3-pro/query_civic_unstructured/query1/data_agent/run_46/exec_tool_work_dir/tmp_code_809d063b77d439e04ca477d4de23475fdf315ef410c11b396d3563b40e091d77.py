code = """import json

k1 = 'var_function-call-13970698935459151877'
k2 = 'var_function-call-13579203068557831030'
with open(locals()[k1], 'r') as f: funding = json.load(f)
with open(locals()[k2], 'r') as f: docs = json.load(f)

sums = {}
for x in funding:
    n = x['Project_Name']
    try:
        a = float(x['Amount'])
    except:
        a = 0
    sums[n] = sums.get(n, 0.0) + a

funded = set()
for n, s in sums.items():
    if s > 50000:
        funded.add(n)

matches = set()
header = "Capital Improvement Projects"
sub = "Design"
LPAREN = chr(40)

for d in docs:
    txt = d['text']
    lines = txt.split('\n')
    on = False
    for l in lines:
        l = l.strip()
        if l.startswith(header):
            if sub in l:
                on = True
            else:
                on = False
            continue
        if "Disaster" in l:
            on = False
            continue
        
        if on:
            if not l: continue
            if l.startswith(LPAREN): continue 
            if l.startswith("Updates"): continue
            if l.startswith("Project"): continue
            if l.startswith("Page"): continue
            if l.startswith("Agenda"): continue
            if l.startswith("Complete"): continue
            if l.startswith("Advertise"): continue
            if l.startswith("Begin"): continue
            if l.startswith("Estimated"): continue
            
            matches.add(l)

final = matches.intersection(funded)
print("__RESULT__:")
print(json.dumps({"count": len(final), "matches": list(final)}))"""

env_args = {'var_function-call-13970698935459151877': 'file_storage/function-call-13970698935459151877.json', 'var_function-call-13579203068557831030': 'file_storage/function-call-13579203068557831030.json'}

exec(code, env_args)
