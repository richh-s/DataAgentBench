code = """import json
import re
import pandas as pd

with open(var_call_GgCAdHc61Z9jVwrfftFCGfWA, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_wGraeOsJe1dV4ji6SLjE7yR7, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# DataFrames
df_cit = pd.DataFrame(citations)
df_cit['citation_count'] = df_cit['citation_count'].astype(int)

df_papers = pd.DataFrame(papers)
# drop entries without filename
df_papers = df_papers[df_papers['filename'].notna()].copy()

def filename_to_title(fn):
    return fn[:-4] if fn.lower().endswith('.txt') else fn

df_papers['title'] = df_papers['filename'].apply(filename_to_title)

# Define chi detection patterns
patterns = [r"\bCHI\b", r"SIGCHI", r"Proceedings of the SIGCHI", r"CHI\s?'", r"CHI:\s" , r"ACM CHI"]

def is_chi(text):
    if not isinstance(text, str):
        return False
    for p in patterns:
        if re.search(p, text, flags=re.IGNORECASE):
            return True
    return False

# Apply detection
# To speed up, search first 2000 chars then whole text if needed
def is_chi_fast(text):
    if not isinstance(text, str):
        return False
    snippet = text[:2000]
    for p in patterns:
        if re.search(p, snippet, flags=re.IGNORECASE):
            return True
    # fallback to full text
    for p in patterns:
        if re.search(p, text, flags=re.IGNORECASE):
            return True
    return False

# Apply
df_papers['is_chi'] = df_papers['text'].apply(is_chi_fast)

# Filter CHI
df_chi = df_papers[df_papers['is_chi']].copy()

# Merge with citations
merged = pd.merge(df_chi[['title']], df_cit, on='title', how='inner')

# Aggregate total citations for 2020
if not merged.empty:
    merged['citation_count'] = merged['citation_count'].astype(int)
    total = int(merged['citation_count'].sum())
    merged_sorted = merged.sort_values(by='citation_count', ascending=False)
    papers_list = merged_sorted[['title', 'citation_count']].to_dict(orient='records')
else:
    total = 0
    papers_list = []

output = {"total_citations_2020": total, "papers": papers_list}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_GgCAdHc61Z9jVwrfftFCGfWA': 'file_storage/call_GgCAdHc61Z9jVwrfftFCGfWA.json', 'var_call_gPsa1A49l0SrTdCgjauY5Nai': ['paper_docs'], 'var_call_wGraeOsJe1dV4ji6SLjE7yR7': 'file_storage/call_wGraeOsJe1dV4ji6SLjE7yR7.json', 'var_call_WinrA26Dl0ESU1Rbde5rb8lp': []}

exec(code, env_args)
