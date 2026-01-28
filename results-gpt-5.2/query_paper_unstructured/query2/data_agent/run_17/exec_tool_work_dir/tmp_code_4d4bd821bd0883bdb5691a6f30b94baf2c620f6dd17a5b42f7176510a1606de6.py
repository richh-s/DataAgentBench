code = """import json, re
import pandas as pd

# Load citations 2018
cit_path = var_call_9BT0BNiohMZNNrqpRgleJ7lv
with open(cit_path,'r',encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
# normalize types
if 'citation_count' in df_cit.columns:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

def title_from_filename(fn):
    if fn is None:
        return None
    return re.sub(r'\.txt$','',fn)

def is_acm(text):
    if not text:
        return False
    t = text.lower()
    # common ACM markers in PDFs converted to text
    return ('permission to make digital or hard copies' in t and 'acm' in t) or ('copyright' in t and 'acm' in t) or ('acm classification' in t) or ('acm press' in t) or ('association for computing machinery' in t)

# Load docs
docs_path = var_call_ejbU6bZp0toDfbi4jq7ihuGd
with open(docs_path,'r',encoding='utf-8') as f:
    docs = json.load(f)

df_docs = pd.DataFrame(docs)
df_docs['title'] = df_docs['filename'].map(title_from_filename)
df_docs['is_acm'] = df_docs['text'].map(is_acm)
acm_titles = set(df_docs.loc[df_docs['is_acm'], 'title'].dropna().tolist())

# filter citations to ACM titles
acm_cit = df_cit[df_cit['title'].isin(acm_titles)].copy()
avg = float(acm_cit['citation_count'].mean()) if len(acm_cit)>0 else None
out = {
    'average_citation_count_2018_for_acm_papers': avg,
    'num_acm_papers_with_2018_citations': int(acm_cit['title'].nunique()),
    'num_citation_rows': int(len(acm_cit))
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_9BT0BNiohMZNNrqpRgleJ7lv': 'file_storage/call_9BT0BNiohMZNNrqpRgleJ7lv.json', 'var_call_ejbU6bZp0toDfbi4jq7ihuGd': 'file_storage/call_ejbU6bZp0toDfbi4jq7ihuGd.json'}

exec(code, env_args)
