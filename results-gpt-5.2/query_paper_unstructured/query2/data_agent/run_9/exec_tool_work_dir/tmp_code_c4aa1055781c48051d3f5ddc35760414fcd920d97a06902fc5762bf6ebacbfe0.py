code = """import json, re
import pandas as pd

# Load citations 2018
cit_path = var_call_jM9O1mahdOheF6xWN2p77YGZ
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
if df_cit.empty:
    out = {"average_citation_count": None, "n_papers": 0}
else:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

# Load paper docs
docs_path = var_call_1cyfjmdrwpGWuhZlxjGI64pI
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

df_docs = pd.DataFrame(docs)
# derive title from filename
if not df_docs.empty:
    df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)
else:
    df_docs['title'] = []

# Identify ACM papers via text contains ACM copyright or '© ACM' or 'Permission to make ... ACM'
acm_pattern = re.compile(r'\bACM\b|©\s*ACM|\(c\)\s*ACM|acm\.org', re.IGNORECASE)

def is_acm_text(t):
    if t is None:
        return False
    return bool(acm_pattern.search(t))

df_docs['is_acm'] = df_docs['text'].apply(is_acm_text)

df_acm = df_docs[df_docs['is_acm']][['title']].drop_duplicates()

# Join and compute mean
if df_cit.empty or df_acm.empty:
    avg = None
    n = 0
else:
    merged = df_cit.merge(df_acm, on='title', how='inner')
    merged = merged.dropna(subset=['citation_count'])
    n = int(merged['title'].nunique())
    avg = float(merged['citation_count'].mean()) if len(merged) else None

out = {"average_citation_count": avg, "n_papers": n}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_jM9O1mahdOheF6xWN2p77YGZ': 'file_storage/call_jM9O1mahdOheF6xWN2p77YGZ.json', 'var_call_1cyfjmdrwpGWuhZlxjGI64pI': 'file_storage/call_1cyfjmdrwpGWuhZlxjGI64pI.json'}

exec(code, env_args)
