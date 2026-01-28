code = """import json
import pandas as pd
import re

with open(var_call_i1EHOe6eQyxSNYCffd5AcO4b, 'r') as f:
    citations = json.load(f)
with open(var_call_24pZGp7rvDVZOFvYZcBb54o0, 'r') as f:
    papers = json.load(f)

df_c = pd.DataFrame(citations)
df_p = pd.DataFrame(papers)

# derive titles from filenames
if 'filename' in df_p.columns:
    df_p['title'] = df_p['filename'].str.replace(r'\.txt$', '', regex=True)
else:
    df_p['title'] = None

# helper normalize function
def normalize_title(s):
    if s is None:
        return ''
    s = str(s).lower()
    # remove punctuation
    s = re.sub(r"[^a-z0-9\s]", ' ', s)
    # collapse whitespace
    s = re.sub(r"\s+", ' ', s).strip()
    return s

# create normalized titles
df_c['norm_title'] = df_c['title'].apply(normalize_title)
df_p['norm_title'] = df_p['title'].apply(normalize_title)

# Detect ACM in text
if 'text' in df_p.columns:
    df_p['is_acm'] = df_p['text'].str.lower().str.contains(r'\bacm\b', regex=True, na=False)
else:
    df_p['is_acm'] = False

# Merge on normalized title
merged = pd.merge(df_c, df_p[['norm_title', 'is_acm']], left_on='norm_title', right_on='norm_title', how='left')

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

# Filter acm
acm_rows = merged[merged['is_acm'] == True]
counts = acm_rows['citation_count'].dropna().astype(int)

# For debugging, also compute number of matched titles
num_matched = merged['is_acm'].notna().sum()
num_acm_true = int(acm_rows.shape[0])

if len(counts) > 0:
    avg = counts.mean()
    result = {'average_citation_count': float(avg), 'num_papers': int(len(counts)), 'num_rows_with_is_acm_notnull': int(num_matched), 'num_acm_true_rows': num_acm_true}
else:
    result = {'average_citation_count': None, 'num_papers': 0, 'num_rows_with_is_acm_notnull': int(num_matched), 'num_acm_true_rows': num_acm_true}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_i1EHOe6eQyxSNYCffd5AcO4b': 'file_storage/call_i1EHOe6eQyxSNYCffd5AcO4b.json', 'var_call_CEZRU4yQ1YSY05ldRxYXaLc1': ['paper_docs'], 'var_call_24pZGp7rvDVZOFvYZcBb54o0': 'file_storage/call_24pZGp7rvDVZOFvYZcBb54o0.json', 'var_call_KMmhw9jgOxEFRWjFJ5OTGlcI': {'average_citation_count': None, 'num_papers': 0}}

exec(code, env_args)
