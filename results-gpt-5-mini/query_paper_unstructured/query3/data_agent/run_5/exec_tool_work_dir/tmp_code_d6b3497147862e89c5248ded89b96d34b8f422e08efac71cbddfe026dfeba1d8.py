code = """import json, re
import pandas as pd

# Load previous tool results from storage file paths
with open(var_call_IsFdhu3QJLfLJT28pCFaUXL1, 'r') as f:
    papers = json.load(f)
with open(var_call_riE3qFMvZWa3oiqprJ24fNy, 'r') as f:
    citations = json.load(f)

# Create DataFrames
df_papers = pd.DataFrame(papers)

def title_from_filename(fn):
    if not isinstance(fn, str):
        return None
    return re.sub(r"\.txt$", "", fn)

df_papers['title'] = df_papers['filename'].apply(title_from_filename)

# Extract publication year (look for years 2017-2029)
def extract_year(text):
    if not isinstance(text, str):
        return None
    m = re.search(r"\b(20(?:1[7-9]|2[0-9]))\b", text)
    return int(m.group(1)) if m else None

df_papers['year'] = df_papers['text'].apply(extract_year)
# Confirm empirical contribution
df_papers['has_empirical'] = df_papers['text'].str.contains(r'\bempirical\b', case=False, na=False)

# Filter: empirical contribution and published after 2016
df_filtered = df_papers[df_papers['has_empirical'] & df_papers['year'].notnull() & (df_papers['year'] > 2016)].copy()

# Citations DataFrame
df_cit = pd.DataFrame(citations)
# normalize column name and types
if 'total_citations' in df_cit.columns:
    df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)
else:
    # fallback if aggregation wasn't precomputed
    if 'citation_count' in df_cit.columns:
        df_cit = df_cit.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})
    else:
        df_cit['total_citations'] = 0

# Merge on title
df_merged = pd.merge(df_filtered[['title','year']], df_cit[['title','total_citations']], on='title', how='left')
# fill missing citation counts with 0
df_merged['total_citations'] = df_merged['total_citations'].fillna(0).astype(int)

# Prepare output
result_list = []
for _, row in df_merged.sort_values('total_citations', ascending=False).iterrows():
    result_list.append({'title': row['title'], 'total_citation_count': int(row['total_citations'])})

import json
print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_call_W12OMTCleckOZ5MbTKK7Bqgu': ['paper_docs'], 'var_call_24V8Vqwp35Q2wTcW4VUhfbWy': ['Citations', 'sqlite_sequence'], 'var_call_IsFdhu3QJLfLJT28pCFaUXL1': 'file_storage/call_IsFdhu3QJLfLJT28pCFaUXL1.json', 'var_call_riE3qFMvZWa3oiqprJ24fNyS': 'file_storage/call_riE3qFMvZWa3oiqprJ24fNyS.json'}

exec(code, env_args)
