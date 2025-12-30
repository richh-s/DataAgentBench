code = """import json, pandas as pd

path = var_call_QVVMdIHmtyFsuI5sqTG3yzN5
with open(path, 'r') as f:
    mongo_records = json.load(f)

import re
from datetime import datetime

papers = []
for rec in mongo_records:
    text = rec.get('text','')
    head = text[:2000]
    years = re.findall(r"(19[9][0-9]|20[0-2][0-9]|2030)", head)
    year = None
    for y in years:
        y_int = int(y)
        if 1990 <= y_int <= datetime.now().year:
            year = y_int
            break
    if not year or year <= 2016:
        continue
    if re.search(r"empirical", text, re.IGNORECASE):
        title = rec.get('filename','').replace('.txt','').strip()
        papers.append({'title': title, 'year': year})

df_papers = pd.DataFrame(papers)
if not df_papers.empty:
    df_papers = df_papers.sort_values(['title','year']).drop_duplicates('title', keep='first')

path2 = var_call_5UTLYr6CjRTZ3IeIVAZpQMJA
with open(path2, 'r') as f:
    cites = json.load(f)

df_cites = pd.DataFrame(cites)

if 'title' in df_cites.columns:
    df_cites['title_clean'] = df_cites['title'].str.replace('^\"|\"$','', regex=True)
else:
    df_cites['title_clean'] = ''

if not df_papers.empty:
    merged = pd.merge(df_papers, df_cites, left_on='title', right_on='title_clean', how='left')
    merged = merged[['title','year'] + ([c for c in merged.columns if c == 'total_citations'])]
    # rename total_citations if exists
    if 'total_citations' in merged.columns:
        merged = merged.rename(columns={'total_citations':'total_citation_count'})
    result = merged.to_dict(orient='records')
else:
    result = []

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_QVVMdIHmtyFsuI5sqTG3yzN5': 'file_storage/call_QVVMdIHmtyFsuI5sqTG3yzN5.json', 'var_call_5UTLYr6CjRTZ3IeIVAZpQMJA': 'file_storage/call_5UTLYr6CjRTZ3IeIVAZpQMJA.json'}

exec(code, env_args)
