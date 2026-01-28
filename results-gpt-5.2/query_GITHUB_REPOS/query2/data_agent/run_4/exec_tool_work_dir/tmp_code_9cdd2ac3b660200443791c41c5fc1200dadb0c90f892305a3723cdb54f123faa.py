code = """import json, pandas as pd, re
path = var_call_KBUkbcMU1867QN93NvxbMlGE
with open(path,'r') as f:
    recs = json.load(f)

rows=[]
for r in recs:
    desc = (r.get('repo_data_description') or '').lower()
    if not r.get('sample_path','').lower().endswith('.swift'):
        continue
    if 'non-binary' not in desc:
        continue
    m = re.search(r'(?:duplicated|copied|appearing|seen|appears)\s+(\d+)\s+times', desc)
    if not m:
        m = re.search(r'(\d+)\s+times', desc)
    copies = int(m.group(1)) if m else None
    rows.append({
        'id': r['id'],
        'repo_name': r['sample_repo_name'],
        'sample_path': r['sample_path'],
        'copies': copies
    })

df=pd.DataFrame(rows)
df=df[df['copies'].notna()]
if len(df)==0:
    out={'error':'no parsed copies in sample'}
else:
    top=df.sort_values(['copies','id'], ascending=[False,True]).iloc[0].to_dict()
    out=top
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_69QHJeGXUwKuNybppCFd0sJO': [], 'var_call_KBUkbcMU1867QN93NvxbMlGE': 'file_storage/call_KBUkbcMU1867QN93NvxbMlGE.json', 'var_call_dX2ssbFpelxOD3aRcZv0HCBJ': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'repo_name': 'kostiakoval/WatchKit-Apps', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'copies': 'None'}], 'var_call_6OS0ODnzYyrCKQhHjeqpxM5S': []}

exec(code, env_args)
