code = """import json, re
import pandas as pd

# Load citations 2020
cit_path = var_call_S9eV44n31jNAPxIgpaspiHF6
with open(cit_path, 'r', encoding='utf-8') as f:
    cit_records = json.load(f)

df_cit = pd.DataFrame(cit_records)
# normalize types
if 'citation_count' in df_cit.columns:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)

df_cit['title_norm'] = df_cit['title'].astype(str).str.strip().str.lower()

# Load paper docs
docs_path = var_call_ftuRxiadPw8NoTU53pyMvgnL
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

df_docs = pd.DataFrame(docs)
df_docs['title'] = df_docs['filename'].astype(str).str.replace(r'\.txt$', '', regex=True)
df_docs['title_norm'] = df_docs['title'].str.strip().str.lower()

# Detect CHI venue from text (robust-ish)
pat = re.compile(r"\bCHI\s*'?\d{2}\b|\bSIGCHI\b|\bCHI\b\s*(Conference|Proceedings)", re.IGNORECASE)

def is_chi(t):
    if not isinstance(t, str):
        return False
    return bool(pat.search(t))

df_docs['is_chi'] = df_docs['text'].map(is_chi)

# Join citations with CHI papers
chi_titles = set(df_docs.loc[df_docs['is_chi'], 'title_norm'])
df_chi_cit = df_cit[df_cit['title_norm'].isin(chi_titles)].copy()

# Total citations across all CHI papers cited in 2020
total = int(df_chi_cit['citation_count'].sum())

# Also compute per-paper citation counts (in 2020) for those CHI papers
per_paper = (df_chi_cit.groupby('title', as_index=False)['citation_count'].sum()
             .sort_values(['citation_count','title'], ascending=[False, True]))

result = {
    'total_citations_2020_for_CHI_papers': total,
    'num_CHI_papers_with_citations_in_2020': int(per_paper.shape[0]),
    'per_paper_citations_2020': per_paper.to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_S9eV44n31jNAPxIgpaspiHF6': 'file_storage/call_S9eV44n31jNAPxIgpaspiHF6.json', 'var_call_ftuRxiadPw8NoTU53pyMvgnL': 'file_storage/call_ftuRxiadPw8NoTU53pyMvgnL.json'}

exec(code, env_args)
