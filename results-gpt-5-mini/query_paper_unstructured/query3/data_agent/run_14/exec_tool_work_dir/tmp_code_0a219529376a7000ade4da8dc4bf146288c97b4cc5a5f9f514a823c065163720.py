code = """import json
import re
import pandas as pd

# Load large query results from storage paths
papers_path = var_call_idPFfHI1yVhLTJ8gvECCDLFs
citations_path = var_call_cjWxuMh7HE7wp9Zh3rOqK43u

with open(papers_path, 'r', encoding='utf-8') as f:
    papers = json.load(f)
with open(citations_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build DataFrames
papers_df = pd.DataFrame(papers)
# Extract title from filename
papers_df['title'] = papers_df['filename'].str.replace(r"\.txt$", '', regex=True)
# Lowercase text for searching
papers_df['text_low'] = papers_df['text'].str.lower()

# Function to extract year
venue_pattern = re.compile(r"\b(?:CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\b[^0-9]{0,20}(20\d{2})", re.I)

def extract_year(text):
    # Search for venue-year pattern
    m = venue_pattern.search(text[:1000])
    if m:
        try:
            y = int(m.group(1))
            return y
        except:
            pass
    # Fallback: first 4-digit year between 2000 and 2025 in first 400 chars
    m2 = re.search(r"\b(20\d{2})\b", text[:400])
    if m2:
        y = int(m2.group(1))
        return y
    # Fallback: any 4-digit between 2000-2025 anywhere
    m3 = re.search(r"\b(20\d{2})\b", text)
    if m3:
        return int(m3.group(1))
    return None

papers_df['year'] = papers_df['text'].apply(extract_year)

# Filter for empirical contribution and year > 2016
papers_df['has_empirical'] = papers_df['text_low'].str.contains('empirical')
filtered = papers_df[papers_df['has_empirical'] & papers_df['year'].notnull() & (papers_df['year'] > 2016)].copy()

# Prepare citations DataFrame
cit_df = pd.DataFrame(citations)
# Normalize title in citations (strip whitespace and possible surrounding quotes)
cit_df['title_norm'] = cit_df['title'].str.strip().str.strip('"')
# Convert total_citations to int
cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

# Merge: left join filtered papers with citations by title
filtered['title_norm'] = filtered['title'].str.strip()
merged = pd.merge(filtered, cit_df[['title_norm','total_citations']], on='title_norm', how='left')
merged['total_citations'] = merged['total_citations'].fillna(0).astype(int)

# Build result list
result = []
for _, row in merged.iterrows():
    result.append({'title': row['title'], 'total_citations': int(row['total_citations']), 'year': int(row['year'])})

# Sort results by total_citations desc
result = sorted(result, key=lambda x: x['total_citations'], reverse=True)

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_V9b2IXSfF9cZmQsCIVpYRBWT': ['paper_docs'], 'var_call_1YqjRGLj3P2sTAQRS36APHNJ': ['Citations', 'sqlite_sequence'], 'var_call_idPFfHI1yVhLTJ8gvECCDLFs': 'file_storage/call_idPFfHI1yVhLTJ8gvECCDLFs.json', 'var_call_cjWxuMh7HE7wp9Zh3rOqK43u': 'file_storage/call_cjWxuMh7HE7wp9Zh3rOqK43u.json'}

exec(code, env_args)
