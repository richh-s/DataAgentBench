code = """import json
import pandas as pd

k1 = 'var_function-call-13970698935459151877'
k2 = 'var_function-call-13579203068557831030'

f_path = locals().get(k1)
d_path = locals().get(k2)

with open(f_path, 'r') as f:
    funding = json.load(f)
with open(d_path, 'r') as f:
    docs = json.load(f)

df = pd.DataFrame(funding)
df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce').fillna(0)
# Group sum check
grp = df.groupby('Project_Name')['Amount'].sum()
funded = set(grp[grp > 50000].index)

design_projs = set()
for d in docs:
    lines = d['text'].split('\n')
    active = False
    for l in lines:
        l = l.strip()
        # Header detection
        if l.startswith('Capital Improvement Projects') and 'Design' in l:
            active = True
            continue
        if l.startswith('Capital Improvement Projects') and 'Design' not in l:
            active = False
            continue
        if l.startswith('Disaster Recovery Projects'):
            active = False
            continue
        
        if active:
            if not l: continue
            if l.startswith('(') or l.startswith('Updates') or l.startswith('Project') or l.startswith('Estimated'): continue
            if l.startswith('Page') or l.startswith('Agenda') or l.startswith('Subject') or l.startswith('Date'): continue
            if l.startswith('Complete') or l.startswith('Advertise') or l.startswith('Begin'): continue
            
            design_projs.add(l)

matches = design_projs.intersection(funded)
print('__RESULT__:')
print(json.dumps({'count': len(matches), 'matches': list(matches)}))"""

env_args = {'var_function-call-13970698935459151877': 'file_storage/function-call-13970698935459151877.json', 'var_function-call-13579203068557831030': 'file_storage/function-call-13579203068557831030.json'}

exec(code, env_args)
