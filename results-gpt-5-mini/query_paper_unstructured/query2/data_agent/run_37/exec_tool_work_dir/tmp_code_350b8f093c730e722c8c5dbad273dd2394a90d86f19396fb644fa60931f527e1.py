code = """import json
import pandas as pd
import re

# Load data from storage variables (could be file paths or lists)
def load_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

citations = load_var(var_call_gaeD5JcrDNpMG8RSzZp1Knio)
papers = load_var(var_call_lBRfFKCi9fUVFHVjqJVNUkxg)

# Create DataFrames
df_c = pd.DataFrame(citations)
# Ensure citation_count is numeric
if 'citation_count' in df_c.columns:
    df_c['citation_count'] = pd.to_numeric(df_c['citation_count'], errors='coerce')

# Prepare papers dataframe: extract title from filename and detect ACM in text
rows = []
for doc in papers:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','') or ''
    is_acm = bool(re.search(r'\bacm\b', text, flags=re.IGNORECASE))
    rows.append({'title': title, 'is_acm': is_acm})

df_p = pd.DataFrame(rows)

# Merge citations (which are for 2018) with papers on title
# Note: Titles in citations table match filename without .txt per hints
merged = pd.merge(df_c, df_p, on='title', how='left')
# Filter to ACM papers
merged_acm = merged[merged['is_acm'] == True]

# Compute average citation_count, ignoring NaNs
valid_counts = merged_acm['citation_count'].dropna().astype(float)
count_papers = int(len(valid_counts))
if count_papers > 0:
    average = float(valid_counts.mean())
else:
    average = None

result = {'average_citation_count': average, 'acm_papers_count': count_papers}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_gaeD5JcrDNpMG8RSzZp1Knio': 'file_storage/call_gaeD5JcrDNpMG8RSzZp1Knio.json', 'var_call_F0PJctYJsnSnHEJXGxITufu2': ['paper_docs'], 'var_call_lBRfFKCi9fUVFHVjqJVNUkxg': 'file_storage/call_lBRfFKCi9fUVFHVjqJVNUkxg.json'}

exec(code, env_args)
