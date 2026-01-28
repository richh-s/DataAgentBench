code = """import json, pandas as pd, re

# Load citations 2018
path_cit = var_call_isGIrpmFn1quHJyzOKacXCKq
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

# Load paper docs
path_docs = var_call_ALTvStGwf8B8AF3ZaErGsFf5
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

df_docs = pd.DataFrame(docs)
df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)

# Heuristic for ACM source: presence of ACM copyright/doi or 'Permission to make digital or hard copies' etc.
pat = re.compile(r"\bACM\b|acm\.org|doi\.org/10\.1145|Association for Computing Machinery", re.IGNORECASE)
df_docs['is_acm'] = df_docs['text'].fillna('').apply(lambda t: bool(pat.search(t)))
acm_titles = set(df_docs.loc[df_docs['is_acm'], 'title'])

# Filter citations to ACM papers
acm_cit = df_cit[df_cit['title'].isin(acm_titles)].copy()
avg_val = float(acm_cit['citation_count'].mean()) if len(acm_cit)>0 else None

out = {
    'avg_citation_count_2018_for_acm_papers': avg_val,
    'num_acm_papers_with_2018_citations': int(acm_cit['title'].nunique()),
    'num_records_2018_matched': int(len(acm_cit))
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_isGIrpmFn1quHJyzOKacXCKq': 'file_storage/call_isGIrpmFn1quHJyzOKacXCKq.json', 'var_call_ALTvStGwf8B8AF3ZaErGsFf5': 'file_storage/call_ALTvStGwf8B8AF3ZaErGsFf5.json'}

exec(code, env_args)
