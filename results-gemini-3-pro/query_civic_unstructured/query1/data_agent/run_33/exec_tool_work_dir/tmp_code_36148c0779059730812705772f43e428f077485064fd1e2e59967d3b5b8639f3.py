code = """import json

fp = locals()['var_function-call-5441404039575521335']
dp = locals()['var_function-call-5441404039575519310']

with open(fp) as f:
    fdata = json.load(f)

high_funds = set()
for x in fdata:
    try:
        if int(x.get('Amount', 0)) > 50000:
            high_funds.add(x.get('Project_Name', '').strip())
    except:
        pass

with open(dp) as f:
    docs = json.load(f)

extracted = set()
target = "Capital Improvement Projects (Design)"
stops = ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]

for d in docs:
    txt = d.get('text', '')
    start = txt.find(target)
    if start == -1:
        continue
    content_start = start + len(target)
    
    end = len(txt)
    for s in stops:
        s_idx = txt.find(s, content_start)
        if s_idx != -1 and s_idx < end:
            end = s_idx
            
    chunk = txt[content_start:end]
    
    for line in chunk.split('\n'):
        l = line.strip()
        if not l: continue
        if l.startswith('(') or l.startswith('Page') or l.startswith('Agenda'): continue
        if ':' in l: continue 
        extracted.add(l)

matches = []
for p in extracted:
    if p in high_funds:
        matches.append(p)

print("__RESULT__:")
print(json.dumps({"count": len(matches), "matches": matches}))"""

env_args = {'var_function-call-5441404039575521335': 'file_storage/function-call-5441404039575521335.json', 'var_function-call-5441404039575519310': 'file_storage/function-call-5441404039575519310.json'}

exec(code, env_args)
