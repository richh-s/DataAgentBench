code = """import json
import pandas as pd

# Load data from storage-provided file paths
with open(var_call_zzK7bHkUDPkIkcg5doQqoM3J, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_9CZg5hl05BZC3LJ77dMjEb4k, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Create DataFrames
df_cit = pd.DataFrame(citations)
df_pap = pd.DataFrame(papers)

# Normalize and convert types
if 'citation_count' in df_cit.columns:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)
else:
    df_cit['citation_count'] = 0

# Extract title from filename in papers
if 'filename' in df_pap.columns:
    df_pap['title'] = df_pap['filename'].str.replace(r"\.txt$", '', regex=True)
else:
    df_pap['title'] = None

# Detect ACM in the text (case-insensitive)
if 'text' in df_pap.columns:
    df_pap['is_acm'] = df_pap['text'].str.contains(r'\bACM\b', case=False, na=False)
else:
    df_pap['is_acm'] = False

# Merge citations with paper metadata on title
df_merged = pd.merge(df_cit, df_pap[['title', 'is_acm']], on='title', how='left')

# Filter for ACM papers
df_acm = df_merged[df_merged['is_acm'] == True]

# Compute average citation count
if len(df_acm) > 0:
    avg = df_acm['citation_count'].mean()
    avg_val = float(avg)
    num_papers = int(len(df_acm))
else:
    avg_val = None
    num_papers = 0

# Prepare result
result = {
    'average_citation_count': avg_val,
    'num_papers_considered': num_papers
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_DeTvufNC96JvlW2cJS5cVew7': ['paper_docs'], 'var_call_NLpSfxNXV8s4NEdNNZxjZu5X': ['Citations', 'sqlite_sequence'], 'var_call_zzK7bHkUDPkIkcg5doQqoM3J': 'file_storage/call_zzK7bHkUDPkIkcg5doQqoM3J.json', 'var_call_9CZg5hl05BZC3LJ77dMjEb4k': 'file_storage/call_9CZg5hl05BZC3LJ77dMjEb4k.json'}

exec(code, env_args)
