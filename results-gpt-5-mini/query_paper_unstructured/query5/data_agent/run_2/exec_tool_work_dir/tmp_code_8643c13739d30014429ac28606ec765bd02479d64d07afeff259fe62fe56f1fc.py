code = """import json
import pandas as pd
import re

# Load previous tool results from storage file paths
with open(var_call_vNOnY2SD5s4ow2jUdA6JW4Qj, 'r') as f:
    citations = json.load(f)
with open(var_call_ZnOphUJL9NVPkha3ZMz2vXiG, 'r') as f:
    papers = json.load(f)

# DataFrames
df_cit = pd.DataFrame(citations)
df_p = pd.DataFrame(papers)

# Clean citations: ensure citation_count numeric
if 'citation_count' in df_cit.columns:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)
else:
    df_cit['citation_count'] = 0

# Extract title from filename
if 'filename' in df_p.columns:
    df_p['title'] = df_p['filename'].str.replace(r"\.txt$", '', regex=True)
else:
    df_p['title'] = ''

# Determine CHI papers by searching for 'CHI' as a whole word (case-insensitive) in text
df_p['is_chi'] = df_p['text'].fillna('').apply(lambda t: bool(re.search(r"\bCHI\b", t.upper())))

# Set of titles for CHI papers
chi_titles = set(df_p.loc[df_p['is_chi'], 'title'].tolist())

# Filter citations to those titles
df_cit_chi = df_cit[df_cit['title'].isin(chi_titles)].copy()

# Compute total citation count
total_citations = int(df_cit_chi['citation_count'].sum())
matched_papers = int(df_cit_chi['title'].nunique())

# Prepare result
result = {
    'total_citations_2020_for_CHI_papers': total_citations,
    'matched_papers_count': matched_papers
}

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_vNOnY2SD5s4ow2jUdA6JW4Qj': 'file_storage/call_vNOnY2SD5s4ow2jUdA6JW4Qj.json', 'var_call_ZnOphUJL9NVPkha3ZMz2vXiG': 'file_storage/call_ZnOphUJL9NVPkha3ZMz2vXiG.json'}

exec(code, env_args)
