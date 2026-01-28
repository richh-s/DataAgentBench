code = """import json
import pandas as pd
import re

# Load data from storage files
with open(var_call_9OQjxwNnIkl9chguzg8khYlU, 'r') as f:
    papers = json.load(f)
with open(var_call_1Ish7gejTavO6J3UUuqY1vlh, 'r') as f:
    citations = json.load(f)

# DataFrames
df_p = pd.DataFrame(papers)
# Create title column from filename by removing trailing .txt
if 'filename' in df_p.columns:
    df_p['title'] = df_p['filename'].apply(lambda x: x.rsplit('.txt', 1)[0])
else:
    df_p['title'] = None

# Detect ACM as source: look for explicit 'ACM' or 'Copyright' lines mentioning ACM
def is_acm(text):
    if not isinstance(text, str):
        return False
    # common patterns
    if re.search(r"\bACM\b", text):
        return True
    if re.search(r"Copyright.*ACM", text, re.IGNORECASE):
        return True
    if re.search(r"\u00a9\s*ACM", text):
        return True
    return False

df_p['source_acm'] = df_p['text'].apply(is_acm)

# Prepare citations dataframe
df_c = pd.DataFrame(citations)
# Ensure correct types
if 'citation_count' in df_c.columns:
    df_c['citation_count'] = pd.to_numeric(df_c['citation_count'], errors='coerce')
else:
    df_c['citation_count'] = pd.Series(dtype='float')

# Merge on title
merged = pd.merge(df_c, df_p[['title', 'source_acm']], on='title', how='left')
# Filter to ACM source
merged_acm = merged[merged['source_acm'] == True]

# Compute average citation_count
if len(merged_acm) > 0:
    avg = float(merged_acm['citation_count'].mean())
    # also number of papers considered
    count = int(len(merged_acm))
else:
    avg = None
    count = 0

result = {"average_citation_count": avg, "paper_count": count}

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_9OQjxwNnIkl9chguzg8khYlU': 'file_storage/call_9OQjxwNnIkl9chguzg8khYlU.json', 'var_call_TWKeuGfyeNcCLldmkazgx5w3': ['Citations', 'sqlite_sequence'], 'var_call_1Ish7gejTavO6J3UUuqY1vlh': 'file_storage/call_1Ish7gejTavO6J3UUuqY1vlh.json'}

exec(code, env_args)
