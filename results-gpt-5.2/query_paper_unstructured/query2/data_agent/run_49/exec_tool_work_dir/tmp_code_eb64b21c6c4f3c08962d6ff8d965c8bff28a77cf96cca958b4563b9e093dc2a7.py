code = """import json, re, pandas as pd
from pathlib import Path

# Load citations 2018
cit_path = var_call_IUCuvoUwBTiz5nxJP8aTJVDY
cit = json.loads(Path(cit_path).read_text())
dfc = pd.DataFrame(cit)
dfc['citation_count'] = pd.to_numeric(dfc['citation_count'], errors='coerce')
dfc = dfc.dropna(subset=['title','citation_count'])

# Load paper docs
docs_path = var_call_1DiL3Pc6wGroByOA2azUWRC9
docs = json.loads(Path(docs_path).read_text())
dfd = pd.DataFrame(docs)

def is_acm(text):
    if not isinstance(text, str):
        return False
    t = text.lower()
    # common ACM indicators
    if 'association for computing machinery' in t:
        return True
    if '© acm' in t or '(c) acm' in t or 'copyright' in t and 'acm' in t:
        return True
    if 'acm classification keywords' in t:
        return True
    if 'acm press' in t:
        return True
    if 'acm,' in t and 'permission to make digital or hard copies' in t:
        return True
    if 'acm 978-' in t or 'acm 979-' in t:
        return True
    if 'dl.acm.org' in t or 'doi.org/10.1145' in t:
        return True
    return False

dfd['title'] = dfd['filename'].str.replace(r'\.txt$','', regex=True)
dfd['is_acm'] = dfd['text'].apply(is_acm)
acm_titles = set(dfd.loc[dfd['is_acm'], 'title'].dropna().tolist())

# Join and compute mean for ACM
acm_cites_2018 = dfc[dfc['title'].isin(acm_titles)]['citation_count']
avg = float(acm_cites_2018.mean()) if len(acm_cites_2018) else None
n = int(acm_cites_2018.shape[0])

out = {'average_citation_count_2018_acm': avg, 'paper_count': n}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_IUCuvoUwBTiz5nxJP8aTJVDY': 'file_storage/call_IUCuvoUwBTiz5nxJP8aTJVDY.json', 'var_call_1DiL3Pc6wGroByOA2azUWRC9': 'file_storage/call_1DiL3Pc6wGroByOA2azUWRC9.json'}

exec(code, env_args)
