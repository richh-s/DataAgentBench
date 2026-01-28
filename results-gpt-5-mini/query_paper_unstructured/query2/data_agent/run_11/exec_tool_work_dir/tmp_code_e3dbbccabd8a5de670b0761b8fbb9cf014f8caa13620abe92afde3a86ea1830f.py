code = """import json
import pandas as pd
import re

# Load the large query results from the provided storage file paths
with open(var_call_i1EHOe6eQyxSNYCffd5AcO4b, 'r') as f:
    citations = json.load(f)
with open(var_call_24pZGp7rvDVZOFvYZcBb54o0, 'r') as f:
    papers = json.load(f)

# Create DataFrames
df_c = pd.DataFrame(citations)
df_p = pd.DataFrame(papers)

# Normalize title from filename by removing trailing .txt
if 'filename' in df_p.columns:
    df_p['title'] = df_p['filename'].str.replace(r'\.txt$', '', regex=True)
else:
    df_p['title'] = None

# Detect ACM as a whole word in the text (case-insensitive)
if 'text' in df_p.columns:
    df_p['is_acm'] = df_p['text'].str.lower().str.contains(r'\bacm\b', regex=True, na=False)
else:
    df_p['is_acm'] = False

# Merge citation records with paper metadata on title
merged = pd.merge(df_c, df_p[['title', 'is_acm']], on='title', how='left')

# Convert citation_count to integers where possible
def to_int(x):
    try:
        return int(x)
    except Exception:
        try:
            return int(float(x))
        except Exception:
            return None

merged['citation_count'] = merged['citation_count'].apply(to_int)

# Filter to ACM papers
acm_rows = merged[merged['is_acm'] == True]
counts = acm_rows['citation_count'].dropna().astype(int)

if len(counts) > 0:
    avg = counts.mean()
    result = {'average_citation_count': float(avg), 'num_papers': int(len(counts))}
else:
    result = {'average_citation_count': None, 'num_papers': 0}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_i1EHOe6eQyxSNYCffd5AcO4b': 'file_storage/call_i1EHOe6eQyxSNYCffd5AcO4b.json', 'var_call_CEZRU4yQ1YSY05ldRxYXaLc1': ['paper_docs'], 'var_call_24pZGp7rvDVZOFvYZcBb54o0': 'file_storage/call_24pZGp7rvDVZOFvYZcBb54o0.json'}

exec(code, env_args)
