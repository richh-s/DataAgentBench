code = """import json, pandas as pd

# Load citations 2018
path_cit = var_call_n62rki6dMjdOPSiDD3KKHEuM
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

# Load paper docs
path_docs = var_call_ptp8xV9i2vjbWxoh7gsNIS4q
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)
df_docs = pd.DataFrame(docs)

def is_acm(text):
    if not isinstance(text, str):
        return False
    t = text.lower()
    # Look for strong ACM publisher indicators
    keys = [
        'association for computing machinery',
        'permissions@acm.org',
        'acm 978',
        'copyright'  # combined with acm checked below
    ]
    if 'acm' in t:
        if any(k in t for k in keys):
            return True
        # also common header lines
        if 'copyright' in t and 'acm' in t:
            return True
    return False

df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)
df_docs['is_acm'] = df_docs['text'].apply(is_acm)
acm_titles = set(df_docs.loc[df_docs['is_acm'], 'title'].dropna().tolist())

# Join/filter citations for ACM papers
acm_cit_2018 = df_cit[df_cit['title'].isin(acm_titles)].copy()
avg_val = float(acm_cit_2018['citation_count'].mean()) if len(acm_cit_2018)>0 else None

out = {
    'average_citation_count_2018_for_acm_papers': avg_val,
    'acm_papers_with_2018_citation_records': int(len(acm_cit_2018))
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_n62rki6dMjdOPSiDD3KKHEuM': 'file_storage/call_n62rki6dMjdOPSiDD3KKHEuM.json', 'var_call_ptp8xV9i2vjbWxoh7gsNIS4q': 'file_storage/call_ptp8xV9i2vjbWxoh7gsNIS4q.json'}

exec(code, env_args)
