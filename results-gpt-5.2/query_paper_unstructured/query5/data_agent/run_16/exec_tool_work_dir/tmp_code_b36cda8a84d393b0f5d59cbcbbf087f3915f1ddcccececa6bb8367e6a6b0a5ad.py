code = """import json, re
import pandas as pd

# load citations 2020
cit_path = var_call_STqGzPnRb9GKunhuCq6wMhct
with open(cit_path, 'r', encoding='utf-8') as f:
    cits = json.load(f)

df_cit = pd.DataFrame(cits)
# coerce counts
if 'citation_count' in df_cit.columns:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)

# load docs
docs_path = var_call_TvfDFOZ5tdhkNuMw0nolpZhO
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

df_docs = pd.DataFrame(docs)
# title from filename
df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)

# venue extraction heuristic: look for CHI in first ~2000 chars, including variants
chi_re = re.compile(r"\bCHI\b(?:\s*'\d{2})?|\bCHI\s+Conference\b|\bSIGCHI\b", re.IGNORECASE)

def is_chi(text):
    if not isinstance(text, str):
        return False
    head = text[:4000]
    return bool(chi_re.search(head))

df_docs['is_chi'] = df_docs['text'].apply(is_chi)

# join with citations and filter CHI
chi_titles = set(df_docs.loc[df_docs['is_chi'], 'title'])
df_chi_cit = df_cit[df_cit['title'].isin(chi_titles)].copy()

# aggregate total citations in 2020 for CHI-presented papers
result_total = int(df_chi_cit['citation_count'].sum())

out = {
    "total_citations_2020_for_CHI_papers": result_total,
    "num_CHI_papers_with_citations_in_2020": int(df_chi_cit['title'].nunique()),
    "num_citation_records_matched": int(len(df_chi_cit))
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_STqGzPnRb9GKunhuCq6wMhct': 'file_storage/call_STqGzPnRb9GKunhuCq6wMhct.json', 'var_call_TvfDFOZ5tdhkNuMw0nolpZhO': 'file_storage/call_TvfDFOZ5tdhkNuMw0nolpZhO.json'}

exec(code, env_args)
