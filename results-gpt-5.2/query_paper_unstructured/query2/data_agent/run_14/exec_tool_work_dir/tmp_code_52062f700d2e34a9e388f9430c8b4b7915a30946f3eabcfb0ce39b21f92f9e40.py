code = """import json, re
import pandas as pd

# Load citations 2018
cit_path = var_call_V839uacQr0XshgiDyJIW124m
with open(cit_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

df_cit = pd.DataFrame(citations)
if df_cit.empty:
    out = {"avg_citation_count": None, "n_papers": 0}
else:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

# Load paper docs
docs_path = var_call_w95yZxzgB6ibjY4GLKuH3XcV
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Identify ACM papers by presence of ACM copyright/classification/doi pattern
acm_titles = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = (d.get('text') or '')
    t = text.lower()
    is_acm = (
        ('© acm' in t) or ('permission to make digital or hard copies' in t and 'acm' in t) or
        ('acm classification' in t) or ('acm 978-' in t) or ('dl.acm.org' in t) or ('doi.org/10.1145' in t) or
        ('10.1145/' in t)
    )
    if is_acm:
        acm_titles.append(title)

acm_set = set(acm_titles)

df_join = df_cit[df_cit['title'].isin(acm_set)].copy()
avg_val = None
n = int(df_join['citation_count'].notna().sum()) if not df_join.empty else 0
if n > 0:
    avg_val = float(df_join['citation_count'].mean())

out = {"avg_citation_count": avg_val, "n_papers": n}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_V839uacQr0XshgiDyJIW124m': 'file_storage/call_V839uacQr0XshgiDyJIW124m.json', 'var_call_w95yZxzgB6ibjY4GLKuH3XcV': 'file_storage/call_w95yZxzgB6ibjY4GLKuH3XcV.json'}

exec(code, env_args)
