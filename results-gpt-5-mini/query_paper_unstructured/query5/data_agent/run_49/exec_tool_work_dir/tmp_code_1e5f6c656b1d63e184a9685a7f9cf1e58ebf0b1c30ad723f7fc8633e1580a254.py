code = """import json
import re
import pandas as pd

# Load data from storage file paths
with open(var_call_fyy8qeXrrcwP3ziXUvVy0mmB, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_i0bVz9Wu1fG8bFGs1JMg6jmP, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Create DataFrames
df_c = pd.DataFrame(citations)
df_docs = pd.DataFrame(docs)

# Normalize titles from filenames
if 'filename' in df_docs.columns:
    df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)
else:
    df_docs['title'] = ''

# Heuristic to detect CHI venue: look for the word 'CHI' in the first 1000 characters
pattern = re.compile(r"\bCHI\b", flags=re.IGNORECASE)

def is_chi(text):
    if not isinstance(text, str):
        return False
    head = text[:1000]
    return bool(pattern.search(head))

if 'text' in df_docs.columns:
    df_docs['is_chi'] = df_docs['text'].apply(is_chi)
else:
    df_docs['is_chi'] = False

# Get titles of CHI papers
chi_titles = df_docs[df_docs['is_chi']]['title'].tolist()

# Prepare citation counts
if 'citation_count' in df_c.columns:
    df_c['citation_count'] = pd.to_numeric(df_c['citation_count'], errors='coerce').fillna(0).astype(int)
else:
    df_c['citation_count'] = 0

# Filter citations for CHI papers
df_chi_cit = df_c[df_c['title'].isin(chi_titles)].copy()

# Prepare result
records = df_chi_cit[['title', 'citation_count']].to_dict(orient='records')
total = int(df_chi_cit['citation_count'].sum())
result = {'papers': records, 'total_citations_2020': total}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_fyy8qeXrrcwP3ziXUvVy0mmB': 'file_storage/call_fyy8qeXrrcwP3ziXUvVy0mmB.json', 'var_call_i0bVz9Wu1fG8bFGs1JMg6jmP': 'file_storage/call_i0bVz9Wu1fG8bFGs1JMg6jmP.json'}

exec(code, env_args)
