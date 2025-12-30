code = """import re, json, pandas as pd
from pathlib import Path

with open(var_call_uLJTeZlWKZHjQvuNomf3W3Tj, 'r') as f:
    papers = json.load(f)
with open(var_call_YQ0mViRvzGEZnCPDnLPVtPTJ, 'r') as f:
    citations = json.load(f)

year_pattern = re.compile(r'\b(20[0-2][0-9])\b')

records = []
for doc in papers:
    text = doc.get('text', '')
    if 'empirical' not in text.lower():
        continue
    years = [int(y) for y in year_pattern.findall(text)]
    year = min(years) if years else None
    if year is None or year <= 2016:
        continue
    title = doc.get('filename','').rsplit('.txt',1)[0]
    records.append({'title': title, 'year': year})

papers_df = pd.DataFrame(records)

cites_df = pd.DataFrame(citations)
# inspect columns
cols = list(cites_df.columns)

import json as _json
out = {'papers_sample': papers_df.head(5).to_dict(orient='records'), 'citation_cols': cols, 'cites_sample': cites_df.head(5).to_dict(orient='records')}

print('__RESULT__:')
print(_json.dumps(out))"""

env_args = {'var_call_uLJTeZlWKZHjQvuNomf3W3Tj': 'file_storage/call_uLJTeZlWKZHjQvuNomf3W3Tj.json', 'var_call_YQ0mViRvzGEZnCPDnLPVtPTJ': 'file_storage/call_YQ0mViRvzGEZnCPDnLPVtPTJ.json'}

exec(code, env_args)
