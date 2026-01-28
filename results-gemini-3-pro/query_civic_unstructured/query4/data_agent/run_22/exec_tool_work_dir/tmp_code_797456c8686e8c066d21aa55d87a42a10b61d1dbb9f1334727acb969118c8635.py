code = """import json
import pandas as pd

k1 = 'var_function-call-8904296491751843034'
k2 = 'var_function-call-8494922430906473506'
with open(locals()[k1], 'r') as f:
    d1 = json.load(f)
df = pd.DataFrame(d1)
df['Amount'] = pd.to_numeric(df['Amount'])

with open(locals()[k2], 'r') as f:
    d2 = json.load(f)

projs = set()
for d in d2:
    txt = d.get('text', '')
    lines = txt.splitlines()
    cur = ''
    buf = ''
    for line in lines:
        line = line.strip()
        if not line: continue
        low = line.lower()
        if 'page' in low: continue
        
        if 'Updates:' in line or 'Project Schedule:' in line:
            if buf: cur = buf
            
        if cur and 'begin construction' in low:
            if 'spring' in low and '2022' in low:
                projs.add(cur)
            elif '2022' in low and ('march' in low or 'april' in low or 'may' in low):
                projs.add(cur)
        
        if 'Updates:' not in line and 'Project Schedule:' not in line:
            buf = line

tot = 0
lst = list(projs)
for i, r in df.iterrows():
    fn = r['Project_Name'].strip()
    m = False
    for p in lst:
        pc = p.strip()
        if pc.lower() in fn.lower() or fn.lower() in pc.lower():
            if len(pc) > 5 and len(fn) > 5:
                m = True
        if m: break
    if m:
        tot += r['Amount']

print('__RESULT__:')
print(json.dumps({'count': len(projs), 'funding': tot, 'projects': lst}))"""

env_args = {'var_function-call-1649366549132259120': 'file_storage/function-call-1649366549132259120.json', 'var_function-call-17157926342599850647': 'file_storage/function-call-17157926342599850647.json', 'var_function-call-8904296491751843034': 'file_storage/function-call-8904296491751843034.json', 'var_function-call-8494922430906473506': 'file_storage/function-call-8494922430906473506.json'}

exec(code, env_args)
