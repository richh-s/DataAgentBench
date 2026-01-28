code = """import json, pandas as pd

# Load citations 2018
path_cit = var_call_47OfNYZWSPMXJNieBRPJSzgP
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

# Load paper docs
path_docs = var_call_BUP3CPFdc6ehd9XGSFdXtGXC
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

df_docs = pd.DataFrame(docs)
df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)

# Identify ACM source papers via text containing 'copyright' and 'acm' or 'acm ' occurrences
text_l = df_docs['text'].str.lower()
acm_mask = text_l.str.contains('acm', na=False)
# reduce false positives by requiring typical ACM copyright/permissions markers
acm_mask = acm_mask & (text_l.str.contains('permissions@acm.org', na=False) | text_l.str.contains('copyright', na=False) | text_l.str.contains('acm classification', na=False) | text_l.str.contains('doi.org/10.1145', na=False) | text_l.str.contains('association for computing machinery', na=False))

acm_titles = set(df_docs.loc[acm_mask, 'title'].dropna().tolist())

# Filter citations for those titles and compute average
filtered = df_cit[df_cit['title'].isin(acm_titles)].copy()
avg_val = float(filtered['citation_count'].mean()) if len(filtered) else None

out = {
    'avg_citation_count': avg_val,
    'citation_year': 2018,
    'acm_paper_count_matched': int(filtered.shape[0])
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_47OfNYZWSPMXJNieBRPJSzgP': 'file_storage/call_47OfNYZWSPMXJNieBRPJSzgP.json', 'var_call_BUP3CPFdc6ehd9XGSFdXtGXC': 'file_storage/call_BUP3CPFdc6ehd9XGSFdXtGXC.json'}

exec(code, env_args)
