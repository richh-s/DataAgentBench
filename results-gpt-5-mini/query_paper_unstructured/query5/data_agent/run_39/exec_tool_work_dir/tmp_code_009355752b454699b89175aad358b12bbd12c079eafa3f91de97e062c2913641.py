code = """import json
import re
import pandas as pd

# Load data from storage-provided file paths
with open(var_call_GgCAdHc61Z9jVwrfftFCGfWA, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_wGraeOsJe1dV4ji6SLjE7yR7, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Convert to DataFrame
df_cit = pd.DataFrame(citations)
# Ensure citation_count is int
df_cit['citation_count'] = df_cit['citation_count'].astype(int)

# Process papers: extract title from filename
df_papers = pd.DataFrame(papers)
# Some entries may not have filename; guard
df_papers = df_papers[df_papers['filename'].notna()].copy()

def filename_to_title(fn):
    return fn[:-4] if fn.lower().endswith('.txt') else fn

df_papers['title'] = df_papers['filename'].apply(filename_to_title)

# Detect CHI venue by searching for 'CHI' in the first 1000 chars of text
def is_chi(text):
    if not isinstance(text, str):
        return False
    header = text[:1000]
    return bool(re.search(r"\bCHI\b", header, flags=re.IGNORECASE))

df_papers['is_chi'] = df_papers['text'].apply(is_chi)

# Filter CHI papers
df_chi = df_papers[df_papers['is_chi']].copy()

# Merge with citations for 2020 on title
# df_cit contains only citation_year=2020 from previous query
merged = pd.merge(df_chi[['title']], df_cit, on='title', how='inner')

# Prepare output list sorted by citation_count desc
merged['citation_count'] = merged['citation_count'].astype(int)
merged_sorted = merged.sort_values(by='citation_count', ascending=False)

result = merged_sorted[['title', 'citation_count']].to_dict(orient='records')

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GgCAdHc61Z9jVwrfftFCGfWA': 'file_storage/call_GgCAdHc61Z9jVwrfftFCGfWA.json', 'var_call_gPsa1A49l0SrTdCgjauY5Nai': ['paper_docs'], 'var_call_wGraeOsJe1dV4ji6SLjE7yR7': 'file_storage/call_wGraeOsJe1dV4ji6SLjE7yR7.json'}

exec(code, env_args)
