code = """import json, re
import pandas as pd

# Load citations 2018
cit_path = var_call_uDE97E423ZjP0bPuyi6V9Ktk
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
if df_cit.empty:
    out = {"average_citation_count": None, "paper_count": 0}
else:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

# Load paper docs
paper_path = var_call_f3lCuPD7hZGps1A7VMUQzU86
with open(paper_path, 'r', encoding='utf-8') as f:
    papers = json.load(f)

df_p = pd.DataFrame(papers)
if df_p.empty:
    out = {"average_citation_count": None, "paper_count": 0}
else:
    df_p['title'] = df_p['filename'].str.replace(r'\.txt$', '', regex=True)
    # Identify ACM source by presence of ACM copyright/classification/doi strings
    acm_pat = re.compile(r'\bACM\b|permissions@acm\.org|doi\.org/10\.1145', re.IGNORECASE)
    df_p['is_acm'] = df_p['text'].fillna('').apply(lambda t: bool(acm_pat.search(t)))

    df_join = df_cit.merge(df_p.loc[df_p['is_acm'], ['title']], on='title', how='inner')
    avg = float(df_join['citation_count'].mean()) if not df_join.empty else None
    out = {"average_citation_count": avg, "paper_count": int(df_join.shape[0])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_uDE97E423ZjP0bPuyi6V9Ktk': 'file_storage/call_uDE97E423ZjP0bPuyi6V9Ktk.json', 'var_call_f3lCuPD7hZGps1A7VMUQzU86': 'file_storage/call_f3lCuPD7hZGps1A7VMUQzU86.json'}

exec(code, env_args)
