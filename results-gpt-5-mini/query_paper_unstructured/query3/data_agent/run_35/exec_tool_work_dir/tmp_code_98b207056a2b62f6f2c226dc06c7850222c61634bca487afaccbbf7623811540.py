code = """import json
import pandas as pd
import re

# Load the Mongo query result (stored as a .json file path)
path_mongo = var_call_5Fr9YDfjdx1RAzPDo7Hd08hK
with open(path_mongo, 'r', encoding='utf-8') as f:
    mongo_docs = json.load(f)

# Load the Citations aggregate result (stored as a .json file path)
path_cit = var_call_wLc89tLLAQJxpXJLjZQRx4G8
with open(path_cit, 'r', encoding='utf-8') as f:
    citations_agg = json.load(f)

# Create DataFrames
dfm = pd.DataFrame(mongo_docs)
if 'filename' not in dfm.columns:
    dfm['filename'] = None
if 'text' not in dfm.columns:
    dfm['text'] = None

# Extract title from filename (remove .txt)
dfm['title'] = dfm['filename'].astype(str).str.replace(r"\.txt$", "", regex=True)

# Extract publication year from text (first occurrence of years 2017-2026)
def extract_year(text):
    if not isinstance(text, str):
        return None
    m = re.search(r"\b(2017|2018|2019|2020|2021|2022|2023|2024|2025|2026)\b", text)
    return int(m.group(1)) if m else None

dfm['year'] = dfm['text'].apply(extract_year)

# Filter papers published after 2016 and containing 'empirical' in text
dfm_filtered = dfm[dfm['year'].notnull()]
dfm_filtered = dfm_filtered[dfm_filtered['year'] > 2016]
dfm_filtered = dfm_filtered[dfm_filtered['text'].str.lower().str.contains('empirical', na=False)]

# Prepare citations DataFrame
dfc = pd.DataFrame(citations_agg)
if 'title' not in dfc.columns:
    dfc['title'] = None
if 'total_citations' not in dfc.columns:
    dfc['total_citations'] = 0

dfc['title'] = dfc['title'].astype(str).str.strip()
# Convert total_citations to integer where possible
dfc['total_citations'] = pd.to_numeric(dfc['total_citations'], errors='coerce').fillna(0).astype(int)

# Merge on title
merged = pd.merge(dfm_filtered[['title','year']], dfc[['title','total_citations']], on='title', how='left')
# Replace NaN total_citations with None to indicate missing
merged['total_citations'] = merged['total_citations'].where(pd.notnull(merged['total_citations']), None)

# Build output list
output = []
for _, row in merged.iterrows():
    tc = None if row['total_citations'] is None else int(row['total_citations'])
    output.append({'title': row['title'], 'total_citations': tc})

import json as _json
print("__RESULT__:")
print(_json.dumps(output))"""

env_args = {'var_call_x3lcIfFpwdG8R83HKaR6vCyr': ['paper_docs'], 'var_call_dwPh5YwNHNe5FaYBiOE7aDyC': ['Citations', 'sqlite_sequence'], 'var_call_5Fr9YDfjdx1RAzPDo7Hd08hK': 'file_storage/call_5Fr9YDfjdx1RAzPDo7Hd08hK.json', 'var_call_wLc89tLLAQJxpXJLjZQRx4G8': 'file_storage/call_wLc89tLLAQJxpXJLjZQRx4G8.json'}

exec(code, env_args)
