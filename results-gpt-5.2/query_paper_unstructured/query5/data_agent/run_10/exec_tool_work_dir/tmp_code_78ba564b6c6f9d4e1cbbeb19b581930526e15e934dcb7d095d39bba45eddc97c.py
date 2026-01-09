code = """import json, re, pandas as pd

# Load citations 2020
path_cit = var_call_Bjr7m9IU4V9l6j6BJRjRK7Ks
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
# normalize types
if 'citation_count' in df_cit.columns:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)

# Load paper docs
path_docs = var_call_5RndJ67YDHIniSOyFlgBmXKk
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

df_docs = pd.DataFrame(docs)
df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)

# Heuristic venue extraction: check for CHI tokens in text/filename
# Many papers include e.g., "CHI '15" or "Proceedings of the SIGCHI".
chi_pat = re.compile(r"\bCHI\b\s*['’]?\s*\d{2}|\bSIGCHI\b|\bConference on Human Factors in Computing Systems\b|\bProceedings of the SIGCHI\b", re.IGNORECASE)

def is_chi(row):
    t = row.get('text') or ''
    fn = row.get('filename') or ''
    return bool(chi_pat.search(t)) or bool(re.search(r"\bCHI\b", fn, flags=re.IGNORECASE))

df_docs['is_chi'] = df_docs.apply(is_chi, axis=1)
chi_titles = set(df_docs.loc[df_docs['is_chi'], 'title'].tolist())

# Join with citations
chi_cit = df_cit[df_cit['title'].isin(chi_titles)].copy()

# Aggregate total citation counts across all CHI papers cited in 2020
# (sum of per-paper citation_count for year=2020)
total = int(chi_cit['citation_count'].sum())

# Also provide per-paper list
per_paper = chi_cit.sort_values(['citation_count','title'], ascending=[False, True])
per_paper_records = per_paper.to_dict(orient='records')

out = {
    'citation_year': 2020,
    'venue': 'CHI',
    'total_citation_count': total,
    'paper_counts': len(per_paper_records),
    'per_paper': per_paper_records
}

print("__RESULT__:")
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_Bjr7m9IU4V9l6j6BJRjRK7Ks': 'file_storage/call_Bjr7m9IU4V9l6j6BJRjRK7Ks.json', 'var_call_5RndJ67YDHIniSOyFlgBmXKk': 'file_storage/call_5RndJ67YDHIniSOyFlgBmXKk.json'}

exec(code, env_args)
