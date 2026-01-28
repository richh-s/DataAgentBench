code = """import json
import pandas as pd

# Load the query results from the provided storage file paths
with open(var_call_8FJWfpiqbOp3DPmVAF68oBct, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_YXYcu0YtJWFdqUv3G6KRKyfK, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Create DataFrames
cit_df = pd.DataFrame(citations)
pap_df = pd.DataFrame(papers)

# Normalize citations: ensure citation_count is int
cit_df['citation_count'] = cit_df['citation_count'].astype(int)

# Normalize paper titles: derive title from filename by removing .txt
pap_df['title'] = pap_df['filename'].str.replace(r"\.txt$", '', regex=True)

# Merge on title
merged = pd.merge(cit_df, pap_df[['title', 'text']], on='title', how='left')

# Filter papers where text indicates ACM as publisher (case-insensitive word match)
merged['is_acm'] = merged['text'].fillna('').str.contains(r"\bACM\b", case=False, regex=True)
acm_papers = merged[merged['is_acm']]

# Compute average citation count
if len(acm_papers) == 0:
    avg = None
else:
    avg = acm_papers['citation_count'].mean()
    # Round to 2 decimal places for readability
    avg = round(float(avg), 2)

result = {
    'average_citation_count': avg,
    'acm_paper_count': int(len(acm_papers))
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_8FJWfpiqbOp3DPmVAF68oBct': 'file_storage/call_8FJWfpiqbOp3DPmVAF68oBct.json', 'var_call_YXYcu0YtJWFdqUv3G6KRKyfK': 'file_storage/call_YXYcu0YtJWFdqUv3G6KRKyfK.json'}

exec(code, env_args)
