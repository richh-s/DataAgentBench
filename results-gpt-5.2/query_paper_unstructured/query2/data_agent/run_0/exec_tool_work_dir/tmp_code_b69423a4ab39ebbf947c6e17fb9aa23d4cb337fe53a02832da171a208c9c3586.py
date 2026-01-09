code = """import json, pandas as pd, re

# Load citations 2018
path_cit = var_call_QfVF2D5znV6e6AK159yJ30Ve
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
# ensure numeric
df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

# Load paper docs
path_docs = var_call_V14Ua7t5AVCP29OvCjM6AnBu
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)
df_docs = pd.DataFrame(docs)

def is_acm(text: str) -> bool:
    if not isinstance(text, str):
        return False
    t = text.lower()
    return ('permission' in t and 'acm' in t) or ('copyright' in t and 'acm' in t) or ('© acm' in t) or ('(c) acm' in t)

df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)
df_docs['is_acm'] = df_docs['text'].map(is_acm)
acm_titles = set(df_docs.loc[df_docs['is_acm'], 'title'].dropna().tolist())

# Filter citations to ACM papers
acm_cit_2018 = df_cit[df_cit['title'].isin(acm_titles)].copy()
avg = float(acm_cit_2018['citation_count'].mean()) if len(acm_cit_2018)>0 else None

out = {
    'average_citation_count_2018_acm_papers': avg,
    'num_acm_papers_with_citations_2018': int(acm_cit_2018['title'].nunique()),
    'num_citation_records_2018_acm': int(len(acm_cit_2018))
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_QfVF2D5znV6e6AK159yJ30Ve': 'file_storage/call_QfVF2D5znV6e6AK159yJ30Ve.json', 'var_call_V14Ua7t5AVCP29OvCjM6AnBu': 'file_storage/call_V14Ua7t5AVCP29OvCjM6AnBu.json'}

exec(code, env_args)
