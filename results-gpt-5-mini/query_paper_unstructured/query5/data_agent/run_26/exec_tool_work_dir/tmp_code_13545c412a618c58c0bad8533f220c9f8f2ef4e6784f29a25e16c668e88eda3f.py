code = """import json
import pandas as pd

# Load query results from storage files
with open(var_call_pPDTnlGp6ErQmAFXxr58GiX9, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_Z5jebswmSD6KDdpfws5ksVZ8, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Prepare DataFrames
df_cit = pd.DataFrame(citations)
# Ensure numeric
df_cit['citations_2020'] = df_cit['citations_2020'].astype(int)

# Extract title from filename in papers
df_p = pd.DataFrame(papers)
# Some entries may not have filename; filter
if 'filename' in df_p.columns:
    df_p['title'] = df_p['filename'].str.replace(r"\.txt$", '', regex=True)
else:
    df_p['title'] = None

# Detect CHI venue by searching for 'CHI' or 'SIGCHI' in first 400 chars of text (case-insensitive)
import re

def is_chi(text):
    if not isinstance(text, str):
        return False
    head = text[:1000].upper()
    # common patterns
    patterns = ['CHI', "SIGCHI", 'PROCEEDINGS OF THE SIGCHI']
    for p in patterns:
        if p in head:
            return True
    # also look for "CHI'" patterns like CHI '15
    if re.search(r"CHI\s*'\d{2}", head):
        return True
    return False

_df = df_p.copy()
_df['is_chi'] = _df['text'].apply(is_chi)

# Merge with citations (only papers that have citations in 2020 are in df_cit)
merged = pd.merge(df_cit, _df[['title','is_chi']], on='title', how='left')
# Keep only CHI papers
chi_merged = merged[merged['is_chi'] == True].copy()
# Compute totals
total_citations = int(chi_merged['citations_2020'].sum())
num_papers = int(chi_merged.shape[0])

# Prepare output list of papers
papers_list = chi_merged[['title','citations_2020']].to_dict(orient='records')

output = {
    'total_citations_2020': total_citations,
    'num_papers_cited_in_2020': num_papers,
    'papers': papers_list
}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_pPDTnlGp6ErQmAFXxr58GiX9': 'file_storage/call_pPDTnlGp6ErQmAFXxr58GiX9.json', 'var_call_BJUQ9l6I9WyLcYhKHWhEQAHV': ['paper_docs'], 'var_call_Z5jebswmSD6KDdpfws5ksVZ8': 'file_storage/call_Z5jebswmSD6KDdpfws5ksVZ8.json'}

exec(code, env_args)
