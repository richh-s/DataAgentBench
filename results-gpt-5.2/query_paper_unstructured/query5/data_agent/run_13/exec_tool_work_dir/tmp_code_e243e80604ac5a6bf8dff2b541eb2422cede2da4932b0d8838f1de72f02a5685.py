code = """import json, re
import pandas as pd

# Load citations 2020
cit = var_call_eItLPis94qne25IFeIwyNIbH
if isinstance(cit, str):
    with open(cit, 'r', encoding='utf-8') as f:
        cit = json.load(f)

df_cit = pd.DataFrame(cit)
if df_cit.empty:
    out = {"total_citations_2020_for_CHI_papers": 0, "chi_paper_count": 0}
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)

# Load paper docs filenames and text to detect venue
papers = var_call_xFj6FdG6bpaX5bvtfSWAWwT5
if isinstance(papers, str):
    with open(papers, 'r', encoding='utf-8') as f:
        papers = json.load(f)

df_p = pd.DataFrame(papers)
# title from filename
if 'filename' in df_p.columns:
    df_p['title'] = df_p['filename'].str.replace(r'\.txt$', '', regex=True)

# Heuristic venue detection: look for CHI markers in first part of text
# We'll use regex for: "CHI 'YY" or "CHI 20" or "Proceedings of the SIGCHI" or "ACM CHI".
pat = re.compile(r"\bCHI\b\s*['’]?\d{2}\b|\bCHI\s*\d{4}\b|SIGCHI\b|\bConference on Human Factors in Computing Systems\b", re.IGNORECASE)

def is_chi(text):
    if not isinstance(text, str):
        return False
    snippet = text[:4000]
    return bool(pat.search(snippet))

df_p['is_CHI'] = df_p['text'].apply(is_chi)
chi_titles = set(df_p.loc[df_p['is_CHI'], 'title'].dropna().tolist())

# Join with citations
chi_cit = df_cit[df_cit['title'].isin(chi_titles)]

total = int(chi_cit['citation_count'].sum())
count_papers = int(chi_cit['title'].nunique())

out = {
    "total_citations_2020_for_CHI_papers": total,
    "chi_paper_count": count_papers
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_eItLPis94qne25IFeIwyNIbH': 'file_storage/call_eItLPis94qne25IFeIwyNIbH.json', 'var_call_xFj6FdG6bpaX5bvtfSWAWwT5': 'file_storage/call_xFj6FdG6bpaX5bvtfSWAWwT5.json', 'var_call_txEjsYO8itQD9UJXV2krZkIw': 'file_storage/call_txEjsYO8itQD9UJXV2krZkIw.json', 'var_call_9zqmYuiKrGqIrFGkQbMW8tNU': 'file_storage/call_9zqmYuiKrGqIrFGkQbMW8tNU.json'}

exec(code, env_args)
