code = """import json, re
import pandas as pd

# Load citations 2018
path_cit = var_call_3C5HxXeg6IMqF0ggquNvQvSA
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
if df_cit.empty:
    avg = None
    n = 0
else:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

# Load paper docs with text
path_docs = var_call_WmnyVsW71YEYOmBNrI3pjfmm
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)
df_docs = pd.DataFrame(docs)

def title_from_filename(fn):
    return re.sub(r'\.txt$', '', fn)

def is_acm(text):
    if not isinstance(text, str):
        return False
    t = text.lower()
    # ACM cues: ACM in copyright/classification/permissions
    return ('copyright' in t and 'acm' in t) or ('acm classification keywords' in t) or ('permissions@acm.org' in t) or ('association for computing machinery' in t)

df_docs['title'] = df_docs['filename'].map(title_from_filename)
df_docs['is_acm'] = df_docs['text'].map(is_acm)
acm_titles = set(df_docs.loc[df_docs['is_acm'], 'title'].dropna().tolist())

if df_cit.empty:
    avg = None
    n = 0
else:
    df_join = df_cit[df_cit['title'].isin(acm_titles)].copy()
    n = int(df_join.shape[0])
    avg = float(df_join['citation_count'].mean()) if n and df_join['citation_count'].notna().any() else None

out = {
    'average_citation_count_2018_acm': avg,
    'num_papers': n
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_3C5HxXeg6IMqF0ggquNvQvSA': 'file_storage/call_3C5HxXeg6IMqF0ggquNvQvSA.json', 'var_call_k0YcfaJa7A9GadwF6P8Unkxl': 'file_storage/call_k0YcfaJa7A9GadwF6P8Unkxl.json', 'var_call_WmnyVsW71YEYOmBNrI3pjfmm': 'file_storage/call_WmnyVsW71YEYOmBNrI3pjfmm.json'}

exec(code, env_args)
