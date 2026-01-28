code = """import json, re
import pandas as pd

# Load citations 2018
cit_path = var_call_qFNbxon6cc9RWSh8DpneeIYX
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
# normalize types
if 'citation_count' in df_cit.columns:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')
df_cit['title_norm'] = df_cit['title'].astype(str).str.strip()

# Load docs
docs_path = var_call_HT8OXoESbRQgwEYAoGoJB2st
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)
df_docs = pd.DataFrame(docs)

# Extract title from filename
if 'filename' in df_docs.columns:
    df_docs['title'] = df_docs['filename'].astype(str).str.replace(r'\.txt$','', regex=True)
else:
    df_docs['title'] = None

def is_acm(text):
    if text is None:
        return False
    t = str(text)
    # look for typical ACM copyright/permission markers
    pats = [r'\bACM\b', r'permission\s+to\s+make\s+digital\s+or\s+hard\s+copies', r'copyright\s+\d{4}\s*©\s*ACM', r'permissions@acm\.org', r'doi\.org/10\.1145']
    return any(re.search(p, t, flags=re.IGNORECASE) for p in pats)

df_docs['is_acm'] = df_docs['text'].apply(is_acm)
acm_titles = set(df_docs.loc[df_docs['is_acm']==True, 'title'].dropna().astype(str).str.strip().tolist())

# Filter citations to ACM papers
mask = df_cit['title_norm'].isin(acm_titles)
df_acm_cit = df_cit.loc[mask].copy()

avg_cites = float(df_acm_cit['citation_count'].mean()) if len(df_acm_cit)>0 else None
res = {
    'average_citation_count_2018_for_acm_papers': avg_cites,
    'acm_papers_with_2018_citation_records': int(len(df_acm_cit)),
    'total_2018_citation_records': int(len(df_cit))
}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_qFNbxon6cc9RWSh8DpneeIYX': 'file_storage/call_qFNbxon6cc9RWSh8DpneeIYX.json', 'var_call_HT8OXoESbRQgwEYAoGoJB2st': 'file_storage/call_HT8OXoESbRQgwEYAoGoJB2st.json'}

exec(code, env_args)
