code = """import json
import pandas as pd
import re

# Load query results from storage file paths
with open(var_call_kmFjYj6j5sznE7zjNoguO6To, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_KxaJXQfWiKOCKq8MAtqzRDGn, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Create DataFrames
df_cit = pd.DataFrame(citations)
df_papers = pd.DataFrame(papers)

# Normalize titles: citations.title should match filename without .txt
# Ensure filename exists
if 'filename' in df_papers.columns:
    df_papers['title'] = df_papers['filename'].str.replace(r"\.txt$", '', regex=True)
else:
    df_papers['title'] = None

# Detect ACM in paper text (case-insensitive word match)
def contains_acm(text):
    if not isinstance(text, str):
        return False
    return bool(re.search(r"\bACM\b", text, flags=re.IGNORECASE))

df_papers['source_is_acm'] = df_papers['text'].apply(contains_acm)

# Clean citations: ensure citation_count numeric
if 'citation_count' in df_cit.columns:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')
else:
    df_cit['citation_count'] = pd.NA

# Trim whitespace on titles
if 'title' in df_cit.columns:
    df_cit['title'] = df_cit['title'].str.strip()
    df_papers['title'] = df_papers['title'].str.strip()

# Merge on title
merged = pd.merge(df_cit, df_papers[['title', 'source_is_acm']], on='title', how='left')

# Filter records where citation_year was 2018 already by earlier query; now filter ACM
acm_2018 = merged[merged['source_is_acm'] == True].copy()

# Compute average citation_count
acm_2018 = acm_2018[acm_2018['citation_count'].notna()]
count = int(acm_2018.shape[0])
average = float(acm_2018['citation_count'].mean()) if count > 0 else None

result = {
    'average_citation_count': average,
    'paper_count': count
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_kmFjYj6j5sznE7zjNoguO6To': 'file_storage/call_kmFjYj6j5sznE7zjNoguO6To.json', 'var_call_KxaJXQfWiKOCKq8MAtqzRDGn': 'file_storage/call_KxaJXQfWiKOCKq8MAtqzRDGn.json'}

exec(code, env_args)
