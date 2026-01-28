code = """import json
import pandas as pd

# Load the large results from the stored JSON files
with open(var_call_AISwXQtvRwgIlyXKTtdQik51, 'r') as f:
    citations = json.load(f)
with open(var_call_IOfbhwM0HnTPxuBnMvIBnir5, 'r') as f:
    papers = json.load(f)

# Create DataFrames
df_cit = pd.DataFrame(citations)
# Ensure citation_count is numeric
if 'citation_count' in df_cit.columns:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)
else:
    df_cit['citation_count'] = 0

# Prepare papers dataframe and extract title from filename
df_p = pd.DataFrame(papers)
if 'filename' in df_p.columns:
    df_p['title'] = df_p['filename'].str.replace(r'\.txt$', '', regex=True)
else:
    df_p['title'] = None

# Filter papers published by ACM by searching for 'acm' in text (case-insensitive)
if 'text' in df_p.columns:
    df_p_acm = df_p[df_p['text'].str.lower().str.contains('acm', na=False)].copy()
else:
    df_p_acm = df_p.iloc[0:0].copy()

# Join citations (for 2018) with ACM papers on title
merged = pd.merge(df_cit, df_p_acm[['title']], on='title', how='inner')

# Compute average citation count
if len(merged) > 0:
    avg = merged['citation_count'].mean()
    avg_rounded = round(float(avg), 2)
else:
    avg_rounded = None

result = {
    'average_citation_count': avg_rounded,
    'num_papers_considered': int(len(merged))
}

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_AISwXQtvRwgIlyXKTtdQik51': 'file_storage/call_AISwXQtvRwgIlyXKTtdQik51.json', 'var_call_IOfbhwM0HnTPxuBnMvIBnir5': 'file_storage/call_IOfbhwM0HnTPxuBnMvIBnir5.json'}

exec(code, env_args)
