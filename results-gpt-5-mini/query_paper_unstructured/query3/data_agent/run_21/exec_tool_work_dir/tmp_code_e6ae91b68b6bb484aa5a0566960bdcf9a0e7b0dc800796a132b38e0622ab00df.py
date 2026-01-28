code = """import json
import pandas as pd
import re

# Load large results from storage file paths provided by previous tool calls
with open(var_call_AxVOzOTTTZQmHbSEpF5rfQAk, 'r', encoding='utf-8') as f:
    papers = json.load(f)

with open(var_call_cLsDcXYtcvhTiAB2DNKlxHzD, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Create DataFrames
df_p = pd.DataFrame(papers)
df_c = pd.DataFrame(citations)

# Extract title from filename
if 'filename' in df_p.columns:
    df_p['title'] = df_p['filename'].str.replace('.txt', '', regex=False).str.strip()
else:
    df_p['title'] = None

# Function to extract publication year: look in the first 2000 chars, fallback to whole text
year_re = re.compile(r'(19|20)\d{2}')

def extract_year(text):
    if not isinstance(text, str):
        return None
    sample = text[:2000]
    m = year_re.search(sample)
    if m:
        return int(m.group(0))
    m = year_re.search(text)
    if m:
        return int(m.group(0))
    return None

# Apply extraction
df_p['year'] = df_p['text'].apply(extract_year)
# Detect 'empirical' contribution by substring match (case-insensitive)
df_p['empirical'] = df_p['text'].str.lower().str.contains('empirical', na=False)

# Filter: empirical contribution and published after 2016
filtered = df_p[(df_p['empirical'] == True) & (df_p['year'].notnull()) & (df_p['year'] > 2016)].copy()

# Prepare citations dataframe
# Ensure columns exist
if 'title' in df_c.columns and 'total_citations' in df_c.columns:
    df_c['title'] = df_c['title'].str.strip()
    # Convert total_citations to int
    df_c['total_citations'] = df_c['total_citations'].astype(int)
else:
    df_c = pd.DataFrame(columns=['title','total_citations'])

# Merge on title
merged = pd.merge(filtered, df_c, on='title', how='left')
merged['total_citations'] = merged['total_citations'].fillna(0).astype(int)

# Prepare output: list of {title, total_citations}
output = merged[['title','total_citations']].drop_duplicates().to_dict(orient='records')

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_0LDWmk2WBdPVRgIrJ8N0swGW': ['paper_docs'], 'var_call_AxVOzOTTTZQmHbSEpF5rfQAk': 'file_storage/call_AxVOzOTTTZQmHbSEpF5rfQAk.json', 'var_call_cLsDcXYtcvhTiAB2DNKlxHzD': 'file_storage/call_cLsDcXYtcvhTiAB2DNKlxHzD.json'}

exec(code, env_args)
