code = """import json, re
import pandas as pd

cit_path = var_call_ITUlFgkZFdLRo26sQZf42O2p
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
df_cit['citations_2020'] = pd.to_numeric(df_cit['citations_2020'], errors='coerce').fillna(0).astype(int)

docs_path = var_call_496QFZUM6xsMCwaNPJXq409X
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)
df_docs = pd.DataFrame(docs)

def infer_venue(txt):
    if not isinstance(txt, str):
        return None
    t = txt[:3000].upper()
    if re.search(r"\bCHI\s*\d{4}\b", t):
        return 'CHI'
    if re.search(r"\bCHI\s*'\d{2}\b", t):
        return 'CHI'
    if 'SIGCHI' in t or 'SIG CHI' in t:
        return 'CHI'
    if 'PROCEEDINGS OF THE SIGCHI CONFERENCE' in t:
        return 'CHI'
    return None

df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)
df_docs['venue_inferred'] = df_docs['text'].apply(infer_venue)

merged = df_cit.merge(df_docs[['title','venue_inferred']], on='title', how='inner')
chi = merged[merged['venue_inferred'] == 'CHI']

result = {
    'total_citations_2020_for_CHI_papers': int(chi['citations_2020'].sum()),
    'num_CHI_papers_cited_in_2020': int((chi['citations_2020'] > 0).sum()),
    'num_CHI_papers_matched': int(len(chi))
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ITUlFgkZFdLRo26sQZf42O2p': 'file_storage/call_ITUlFgkZFdLRo26sQZf42O2p.json', 'var_call_496QFZUM6xsMCwaNPJXq409X': 'file_storage/call_496QFZUM6xsMCwaNPJXq409X.json'}

exec(code, env_args)
