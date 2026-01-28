code = """import json, pandas as pd, re

# Load JSON results from previous tool calls
with open(var_call_IgMGRy82fd6CM3YSp579uesP, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_bj5IIhfHCAcIpURljX3hdbZG, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# DataFrames
df_docs = pd.DataFrame(docs)
df_cit = pd.DataFrame(citations)

# Helper functions
def normalize_title(t):
    if pd.isna(t):
        return ""
    s = str(t).strip()
    s = re.sub(r"^[\'\"]+|[\'\"]+$", '', s)
    s = re.sub(r"\s+", ' ', s)
    return s.lower()

def extract_pub_year(text):
    if not isinstance(text, str):
        return None
    header = text[:1500]
    if re.search(r"\b2016\b", header):
        return 2016
    return None

def has_physical_activity(text):
    return isinstance(text, str) and re.search(r"physical activity", text, re.I) is not None

# Prepare docs
if 'filename' in df_docs.columns and 'text' in df_docs.columns:
    df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)
    df_docs['norm_title'] = df_docs['title'].apply(normalize_title)
    df_docs['year'] = df_docs['text'].apply(extract_pub_year)
    df_docs['has_physical_activity'] = df_docs['text'].apply(has_physical_activity)
    df_filtered = df_docs[(df_docs['year'] == 2016) & (df_docs['has_physical_activity'])]
else:
    df_filtered = pd.DataFrame()

# Prepare citations
if 'title' in df_cit.columns and 'total_citations' in df_cit.columns:
    df_cit['norm_title'] = df_cit['title'].apply(normalize_title)
    df_cit['total_citations'] = df_cit['total_citations'].astype(int)
else:
    df_cit['norm_title'] = []
    df_cit['total_citations'] = []

# Merge
if not df_filtered.empty:
    merged = pd.merge(df_filtered, df_cit, on='norm_title', how='left', suffixes=('_doc', '_cite'))
else:
    merged = pd.DataFrame()

result = []
for _, row in merged.iterrows():
    title_out = ''
    if 'title_doc' in row and pd.notna(row['title_doc']):
        title_out = row['title_doc']
    elif 'title' in row and pd.notna(row['title']):
        title_out = row['title']
    total = int(row['total_citations']) if 'total_citations' in row and pd.notna(row['total_citations']) else 0
    result.append({'title': title_out, 'total_citations': total})

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GCr1zw7xx9xk1G0vBAUywNW4': ['paper_docs'], 'var_call_IgMGRy82fd6CM3YSp579uesP': 'file_storage/call_IgMGRy82fd6CM3YSp579uesP.json', 'var_call_fbCH73ERsJiR8V8GgNikjxAJ': ['Citations', 'sqlite_sequence'], 'var_call_bj5IIhfHCAcIpURljX3hdbZG': 'file_storage/call_bj5IIhfHCAcIpURljX3hdbZG.json'}

exec(code, env_args)
