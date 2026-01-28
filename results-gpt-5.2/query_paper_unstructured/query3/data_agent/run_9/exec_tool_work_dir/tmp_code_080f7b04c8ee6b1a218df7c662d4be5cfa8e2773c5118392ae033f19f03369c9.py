code = """import json, re
import pandas as pd

def load(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj,'r',encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

paper_files = load(var_call_yT6VnzVAD5KgNEJfkDcNSIvX)
cit_totals = load(var_call_dlKzirn0K8NqiTc2y1I5brDh)

titles = [r['filename'][:-4] if r.get('filename','').lower().endswith('.txt') else r.get('filename') for r in paper_files]

def infer_year_from_title(t):
    m = re.search(r'\b(19\d{2}|20\d{2})\b', t)
    return int(m.group(1)) if m else None

def is_empirical_title(t):
    return bool(re.search(r'\bempirical\b', t, flags=re.I))

rows=[]
for t in titles:
    y = infer_year_from_title(t)
    if y is not None and y>2016 and is_empirical_title(t):
        rows.append({'title':t, 'year':y})

emp_df = pd.DataFrame(rows)
if emp_df.empty:
    out=[]
else:
    cit_df = pd.DataFrame(cit_totals)
    cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)
    merged = emp_df.merge(cit_df, on='title', how='left')
    merged['total_citations'] = merged['total_citations'].fillna(0).astype(int)
    merged = merged.sort_values(['total_citations','title'], ascending=[False, True])
    out = merged[['title','total_citations']].to_dict('records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_yT6VnzVAD5KgNEJfkDcNSIvX': 'file_storage/call_yT6VnzVAD5KgNEJfkDcNSIvX.json', 'var_call_dlKzirn0K8NqiTc2y1I5brDh': 'file_storage/call_dlKzirn0K8NqiTc2y1I5brDh.json'}

exec(code, env_args)
