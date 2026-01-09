code = """import json, re
import pandas as pd

# load citations 2018
path_cit = var_call_Y3wGKhdbYQLKhFY8gYokwgOF
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
if df_cit.empty:
    avg = None
else:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

# load paper docs
path_docs = var_call_ChWAArdJfbJdSqXrTKy67PQd
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)
df_docs = pd.DataFrame(docs)

def is_acm(text):
    if not isinstance(text, str):
        return False
    t = text
    # common ACM signals
    patterns = [
        r'\bAssociation for Computing Machinery\b',
        r'\bACM\b',
        r'Copyright\s*\d{4}\s*\u00a9\s*ACM',
        r'permissions@acm\.org',
        r'\bACM Classification Keywords\b',
        r'\bProceedings of the ACM\b'
    ]
    return any(re.search(p, t, flags=re.IGNORECASE) for p in patterns)

df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)
df_docs['is_acm'] = df_docs['text'].apply(is_acm)
df_acm_titles = df_docs.loc[df_docs['is_acm'], ['title']].drop_duplicates()

# join
if df_cit.empty:
    avg_acm_2018 = None
    n = 0
else:
    df_join = df_cit.merge(df_acm_titles, on='title', how='inner')
    n = int(df_join['citation_count'].notna().sum())
    avg_acm_2018 = float(df_join['citation_count'].mean()) if n>0 else None

out = {"average_citation_count": avg_acm_2018, "num_acm_papers_matched": n, "citation_year": 2018}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Y3wGKhdbYQLKhFY8gYokwgOF': 'file_storage/call_Y3wGKhdbYQLKhFY8gYokwgOF.json', 'var_call_ChWAArdJfbJdSqXrTKy67PQd': 'file_storage/call_ChWAArdJfbJdSqXrTKy67PQd.json'}

exec(code, env_args)
