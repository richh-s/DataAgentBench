code = """import json, re, pandas as pd

# Load citations 2020
path_cit = var_call_qFkSnbDyNpOvsonbQrfkzSQb
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
# ensure numeric
if not df_cit.empty:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)

# Load paper docs
path_docs = var_call_g7wg3q1JUJXRLPOjzZpvzpmg
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)
df_docs = pd.DataFrame(docs)
if not df_docs.empty:
    df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$','', regex=True)

# Heuristic venue extraction: look for CHI token near start
# We'll mark as CHI if text contains patterns like "CHI '" or "PROCEEDINGS OF THE SIGCHI" or "SIGCHI" or "CHI 20" etc.
chi_patterns = [
    r"\bCHI\b\s*['’]\s*\d{2}",
    r"\bCHI\s*20\d{2}\b",
    r"\bSIGCHI\b",
    r"\bConference on Human Factors in Computing Systems\b",
    r"\bProceedings of the SIGCHI\b",
]
pat = re.compile("|".join(chi_patterns), flags=re.IGNORECASE)

def is_chi(txt):
    if not isinstance(txt, str):
        return False
    # search first 5000 chars for venue header signal
    head = txt[:5000]
    return bool(pat.search(head))

if not df_docs.empty:
    df_docs['is_chi'] = df_docs['text'].apply(is_chi)

# Join with citations
if df_cit.empty or df_docs.empty:
    out = {"total_citations_2020_for_CHI_papers": 0, "num_CHI_papers_cited_in_2020": 0}
else:
    df_chi = df_docs.loc[df_docs['is_chi'], ['title']].drop_duplicates()
    df_join = df_cit.merge(df_chi, on='title', how='inner')
    out = {
        "total_citations_2020_for_CHI_papers": int(df_join['citation_count'].sum()),
        "num_CHI_papers_cited_in_2020": int(df_join['title'].nunique())
    }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_qFkSnbDyNpOvsonbQrfkzSQb': 'file_storage/call_qFkSnbDyNpOvsonbQrfkzSQb.json', 'var_call_g7wg3q1JUJXRLPOjzZpvzpmg': 'file_storage/call_g7wg3q1JUJXRLPOjzZpvzpmg.json'}

exec(code, env_args)
