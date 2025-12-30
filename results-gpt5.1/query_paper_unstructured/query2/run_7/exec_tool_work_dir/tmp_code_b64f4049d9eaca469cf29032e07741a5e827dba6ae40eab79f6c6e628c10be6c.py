code = """import json
import pandas as pd

# Load citations data from storage file
with open(var_call_EN9qVK0j9H3NLX8OmVWYaIHZ, 'r') as f:
    citations = json.load(f)

# Create DataFrame
cit_df = pd.DataFrame(citations)

# Convert citation_count to int
cit_df['citation_count'] = cit_df['citation_count'].astype(int)

# We need only ACM papers, but source info is in paper docs; titles match filenames without .txt
# Load paper docs
with open(var_call_7tgA6xXdY2St4XLAAItnaApi, 'r') as f:
    papers = json.load(f)

paper_df = pd.DataFrame(papers)

# Derive title from filename
paper_df['title'] = paper_df['filename'].str.replace('.txt','', regex=False)

# Identify ACM papers by searching for 'Copyright' lines mentioning ACM in text
paper_df['is_acm'] = paper_df['text'].str.contains('Copyright', case=False, na=False) & paper_df['text'].str.contains('ACM', case=False, na=False)

# Merge citations with paper metadata on title
merged = cit_df.merge(paper_df[['title','is_acm']], on='title', how='left')

# Filter to ACM papers
acm_citations = merged[merged['is_acm'] == True]

# Compute average citation count
avg_citations = float(acm_citations['citation_count'].mean()) if not acm_citations.empty else None

import math
if avg_citations is not None:
    avg_citations = round(avg_citations, 2)

result = avg_citations

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_EN9qVK0j9H3NLX8OmVWYaIHZ': 'file_storage/call_EN9qVK0j9H3NLX8OmVWYaIHZ.json', 'var_call_7tgA6xXdY2St4XLAAItnaApi': 'file_storage/call_7tgA6xXdY2St4XLAAItnaApi.json'}

exec(code, env_args)
