code = """import json, re
import pandas as pd

# Load mongo docs
path_docs = var_call_dPoUNT5xhNGGm3c8MaJEw98c
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def infer_domain(text):
    t = (text or '').lower()
    kws = ['physical activity','activity tracker','fitness tracker','exercise','workout','walking','running','gym','sedentary','accelerometer','step count','steps']
    return any(k in t for k in kws)

def infer_year(text):
    if not text:
        return None
    if re.search(r'\b2016\b', text):
        return 2016
    m = re.search(r'\b(20\d{2})\b', text)
    return int(m.group(1)) if m else None

rows = []
for d in docs:
    title = (d.get('filename') or '')
    if title.lower().endswith('.txt'):
        title = title[:-4]
    year = infer_year(d.get('text'))
    if year == 2016 and infer_domain(d.get('text')):
        rows.append({'title': title})

papers = pd.DataFrame(rows).drop_duplicates()

cit_obj = var_call_07x0yUYHFpKHUO0aSEKZ8XxZ
if isinstance(cit_obj, list):
    cit = pd.DataFrame(cit_obj)
else:
    cit = pd.DataFrame([])

if not cit.empty:
    cit['total_citations'] = cit['total_citations'].astype(int)

if papers.empty:
    out = []
else:
    res = papers.merge(cit, on='title', how='left')
    res['total_citations'] = res.get('total_citations', 0)
    res['total_citations'] = res['total_citations'].fillna(0).astype(int)
    res = res.sort_values(['total_citations','title'], ascending=[False, True])
    out = res.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_dPoUNT5xhNGGm3c8MaJEw98c': 'file_storage/call_dPoUNT5xhNGGm3c8MaJEw98c.json', 'var_call_07x0yUYHFpKHUO0aSEKZ8XxZ': 'file_storage/call_07x0yUYHFpKHUO0aSEKZ8XxZ.json'}

exec(code, env_args)
