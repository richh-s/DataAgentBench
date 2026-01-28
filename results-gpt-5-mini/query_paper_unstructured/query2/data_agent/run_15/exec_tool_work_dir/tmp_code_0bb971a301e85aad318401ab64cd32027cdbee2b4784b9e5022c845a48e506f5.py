code = """import json
import pandas as pd

# Load previous tool results from storage files
with open(var_call_u3T2V5YVOxUQx6K1kkGmr6mw, 'r') as f:
    citations = json.load(f)
with open(var_call_ZQ9kT6u34ivTSrIpZD1p5rSh, 'r') as f:
    papers = json.load(f)

# Create DataFrames
df_cit = pd.DataFrame(citations)
# Ensure correct types
if 'citation_count' in df_cit.columns:
    df_cit['citation_count'] = df_cit['citation_count'].astype(int)

df_papers = pd.DataFrame(papers)
# Extract title from filename
df_papers['title'] = df_papers['filename'].str.replace('.txt', '', regex=False)
# Detect ACM in text (case-insensitive word match)
df_papers['is_acm'] = df_papers['text'].str.contains(r'(?i)\bACM\b', regex=True)

# Filter ACM papers
acm_papers = df_papers[df_papers['is_acm']]

# Merge citations (which are for citation_year 2018) with ACM papers by title
merged = pd.merge(df_cit, acm_papers[['title']], on='title', how='inner')

# Compute average citation count
if merged.shape[0] == 0:
    avg = None
else:
    avg = merged['citation_count'].mean()

result = {
    'average_citation_count': round(float(avg), 2) if avg is not None else None,
    'num_acm_papers_cited_in_2018': int(merged.shape[0])
}

print("__RESULT__:")
import json as _json
print(_json.dumps(result))"""

env_args = {'var_call_u3T2V5YVOxUQx6K1kkGmr6mw': 'file_storage/call_u3T2V5YVOxUQx6K1kkGmr6mw.json', 'var_call_ZQ9kT6u34ivTSrIpZD1p5rSh': 'file_storage/call_ZQ9kT6u34ivTSrIpZD1p5rSh.json'}

exec(code, env_args)
