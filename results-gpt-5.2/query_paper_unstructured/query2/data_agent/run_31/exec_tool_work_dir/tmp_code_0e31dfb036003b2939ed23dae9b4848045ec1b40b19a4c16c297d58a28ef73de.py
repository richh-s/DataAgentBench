code = """import json, re, pandas as pd

# Load citations 2018
cit_path = var_call_GhAB3TChXbcRuV5lQ6Jjdagu
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

# Load docs
docs_path = var_call_mHfyw2VR1b56VMK2bsfTMIMT
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

df_cit = pd.DataFrame(cit)
# coerce citation_count to numeric
if 'citation_count' in df_cit.columns:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

def title_from_filename(fn):
    return re.sub(r'\.txt$','',fn).strip() if isinstance(fn,str) else None

df_docs = pd.DataFrame(docs)
df_docs['title'] = df_docs['filename'].apply(title_from_filename)

# identify ACM papers by presence of ACM copyright / permissions / doi domain
acm_pat = re.compile(r'\bACM\b|permissions@acm\.org|doi\.org/10\.1145|Copyright\s*\d{4}\s*©?\s*ACM', re.IGNORECASE)

def is_acm(text):
    if not isinstance(text,str):
        return False
    return bool(acm_pat.search(text))

df_docs['is_acm'] = df_docs['text'].apply(is_acm)

# Join
df = df_cit.merge(df_docs[['title','is_acm']], on='title', how='inner')

df_acm = df[df['is_acm'] == True].copy()
avg_citations = float(df_acm['citation_count'].mean()) if len(df_acm) else None

out = {
    'average_citation_count_2018_for_acm_papers': avg_citations,
    'num_acm_papers_matched': int(df_acm['title'].nunique()),
    'num_citation_records_2018_matched_to_acm': int(len(df_acm))
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_GhAB3TChXbcRuV5lQ6Jjdagu': 'file_storage/call_GhAB3TChXbcRuV5lQ6Jjdagu.json', 'var_call_mHfyw2VR1b56VMK2bsfTMIMT': 'file_storage/call_mHfyw2VR1b56VMK2bsfTMIMT.json'}

exec(code, env_args)
