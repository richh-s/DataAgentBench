code = """import json, re
import pandas as pd

# load citations 2018
path_cit = var_call_1lsflZXPrOlLE3ug5uv1Kchf
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
if df_cit.empty:
    out = {"average_citation_count": None, "n_papers": 0}
else:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

# load paper docs with ACM in text
path_docs = var_call_WE113ozVza5wA9N2cxgbTQP4
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# determine which docs are ACM published based on copyright / permission lines
acm_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = re.sub(r'\.txt$','',fn)
    text = d.get('text','')
    t = text.lower()
    is_acm = ('copyright' in t and 'acm' in t) or ('permission' in t and 'acm' in t) or ('acm classification' in t)
    if is_acm:
        acm_titles.add(title)

# filter citations to those titles
if df_cit.empty:
    avg = None
    n = 0
else:
    df_acm = df_cit[df_cit['title'].isin(acm_titles)].copy()
    n = int(df_acm['title'].nunique())
    avg = float(df_acm['citation_count'].mean()) if len(df_acm) else None

out = {"average_citation_count": avg, "n_papers": n}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1lsflZXPrOlLE3ug5uv1Kchf': 'file_storage/call_1lsflZXPrOlLE3ug5uv1Kchf.json', 'var_call_AcwbKbWSzur9YzPI8VCKMsad': 'file_storage/call_AcwbKbWSzur9YzPI8VCKMsad.json', 'var_call_WE113ozVza5wA9N2cxgbTQP4': 'file_storage/call_WE113ozVza5wA9N2cxgbTQP4.json'}

exec(code, env_args)
