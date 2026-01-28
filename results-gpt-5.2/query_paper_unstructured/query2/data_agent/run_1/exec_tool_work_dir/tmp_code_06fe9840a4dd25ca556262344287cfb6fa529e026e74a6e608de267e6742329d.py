code = """import json, re
import pandas as pd

# Load citations 2018
path_cit = var_call_MyWDa3zZmfRCtaydwDBHCMml
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
if df_cit.empty:
    out = {"average_citation_count": None, "paper_count": 0}
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')
df_cit = df_cit.dropna(subset=['title','citation_count'])

# Load paper docs and infer ACM source
path_docs = var_call_EbHJziHzSeCKyAig0jBaNBzd
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def infer_source(text: str) -> str:
    if not text:
        return None
    t = text.lower()
    # ACM indicators
    if ('permission to make digital or hard copies' in t and 'acm' in t) or ('acm' in t and 'copyright' in t) or ('acm classification' in t) or ('acm press' in t) or ('acm 978-' in t) or ('10.1145/' in t):
        return 'ACM'
    if 'ieee' in t or '10.1109/' in t:
        return 'IEEE'
    if 'pubmed' in t or 'pmid' in t:
        return 'PubMed'
    return None

rows=[]
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    src = infer_source(d.get('text',''))
    rows.append({'title': title, 'source': src})

df_p = pd.DataFrame(rows)

df = df_cit.merge(df_p, on='title', how='inner')
df_acm = df[df['source']=='ACM']

avg = float(df_acm['citation_count'].mean()) if len(df_acm) else None
out = {
    "average_citation_count": avg,
    "paper_count": int(len(df_acm))
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_MyWDa3zZmfRCtaydwDBHCMml': 'file_storage/call_MyWDa3zZmfRCtaydwDBHCMml.json', 'var_call_EbHJziHzSeCKyAig0jBaNBzd': 'file_storage/call_EbHJziHzSeCKyAig0jBaNBzd.json'}

exec(code, env_args)
