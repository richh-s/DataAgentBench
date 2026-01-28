code = """import json, re
import pandas as pd

# Load citations 2020
path = var_call_igDrrn9boSe6hpcUsJwXKVXG
with open(path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
if df_cit.empty:
    out = {"total_citations_2020_for_CHI_papers": 0, "num_CHI_papers_cited_in_2020": 0}
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)

# Load paper docs
path2 = var_call_SNpQUFmR87tJn0zGb3F76gGX
with open(path2, 'r', encoding='utf-8') as f:
    docs = json.load(f)

df_docs = pd.DataFrame(docs)

def norm_title(s):
    if s is None:
        return ''
    s = re.sub(r'\s+', ' ', str(s)).strip()
    return s.casefold()

# derive title from filename
if 'filename' in df_docs.columns:
    df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)
else:
    df_docs['title'] = ''

df_docs['title_norm'] = df_docs['title'].map(norm_title)

def is_chi(text):
    if not isinstance(text, str):
        return False
    t = text.casefold()
    # match CHI proceedings patterns
    return ("chi " in t) or ("chi'" in t) or ("chi ’" in t) or ("proceedings of the sigchi" in t) or ("sigchi" in t)

# more robust: look for standalone CHI in header lines
chi_mask = df_docs['text'].apply(lambda x: bool(re.search(r'\bchi\b', x, flags=re.IGNORECASE)))
# but avoid matching within words; regex already

df_chi = df_docs[chi_mask].copy()

# Join

df_cit['title_norm'] = df_cit['title'].map(norm_title)
merged = df_cit.merge(df_chi[['title_norm','title']], on='title_norm', how='inner')

out = {
    "total_citations_2020_for_CHI_papers": int(merged['citation_count'].sum()),
    "num_CHI_papers_cited_in_2020": int(merged['title_norm'].nunique()),
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_BlIIEiROmlTIvUTWbDqLHOqp': [{'total_citations_2020': '9576'}], 'var_call_igDrrn9boSe6hpcUsJwXKVXG': 'file_storage/call_igDrrn9boSe6hpcUsJwXKVXG.json', 'var_call_SNpQUFmR87tJn0zGb3F76gGX': 'file_storage/call_SNpQUFmR87tJn0zGb3F76gGX.json'}

exec(code, env_args)
