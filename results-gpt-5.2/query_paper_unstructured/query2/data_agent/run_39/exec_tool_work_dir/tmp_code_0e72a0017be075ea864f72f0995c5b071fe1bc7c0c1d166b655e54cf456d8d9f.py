code = """import json, re
import pandas as pd

# Load citations 2018
path_cit = var_call_JTsbOOxVsemjuiAJ63u79YJ1
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
if df_cit.empty:
    out = {"average_citation_count": None, "n_papers": 0}
else:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

# Load paper docs
path_docs = var_call_TlrRbKsrnxFZ0Ew1YbuhEQkd
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)
df_docs = pd.DataFrame(docs)

# Extract title and source (ACM) using regex
if not df_docs.empty:
    df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$','', regex=True)
    # Detect ACM publisher mentions
    acm_re = re.compile(r'\bACM\b|Association for Computing Machinery|acm\.org', re.IGNORECASE)
    df_docs['is_acm'] = df_docs['text'].apply(lambda t: bool(acm_re.search(t or '')))
else:
    df_docs['title'] = []
    df_docs['is_acm'] = []

# Join on title
if df_cit.empty or df_docs.empty:
    avg = None
    n = 0
else:
    df_join = df_cit.merge(df_docs[['title','is_acm']], on='title', how='inner')
    df_acm = df_join[df_join['is_acm']].copy()
    avg = float(df_acm['citation_count'].mean()) if len(df_acm) else None
    n = int(len(df_acm))

out = {"average_citation_count": avg, "n_papers": n}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_iDiQx4H1fe1IbzDXQSYzft0C': ['Citations', 'sqlite_sequence'], 'var_call_JTsbOOxVsemjuiAJ63u79YJ1': 'file_storage/call_JTsbOOxVsemjuiAJ63u79YJ1.json', 'var_call_TlrRbKsrnxFZ0Ew1YbuhEQkd': 'file_storage/call_TlrRbKsrnxFZ0Ew1YbuhEQkd.json'}

exec(code, env_args)
