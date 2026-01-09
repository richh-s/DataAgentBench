code = """import json, pandas as pd, re
from pathlib import Path

# Load citations 2018
p_cit = Path(var_call_Yqge2vWKsKCcu0uXhnbObYDp)
with p_cit.open('r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
if df_cit.empty:
    out = {"average_citation_count_acm_cited_2018": None, "num_papers": 0}
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')
df_cit = df_cit.dropna(subset=['title','citation_count'])

# Load paper docs
p_docs = Path(var_call_4YjYtlCmVGfuXx90LhUQCAHz)
with p_docs.open('r', encoding='utf-8') as f:
    docs = json.load(f)
df_docs = pd.DataFrame(docs)
if df_docs.empty:
    out = {"average_citation_count_acm_cited_2018": None, "num_papers": 0}
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

def is_acm(text):
    if not isinstance(text, str):
        return False
    t = text.lower()
    # look for common ACM copyright / permissions markers
    patterns = [
        r'copyright\s*\d{4}\s*[©\(]?\s*acm',
        r'permission\s+to\s+make\s+digital\s+or\s+hard\s+copies.*acm',
        r'http://dx\.doi\.org/10\.1145/',
        r'doi\.org/10\.1145/',
        r'acm\s+classification\s+keywords',
        r'\bproceedings\s+of\s+the\s+acm\b',
    ]
    return any(re.search(p, t, flags=re.DOTALL) for p in patterns)

df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)
df_docs['is_acm'] = df_docs['text'].apply(is_acm)

df_join = df_cit.merge(df_docs[['title','is_acm']], on='title', how='inner')
df_acm = df_join[df_join['is_acm'] == True]

avg = float(df_acm['citation_count'].mean()) if len(df_acm) else None
out = {"average_citation_count_acm_cited_2018": avg, "num_papers": int(len(df_acm))}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Yqge2vWKsKCcu0uXhnbObYDp': 'file_storage/call_Yqge2vWKsKCcu0uXhnbObYDp.json', 'var_call_4YjYtlCmVGfuXx90LhUQCAHz': 'file_storage/call_4YjYtlCmVGfuXx90LhUQCAHz.json'}

exec(code, env_args)
