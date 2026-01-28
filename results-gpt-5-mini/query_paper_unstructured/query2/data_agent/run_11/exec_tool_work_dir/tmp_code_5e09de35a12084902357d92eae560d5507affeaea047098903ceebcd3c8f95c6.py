code = """import json
import pandas as pd
import re

with open(var_call_i1EHOe6eQyxSNYCffd5AcO4b, 'r') as f:
    citations = json.load(f)
with open(var_call_24pZGp7rvDVZOFvYZcBb54o0, 'r') as f:
    papers = json.load(f)

# DataFrames
df_c = pd.DataFrame(citations)
df_p = pd.DataFrame(papers)

# derive titles
if 'filename' in df_p.columns:
    df_p['title'] = df_p['filename'].str.replace(r'\.txt$', '', regex=True)
else:
    df_p['title'] = None

# normalize title function
def normalize_title(s):
    if s is None:
        return ''
    s = str(s).lower()
    s = re.sub(r"[^a-z0-9\s]", ' ', s)
    s = re.sub(r"\s+", ' ', s).strip()
    return s

# normalized titles
df_c['norm_title'] = df_c['title'].apply(normalize_title)
df_p['norm_title'] = df_p['title'].apply(normalize_title)

# Detect ACM using multiple heuristics
texts = df_p['text'].fillna('').astype(str).str.lower()
contains_acm_word = texts.str.contains(r'\bacm\b', regex=True, na=False)
contains_association = texts.str.contains('association for computing machinery', na=False)
contains_1145 = texts.str.contains('10.1145', na=False)
contains_acm_copyright = texts.str.contains('copyright.*acm', regex=True, na=False)

# Combine
df_p['is_acm_any'] = contains_acm_word | contains_association | contains_1145 | contains_acm_copyright

# Merge on normalized title
merged = pd.merge(df_c, df_p[['norm_title', 'is_acm_any', 'title']], on='norm_title', how='left', suffixes=('_c', '_p'))

# convert citation_count
def to_int(x):
    try:
        return int(x)
    except Exception:
        try:
            return int(float(x))
        except Exception:
            return None

merged['citation_count'] = merged['citation_count'].apply(to_int)

# Filter to ACM-detected
acm_rows = merged[merged['is_acm_any'] == True]
counts = acm_rows['citation_count'].dropna().astype(int)

# show sample mismatches
sample = acm_rows[['title_c','title_p','citation_count']].head(20).to_dict(orient='records')

num_acm_true_in_papers = int(df_p['is_acm_any'].sum())

if len(counts) > 0:
    avg = float(counts.mean())
    result = {'average_citation_count': avg, 'num_papers': int(len(counts)), 'num_acm_true_in_papers': num_acm_true_in_papers, 'sample_rows': sample}
else:
    result = {'average_citation_count': None, 'num_papers': 0, 'num_acm_true_in_papers': num_acm_true_in_papers, 'sample_rows': sample}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_i1EHOe6eQyxSNYCffd5AcO4b': 'file_storage/call_i1EHOe6eQyxSNYCffd5AcO4b.json', 'var_call_CEZRU4yQ1YSY05ldRxYXaLc1': ['paper_docs'], 'var_call_24pZGp7rvDVZOFvYZcBb54o0': 'file_storage/call_24pZGp7rvDVZOFvYZcBb54o0.json', 'var_call_KMmhw9jgOxEFRWjFJ5OTGlcI': {'average_citation_count': None, 'num_papers': 0}, 'var_call_g5NOyVL8wOsrx3UOs05wpjEn': {'average_citation_count': None, 'num_papers': 0, 'num_rows_with_is_acm_notnull': 55, 'num_acm_true_rows': 0}, 'var_call_kATS3XKk72i9xayEy5e1k8J5': {'average_citation_count': 60.092592592592595, 'num_papers': 54, 'num_acm_rows_in_merged': 54, 'num_acm_true_in_papers': 97, 'num_citation_records_total': 158}}

exec(code, env_args)
