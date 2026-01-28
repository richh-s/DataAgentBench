code = """import json
import pandas as pd

# Load data from storage-provided file paths
with open(var_call_l3PPpLM8azB2GyPcKmLRSWmP, 'r') as f:
    citations = json.load(f)
with open(var_call_LyPn518D1Z9V3O9rDu5LttwR, 'r') as f:
    papers = json.load(f)

# Create DataFrames
df_c = pd.DataFrame(citations)
df_p = pd.DataFrame(papers)

# Normalize and convert types
if 'citation_count' in df_c.columns:
    df_c['citation_count'] = pd.to_numeric(df_c['citation_count'], errors='coerce').fillna(0).astype(int)
else:
    df_c['citation_count'] = 0

# Extract title from filename (remove trailing .txt)
if 'filename' in df_p.columns:
    df_p['title'] = df_p['filename'].str.replace(r'\.txt$', '', regex=True)
else:
    df_p['title'] = None

# Determine if paper is published by ACM by searching for 'ACM' or 'Association for Computing Machinery' in text
if 'text' in df_p.columns:
    df_p['source_is_acm'] = df_p['text'].str.contains(r'\bACM\b', case=False, na=False) | df_p['text'].str.contains('Association for Computing Machinery', case=False, na=False)
else:
    df_p['source_is_acm'] = False

# Merge citations with paper info on title
df_merged = pd.merge(df_c, df_p[['title', 'source_is_acm']], on='title', how='left')

# Filter to ACM papers
df_acm = df_merged[df_merged['source_is_acm'] == True]

# Compute average citation count
if len(df_acm) == 0:
    avg = None
    count = 0
else:
    avg = df_acm['citation_count'].mean()
    count = int(len(df_acm))

# Prepare result
result = {
    'average_citation_count': None if avg is None else round(float(avg), 2),
    'num_acm_papers_considered': count
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_l3PPpLM8azB2GyPcKmLRSWmP': 'file_storage/call_l3PPpLM8azB2GyPcKmLRSWmP.json', 'var_call_JpdX0be34W7QvGpbBwH5EoYN': ['paper_docs'], 'var_call_LyPn518D1Z9V3O9rDu5LttwR': 'file_storage/call_LyPn518D1Z9V3O9rDu5LttwR.json'}

exec(code, env_args)
