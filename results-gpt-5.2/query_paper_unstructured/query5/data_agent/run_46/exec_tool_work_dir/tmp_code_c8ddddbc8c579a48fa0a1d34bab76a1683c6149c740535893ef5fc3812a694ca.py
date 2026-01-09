code = """import json, re
import pandas as pd

# Load citations 2020
path_cit = var_call_SzvnF6fQlofprebTtfEIA7FJ
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
# ensure numeric
if 'citation_count' in df_cit.columns:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)

# Load paper docs
path_docs = var_call_rmlp8nu53dU2sywFXl8npTNL
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

df_docs = pd.DataFrame(docs)
df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$','', regex=True)

# Heuristic venue extraction: look for 'CHI' token near top
chi_pat = re.compile(r"\bCHI\b", re.IGNORECASE)

def is_chi(text):
    if not isinstance(text, str):
        return False
    head = text[:2000]
    return bool(chi_pat.search(head))

df_docs['is_chi'] = df_docs['text'].apply(is_chi)
chi_titles = set(df_docs.loc[df_docs['is_chi'], 'title'].dropna().tolist())

# Filter citations to CHI titles and sum
mask = df_cit['title'].isin(chi_titles)
total = int(df_cit.loc[mask, 'citation_count'].sum())

print('__RESULT__:')
print(json.dumps({'total_citations_2020_for_CHI_papers': total, 'num_CHI_papers_with_citations_2020': int(df_cit.loc[mask,'title'].nunique()), 'num_CHI_papers_in_docs': int(len(chi_titles))}))"""

env_args = {'var_call_SzvnF6fQlofprebTtfEIA7FJ': 'file_storage/call_SzvnF6fQlofprebTtfEIA7FJ.json', 'var_call_rmlp8nu53dU2sywFXl8npTNL': 'file_storage/call_rmlp8nu53dU2sywFXl8npTNL.json'}

exec(code, env_args)
