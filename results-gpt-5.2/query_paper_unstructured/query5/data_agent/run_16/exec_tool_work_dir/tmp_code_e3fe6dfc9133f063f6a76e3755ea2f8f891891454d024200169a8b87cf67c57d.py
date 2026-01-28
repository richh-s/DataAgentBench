code = """import json, re
import pandas as pd

# load citations 2020
cit_path = var_call_STqGzPnRb9GKunhuCq6wMhct
with open(cit_path, 'r', encoding='utf-8') as f:
    cits = json.load(f)
df_cit = pd.DataFrame(cits)
df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)

# load docs
path = var_call_TvfDFOZ5tdhkNuMw0nolpZhO
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)
df_docs = pd.DataFrame(docs)
df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)

# broader CHI detection: any occurrence of CHI in first 10000 chars
chi_re = re.compile(r"\bCHI\b|\bSIGCHI\b", re.IGNORECASE)

def is_chi(text):
    if not isinstance(text, str):
        return False
    head = text[:12000]
    return bool(chi_re.search(head))

df_docs['is_chi'] = df_docs['text'].apply(is_chi)

chi_titles = set(df_docs.loc[df_docs['is_chi'], 'title'])
matched = df_cit[df_cit['title'].isin(chi_titles)].copy()

out = {
    'docs_total': int(len(df_docs)),
    'docs_chi_detected': int(df_docs['is_chi'].sum()),
    'cit2020_total_records': int(len(df_cit)),
    'cit2020_matched_records': int(len(matched)),
    'cit2020_matched_unique_titles': int(matched['title'].nunique()),
    'sample_chi_titles': list(sorted(list(chi_titles))[:20]),
    'sample_matched_titles': list(matched['title'].head(20))
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_STqGzPnRb9GKunhuCq6wMhct': 'file_storage/call_STqGzPnRb9GKunhuCq6wMhct.json', 'var_call_TvfDFOZ5tdhkNuMw0nolpZhO': 'file_storage/call_TvfDFOZ5tdhkNuMw0nolpZhO.json', 'var_call_83A03zmgFzU2tzoZuUErtWgr': {'total_citations_2020_for_CHI_papers': 0, 'num_CHI_papers_with_citations_in_2020': 0, 'num_citation_records_matched': 0}}

exec(code, env_args)
