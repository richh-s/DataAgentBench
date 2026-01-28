code = """import json
import pandas as pd
import re

with open(var_call_l3PPpLM8azB2GyPcKmLRSWmP, 'r') as f:
    citations = json.load(f)
with open(var_call_LyPn518D1Z9V3O9rDu5LttwR, 'r') as f:
    papers = json.load(f)

df_c = pd.DataFrame(citations)
df_p = pd.DataFrame(papers)

# Normalize citation_count
df_c['citation_count'] = pd.to_numeric(df_c.get('citation_count', 0), errors='coerce').fillna(0).astype(int)

# Extract and normalize titles
if 'filename' in df_p.columns:
    df_p['title'] = df_p['filename'].str.replace(r'\.txt$', '', regex=True)
else:
    df_p['title'] = None

# Helper normalize function
def norm(t):
    if t is None:
        return ''
    t = str(t)
    t = t.strip()
    t = re.sub(r"\s+", " ", t)
    return t

# Apply normalization to title columns for safer matching
df_c['title_norm'] = df_c['title'].apply(norm)
df_p['title_norm'] = df_p['title'].apply(norm)

# Check ACM presence in papers
df_p['source_is_acm'] = False
if 'text' in df_p.columns:
    df_p['source_is_acm'] = df_p['text'].str.contains(r'\bACM\b', case=False, na=False) | df_p['text'].str.contains('Association for Computing Machinery', case=False, na=False)

# Some diagnostics
num_citations = len(df_c)
num_papers = len(df_p)
num_papers_acm = int(df_p['source_is_acm'].sum())

# Merge on normalized title
df_merged = pd.merge(df_c, df_p[['title_norm','source_is_acm','title']], on='title_norm', how='left', indicator=True)
merged_total = len(df_merged)
matched = df_merged[df_merged['_merge']=='both']
matched_count = len(matched)
matched_acm = matched[matched['source_is_acm']==True]
matched_acm_count = len(matched_acm)

avg = None
if matched_acm_count>0:
    avg = round(float(matched_acm['citation_count'].mean()),2)

sample_matched_acm = matched_acm[['title','citation_count']].head(20).to_dict(orient='records')

result = {
    'num_citations_records': num_citations,
    'num_paper_docs': num_papers,
    'num_paper_docs_acm': num_papers_acm,
    'merged_records_total': merged_total,
    'matched_on_title_count': matched_count,
    'matched_acm_count': matched_acm_count,
    'average_citation_count_for_matched_acm': avg,
    'sample_matched_acm': sample_matched_acm
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_l3PPpLM8azB2GyPcKmLRSWmP': 'file_storage/call_l3PPpLM8azB2GyPcKmLRSWmP.json', 'var_call_JpdX0be34W7QvGpbBwH5EoYN': ['paper_docs'], 'var_call_LyPn518D1Z9V3O9rDu5LttwR': 'file_storage/call_LyPn518D1Z9V3O9rDu5LttwR.json', 'var_call_ot8o1VcWilpQ4hD8fqPulUQC': {'average_citation_count': None, 'num_acm_papers_considered': 0}}

exec(code, env_args)
