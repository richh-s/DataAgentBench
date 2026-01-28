code = """import json
import pandas as pd
import re

# Load the large query results from the provided file paths
with open(var_call_REkXxPIABFYdzE3SXKyq4t0B, 'r', encoding='utf-8') as f:
    citations_data = json.load(f)

with open(var_call_eLeNFq4h3afexjuODnDi46VC, 'r', encoding='utf-8') as f:
    papers_data = json.load(f)

# Create DataFrames
df_cit = pd.DataFrame(citations_data)
df_pap = pd.DataFrame(papers_data)

# Normalize citations: ensure title matches the filename without .txt
# Convert citation_count to int where possible
def to_int(x):
    try:
        return int(x)
    except:
        try:
            return int(float(x))
        except:
            return None

if 'citation_count' in df_cit.columns:
    df_cit['citation_count'] = df_cit['citation_count'].apply(to_int)

# Extract title from filename in papers collection
if 'filename' in df_pap.columns:
    df_pap['title'] = df_pap['filename'].str.replace(r"\.txt$", "", regex=True)
else:
    df_pap['title'] = None

# Detect CHI venue by searching for the token 'CHI' in the text field
# Use word boundary to avoid false matches
def is_chi(text):
    if not isinstance(text, str):
        return False
    return re.search(r"\bCHI\b", text, flags=re.IGNORECASE) is not None

if 'text' in df_pap.columns:
    df_pap['is_chi'] = df_pap['text'].apply(is_chi)
else:
    df_pap['is_chi'] = False

# Filter CHI papers
df_chi = df_pap[df_pap['is_chi'] == True]

# Merge citations (which are for citation_year=2020) with CHI papers on title
# The citations table title should match df_pap title
merged = pd.merge(df_chi[['title']], df_cit, on='title', how='inner')

# Drop rows without citation_count or with null
merged = merged[merged['citation_count'].notnull()]

# Compute total citation counts and prepare per-paper list
merged['citation_count'] = merged['citation_count'].astype(int)
per_paper = merged[['title', 'citation_count']].to_dict(orient='records')

total_citations = int(merged['citation_count'].sum()) if not merged.empty else 0

result = {
    'total_citations': total_citations,
    'num_papers': len(per_paper),
    'papers': per_paper
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_REkXxPIABFYdzE3SXKyq4t0B': 'file_storage/call_REkXxPIABFYdzE3SXKyq4t0B.json', 'var_call_eLeNFq4h3afexjuODnDi46VC': 'file_storage/call_eLeNFq4h3afexjuODnDi46VC.json'}

exec(code, env_args)
