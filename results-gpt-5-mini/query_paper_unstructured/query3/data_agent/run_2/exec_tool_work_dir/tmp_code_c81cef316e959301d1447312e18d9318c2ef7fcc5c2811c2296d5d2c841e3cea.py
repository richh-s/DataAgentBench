code = """import json, re, pandas as pd

# Load the large results from previous tool calls (file paths are provided in variables)
with open(var_call_cm45ai5zjnyskSalud4qTJFo, 'r', encoding='utf-8') as f:
    papers = json.load(f)
with open(var_call_lKMNNrH22tZXuQfe86upAyfx, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Prepare dataframes
df_papers = pd.DataFrame(papers)
# Extract title from filename
df_papers['title'] = df_papers['filename'].apply(lambda x: x[:-4] if x.lower().endswith('.txt') else x)

# Function to extract year from text: find first 4-digit year between 1900 and 2026
year_re = re.compile(r'\b(19\d{2}|20\d{2})\b')
def extract_year(text):
    if not isinstance(text, str):
        return None
    m = year_re.findall(text)
    if not m:
        return None
    # find first valid
    for yy in m:
        y = int(yy)
        if 1900 <= y <= 2026:
            return y
    return None

df_papers['year'] = df_papers['text'].apply(extract_year)

# Determine if contribution includes 'empirical' by searching text
df_papers['is_empirical'] = df_papers['text'].str.lower().str.contains('empirical', na=False)

# Load citations
df_cit = pd.DataFrame(citations)
# Ensure total_citations numeric
if not df_cit.empty:
    df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)

# Filter papers: empirical and year > 2016
df_filtered = df_papers[(df_papers['is_empirical']) & (df_papers['year'].notnull()) & (df_papers['year'] > 2016)].copy()

# Merge with citation totals
if df_cit.empty:
    df_filtered['total_citations'] = 0
else:
    df_merged = pd.merge(df_filtered, df_cit[['title','total_citations']], on='title', how='left')
    df_merged['total_citations'] = df_merged['total_citations'].fillna(0).astype(int)
    df_filtered = df_merged

# Prepare results: list of dicts with title and total_citations
results = df_filtered[['title','total_citations']].to_dict(orient='records')
# Sort by total_citations descending
results = sorted(results, key=lambda x: x['total_citations'], reverse=True)

import json
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_EdUzSjXspaM43prOHQZHWoTk': ['paper_docs'], 'var_call_9JMIC0xvORd9wzETOIlicpK9': ['Citations', 'sqlite_sequence'], 'var_call_cm45ai5zjnyskSalud4qTJFo': 'file_storage/call_cm45ai5zjnyskSalud4qTJFo.json', 'var_call_lKMNNrH22tZXuQfe86upAyfx': 'file_storage/call_lKMNNrH22tZXuQfe86upAyfx.json'}

exec(code, env_args)
