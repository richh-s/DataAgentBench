code = """import json
import re
import pandas as pd

# Load the Mongo query result (stored in a JSON file path)
with open(var_call_kIFXeteoQUbuva9crHgsAZD8, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Load the citations aggregated result
with open(var_call_BKp0vng3tViWqcspUiohZKn8, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build DataFrame for papers
rows = []
for doc in papers:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text', '') or ''
    # find year: look for 4-digit year between 1900 and 2026, prefer first occurrence near top
    years = re.findall(r"\b(19[5-9][0-9]|20[0-2][0-9]|2026)\b", text)
    year = None
    if years:
        try:
            year = int(years[0])
        except:
            year = None
    # contribution: check if 'empirical' substring appears
    contribution_empirical = 'empirical' in text.lower()
    rows.append({'title': title.strip(), 'year': year, 'empirical': contribution_empirical})

df_papers = pd.DataFrame(rows)
# drop papers without year
df_papers = df_papers[df_papers['year'].notnull()].copy()
# filter year > 2016 and empirical
df_papers = df_papers[(df_papers['year'] > 2016) & (df_papers['empirical'])]

# Build citations DataFrame
df_cit = pd.DataFrame(citations)
# normalize column names
if 'total_citations' in df_cit.columns:
    df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)
else:
    # if aggregated field named differently, try citation_count
    if 'citation_count' in df_cit.columns:
        df_cit['total_citations'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)
    else:
        df_cit['total_citations'] = 0

# strip titles in citations
df_cit['title'] = df_cit['title'].str.strip()

# join on title
merged = pd.merge(df_papers, df_cit, on='title', how='inner')

# prepare result list of dicts with title and total_citations
result = []
for _, r in merged.iterrows():
    result.append({'title': r['title'], 'total_citations': int(r['total_citations'])})

# Sort result by total_citations descending for readability
result = sorted(result, key=lambda x: x['total_citations'], reverse=True)

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_IuRfB0nUwQgBKOA6v7o0NdhJ': ['paper_docs'], 'var_call_JoyOfI0RlBzypbqQkpiuuxCr': ['Citations', 'sqlite_sequence'], 'var_call_kIFXeteoQUbuva9crHgsAZD8': 'file_storage/call_kIFXeteoQUbuva9crHgsAZD8.json', 'var_call_BKp0vng3tViWqcspUiohZKn8': 'file_storage/call_BKp0vng3tViWqcspUiohZKn8.json'}

exec(code, env_args)
