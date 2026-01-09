code = """import json, pandas as pd, re

# Load citations 2020
cit_path = var_call_QZjYCZ9OZ4pVTag9MK7OoHD3
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)

# Load paper docs
docs_path = var_call_P0M8IRlJNfKBrujTsIrkOlc2
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)
df_docs = pd.DataFrame(docs)

def is_chi(text: str) -> bool:
    if not isinstance(text, str):
        return False
    # detect CHI in venue line like "CHI 'YY" or "CHI 20XX"; avoid matching within words
    return re.search(r"\bCHI\b", text) is not None

df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)
df_docs['is_chi'] = df_docs['text'].map(is_chi)
chi_titles = set(df_docs.loc[df_docs['is_chi'], 'title'].dropna().tolist())

# Join and sum
chi_cit_2020 = df_cit[df_cit['title'].isin(chi_titles)]
result = {
    'num_chi_papers_with_citations_in_2020': int(chi_cit_2020.shape[0]),
    'total_citations_2020_for_chi_papers': int(chi_cit_2020['citation_count'].sum())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_QZjYCZ9OZ4pVTag9MK7OoHD3': 'file_storage/call_QZjYCZ9OZ4pVTag9MK7OoHD3.json', 'var_call_P0M8IRlJNfKBrujTsIrkOlc2': 'file_storage/call_P0M8IRlJNfKBrujTsIrkOlc2.json'}

exec(code, env_args)
