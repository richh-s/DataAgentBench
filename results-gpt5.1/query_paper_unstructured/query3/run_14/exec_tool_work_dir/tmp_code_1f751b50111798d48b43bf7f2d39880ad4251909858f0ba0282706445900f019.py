code = """import re, json, pandas as pd
from datetime import datetime

# Load full mongo results
path_docs = var_call_gfbxBbNwkooMzTidlX1tcQ3S
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Heuristic extract year from text
empirical_papers = []
for d in docs:
    text = d.get('text','')
    # contribution: must contain 'empirical'
    if 'empirical' not in text.lower():
        continue
    # year: look for CHI-like headers with years 2017-2025
    years = re.findall(r'20[1-2][0-9]', text)
    year = None
    for y in years:
        yi = int(y)
        if 2017 <= yi <= 2025:
            year = yi
            break
    if not year:
        continue
    title = d.get('filename','').replace('.txt','').strip()
    empirical_papers.append({'title': title, 'year': year})

# Deduplicate by title keeping earliest year
df_papers = pd.DataFrame(empirical_papers)
if not df_papers.empty:
    df_papers = df_papers.sort_values(['title','year']).drop_duplicates('title', keep='first')

# Load citations aggregated
path_cit = var_call_FzzPpDz1IvY04owJLG2eGnwu
with open(path_cit, 'r') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
if not df_cit.empty:
    df_cit['total_citations'] = df_cit['total_citations'].astype(int)

# Join on title
if df_papers.empty or df_cit.empty:
    result = []
else:
    merged = pd.merge(df_papers, df_cit, on='title', how='left')
    merged = merged[['title','total_citations']].fillna(0)
    result = merged.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_gfbxBbNwkooMzTidlX1tcQ3S': 'file_storage/call_gfbxBbNwkooMzTidlX1tcQ3S.json', 'var_call_FzzPpDz1IvY04owJLG2eGnwu': 'file_storage/call_FzzPpDz1IvY04owJLG2eGnwu.json'}

exec(code, env_args)
