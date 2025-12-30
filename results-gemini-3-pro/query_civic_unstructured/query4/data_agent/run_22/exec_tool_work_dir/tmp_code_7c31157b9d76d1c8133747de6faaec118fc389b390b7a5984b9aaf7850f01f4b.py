code = """import json
import pandas as pd

# Load data
k1 = 'var_function-call-8904296491751843034'
k2 = 'var_function-call-8494922430906473506'
with open(locals()[k1], 'r') as f: fd = json.load(f)
with open(locals()[k2], 'r') as f: cd = json.load(f)

f_df = pd.DataFrame(fd)
f_df['Amount'] = pd.to_numeric(f_df['Amount'])

projs = set()

for d in cd:
    txt = d.get('text', '')
    lns = txt.split('\n')
    curr = None
    buf = None
    
    for l in lns:
        l = l.strip()
        if not l: continue
        if l.lower().startswith('page ') or 'agenda item' in l.lower(): continue
        
        # Check markers
        is_marker = 'Updates:' in l or 'Project Schedule:' in l or 'Project Description:' in l
        
        if is_marker and buf:
            curr = buf
            
        if curr and 'begin construction' in l.lower():
            if 'spring' in l.lower() and '2022' in l.lower():
                projs.add(curr)
            elif '2022' in l.lower():
                # Check months
                if any(m in l.lower() for m in ['march', 'april', 'may']):
                    projs.add(curr)
                    
        if not is_marker and '(cid:' not in l:
            buf = l

# Calculate funding
tot = 0
found_projs = list(projs)

for i, r in f_df.iterrows():
    fn = r['Project_Name'].strip()
    match = False
    for p in found_projs:
        if p.lower() == fn.lower(): match = True
        elif len(p) > 5 and len(fn) > 5 and (p.lower() in fn.lower() or fn.lower() in p.lower()): match = True
        if match: break
    
    if match:
        tot += r['Amount']

print("__RESULT__:")
print(json.dumps({"count": len(projs), "funding": tot, "list": found_projs}))"""

env_args = {'var_function-call-1649366549132259120': 'file_storage/function-call-1649366549132259120.json', 'var_function-call-17157926342599850647': 'file_storage/function-call-17157926342599850647.json', 'var_function-call-8904296491751843034': 'file_storage/function-call-8904296491751843034.json', 'var_function-call-8494922430906473506': 'file_storage/function-call-8494922430906473506.json'}

exec(code, env_args)
