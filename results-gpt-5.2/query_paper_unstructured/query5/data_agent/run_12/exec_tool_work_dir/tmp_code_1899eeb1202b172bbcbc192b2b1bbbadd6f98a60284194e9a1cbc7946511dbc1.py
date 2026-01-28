code = """import json, re
import pandas as pd

# Load citations 2020
cit_path = var_call_xqQc0vHIxIpD839NF5EFGOlc
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
# coerce types
if not df_cit.empty:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)

# Load paper docs
docs_path = var_call_IFALuOM496GWXYPTg9qESAJm
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

df_docs = pd.DataFrame(docs)
if df_docs.empty:
    chi_titles = set()
else:
    df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)
    # Venue detection: look for 'CHI' in header-like patterns, but avoid false positives by matching CHI with year or apostrophe
    def is_chi(text):
        if not isinstance(text, str):
            return False
        t = text.upper()
        # common patterns: "CHI '20", "CHI 2020", "PROCEEDINGS OF THE SIGCHI"
        return (re.search(r"\bCHI\b\s*['’]?\s*\d{2}\b", t) is not None) or (re.search(r"\bCHI\b\s*20\d{2}\b", t) is not None) or ('SIGCHI CONFERENCE ON HUMAN FACTORS IN COMPUTING SYSTEMS' in t)
    df_docs['is_chi'] = df_docs['text'].map(is_chi)
    chi_titles = set(df_docs.loc[df_docs['is_chi'], 'title'].tolist())

# Filter citations for CHI papers
if df_cit.empty:
    total = 0
    n = 0
else:
    df_chi_cit = df_cit[df_cit['title'].isin(chi_titles)].copy()
    total = int(df_chi_cit['citation_count'].sum())
    n = int(df_chi_cit.shape[0])

out = {"citation_year": 2020, "venue": "CHI", "num_papers": n, "total_citations": total}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_xqQc0vHIxIpD839NF5EFGOlc': 'file_storage/call_xqQc0vHIxIpD839NF5EFGOlc.json', 'var_call_IFALuOM496GWXYPTg9qESAJm': 'file_storage/call_IFALuOM496GWXYPTg9qESAJm.json'}

exec(code, env_args)
