code = """import json
import re
import pandas as pd

# Load results from previous tool calls (file paths)
with open(var_call_9n2jggcUPYMKWrcaQZltXrU5, 'r') as f:
    citations = json.load(f)
with open(var_call_9vJrp2igNez58Y88RnbtN12T, 'r') as f:
    docs = json.load(f)

# Create DataFrames
df_cit = pd.DataFrame(citations)
# Ensure citation_count is int
if 'citation_count' in df_cit.columns:
    df_cit['citation_count'] = df_cit['citation_count'].astype(int)

# Prepare docs DataFrame: extract title from filename
df_docs = pd.DataFrame(docs)
# Some filenames may include path or weird chars; strip trailing .txt
df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)

# Merge on title
df_merged = pd.merge(df_cit, df_docs[['title', 'text']], on='title', how='left')

# Function to detect ACM as source in text
acm_pattern = re.compile(r"\bACM\b", re.IGNORECASE)

def is_acm(text):
    if not isinstance(text, str):
        return False
    if acm_pattern.search(text):
        return True
    # also check for common copyright patterns
    if 'copyright' in text.lower() and 'acm' in text.lower():
        return True
    return False

# Apply detection
df_merged['is_acm'] = df_merged['text'].apply(is_acm)

# Filter ACM
df_acm = df_merged[df_merged['is_acm'] == True]

# Compute average citation_count
if len(df_acm) == 0:
    avg_citations = None
else:
    avg_citations = df_acm['citation_count'].mean()

result = {
    'average_citation_count_2018_for_ACM_papers': (None if avg_citations is None else round(float(avg_citations), 4)),
    'matched_acm_papers_count': int(len(df_acm)),
    'total_citation_records_in_2018': int(len(df_cit))
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_9n2jggcUPYMKWrcaQZltXrU5': 'file_storage/call_9n2jggcUPYMKWrcaQZltXrU5.json', 'var_call_9vJrp2igNez58Y88RnbtN12T': 'file_storage/call_9vJrp2igNez58Y88RnbtN12T.json'}

exec(code, env_args)
