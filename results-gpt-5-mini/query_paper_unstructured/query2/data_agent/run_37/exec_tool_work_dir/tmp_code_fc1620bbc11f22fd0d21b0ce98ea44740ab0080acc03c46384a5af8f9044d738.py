code = """import json
import pandas as pd
import re

def load_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

citations = load_var(var_call_gaeD5JcrDNpMG8RSzZp1Knio)
papers = load_var(var_call_lBRfFKCi9fUVFHVjqJVNUkxg)

df_c = pd.DataFrame(citations)
if 'citation_count' in df_c.columns:
    df_c['citation_count'] = pd.to_numeric(df_c['citation_count'], errors='coerce')

rows = []
for doc in papers:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','') or ''
    is_acm = 'acm' in text.lower()
    rows.append({'title': title, 'is_acm': is_acm, 'text_snippet': text[:500]})

df_p = pd.DataFrame(rows)
merged = pd.merge(df_c, df_p, on='title', how='left')

total_citations = len(df_c)
matched_papers = merged['is_acm'].notna().sum()
acm_true = int(merged['is_acm'].fillna(False).sum())
acm_false = int(((merged['is_acm'] == False)).sum())
na_count = int(merged['is_acm'].isna().sum())

# average for acm_true where is_acm True
merged_acm = merged[merged['is_acm'] == True]
valid_counts = merged_acm['citation_count'].dropna().astype(float)
count_papers = int(len(valid_counts))
avg = float(valid_counts.mean()) if count_papers>0 else None

sample_acm_titles = merged_acm['title'].drop_duplicates().head(10).tolist()
sample_unmatched = merged[merged['is_acm'].isna()]['title'].drop_duplicates().head(10).tolist()

result = {
    'total_citations_rows': total_citations,
    'matched_papers_rows': int(matched_papers),
    'acm_true_count_rows': acm_true,
    'acm_false_count_rows': acm_false,
    'na_count_rows': na_count,
    'average_citation_count_computed': avg,
    'acm_papers_count_used_in_average': count_papers,
    'sample_acm_titles': sample_acm_titles,
    'sample_unmatched_titles': sample_unmatched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_gaeD5JcrDNpMG8RSzZp1Knio': 'file_storage/call_gaeD5JcrDNpMG8RSzZp1Knio.json', 'var_call_F0PJctYJsnSnHEJXGxITufu2': ['paper_docs'], 'var_call_lBRfFKCi9fUVFHVjqJVNUkxg': 'file_storage/call_lBRfFKCi9fUVFHVjqJVNUkxg.json', 'var_call_ygoiSFUVelnR8TPdaNNo9Pzp': {'average_citation_count': None, 'acm_papers_count': 0}}

exec(code, env_args)
