code = """import json, re
import pandas as pd

# Load mongo docs
path_docs = var_call_dPoUNT5xhNGGm3c8MaJEw98c
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def infer_domain(text):
    t = text.lower()
    # heuristic keywords for physical activity domain
    kws = [
        'physical activity', 'activity tracker', 'fitness tracker', 'step', 'steps',
        'exercise', 'workout', 'walking', 'run', 'running', 'gym', 'sedentary',
        'mvpa', 'moderate-to-vigorous', 'accelerometer'
    ]
    return any(k in t for k in kws)

def infer_year(text):
    # look for typical publication year patterns near top; fallback any 4-digit 20xx
    # Prefer 2016 if present as standalone.
    if re.search(r'\b2016\b', text):
        return 2016
    m = re.search(r'\b(20\d{2})\b', text)
    return int(m.group(1)) if m else None

rows = []
for d in docs:
    title = d.get('filename','')
    if title.lower().endswith('.txt'):
        title = title[:-4]
    text = d.get('text','')
    year = infer_year(text)
    if year == 2016 and infer_domain(text):
        rows.append({'title': title})

# citations totals
cit = pd.DataFrame(var_call_07x0yUYHFpKHUO0aSEKZ8XxZ)
if not cit.empty:
    cit['total_citations'] = cit['total_citations'].astype(int)

papers = pd.DataFrame(rows).drop_duplicates()
res = papers.merge(cit, on='title', how='left')
res['total_citations'] = res['total_citations'].fillna(0).astype(int)
res = res.sort_values(['total_citations','title'], ascending=[False, True])

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_dPoUNT5xhNGGm3c8MaJEw98c': 'file_storage/call_dPoUNT5xhNGGm3c8MaJEw98c.json', 'var_call_07x0yUYHFpKHUO0aSEKZ8XxZ': 'file_storage/call_07x0yUYHFpKHUO0aSEKZ8XxZ.json'}

exec(code, env_args)
