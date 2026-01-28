code = """import json
import pandas as pd
import re

# Load data from storage paths
with open(var_call_IgMGRy82fd6CM3YSp579uesP, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_bj5IIhfHCAcIpURljX3hdbZG, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# DataFrames
df_docs = pd.DataFrame(docs)
df_citations = pd.DataFrame(citations)

# Normalize title function
def normalize_title(t):
    if t is None:
        return ""
    t = t.strip()
    # remove surrounding quotes
    t = re.sub(r'^\s*["\']+|["\']+\s*$', '', t)
    # collapse whitespace
    t = re.sub(r"\s+", ' ', t)
    return t.lower()

# Extract year heuristic
def extract_pub_year(text):
    if not isinstance(text, str):
        return None
    header = text[:1500]
    if re.search(r"\b2016\b", header):
        return 2016
    m = re.search(r"\b2016\b", text)
    if m and m.start() < 1200:
        return 2016
    return None

# Determine domain presence
def has_physical_activity(text):
    if not isinstance(text, str):
        return False
    return bool(re.search(r"physical activity", text, re.I))

# Prepare docs dataframe
if 'filename' not in df_docs.columns or 'text' not in df_docs.columns:
    result = []
else:
    df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)
    df_docs['norm_title'] = df_docs['title'].apply(normalize_title)
    df_docs['year'] = df_docs['text'].apply(extract_pub_year)
    df_docs['has_physical_activity'] = df_docs['text'].apply(has_physical_activity)

    # Filter for year 2016 and domain physical activity
    df_filtered = df_docs[(df_docs['year'] == 2016) & (df_docs['has_physical_activity'])]

    # Prepare citations df
    if 'title' in df_citations.columns and 'total_citations' in df_citations.columns:
        df_citations['norm_title'] = df_citations['title'].apply(lambda x: normalize_title(x))
        # Convert total_citations to int
        df_citations['total_citations'] = df_citations['total_citations'].astype(int)

        # Merge on normalized title
        merged = pd.merge(df_filtered, df_citations, left_on='norm_title', right_on='norm_title', how='left', suffixes=('_doc', '_cite'))

        # Build result list
        result = []
        for _, row in merged.iterrows():
            title_out = row['title_doc'] if 'title_doc' in row and pd.notna(row['title_doc']) else row.get('title', '')
            # If citation total missing, set to 0
            total = int(row['total_citations']) if 'total_citations' in row and pd.notna(row['total_citations']) else 0
            result.append({
                'title': title_out,
                'total_citations': total
            })
    else:
        result = []

# Print result in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GCr1zw7xx9xk1G0vBAUywNW4': ['paper_docs'], 'var_call_IgMGRy82fd6CM3YSp579uesP': 'file_storage/call_IgMGRy82fd6CM3YSp579uesP.json', 'var_call_fbCH73ERsJiR8V8GgNikjxAJ': ['Citations', 'sqlite_sequence'], 'var_call_bj5IIhfHCAcIpURljX3hdbZG': 'file_storage/call_bj5IIhfHCAcIpURljX3hdbZG.json'}

exec(code, env_args)
