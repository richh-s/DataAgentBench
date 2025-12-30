code = """import re, json
import pandas as pd

path_docs = var_call_rQhO3J8ababzRmEaiUYRdlip
with open(path_docs, 'r') as f:
    docs = json.load(f)

records = []
for d in docs:
    text = d.get('text','')
    year = 2016 if '2016' in text else None
    domain = 'physical activity' if re.search(r"physical activity", text, re.I) else None
    if year == 2016 and domain == 'physical activity':
        title = d.get('filename','').rsplit('.txt',1)[0]
        records.append({'title': title, 'year': year, 'domain': domain})

path_cit = var_call_syR0Ndh1j0mfqkBPI1WLJhad
with open(path_cit, 'r') as f:
    cits = json.load(f)

cit_df = pd.DataFrame(cits)
if 'title' in cit_df.columns:
    cit_df['title_clean'] = cit_df['title'].astype(str).str.replace('"','', regex=False)
else:
    cit_df['title_clean'] = []

paper_df = pd.DataFrame(records)
if not paper_df.empty and 'title_clean' in cit_df.columns:
    merged = paper_df.merge(cit_df, left_on='title', right_on='title_clean', how='left')
    if 'total_citations' in merged.columns:
        merged['total_citations'] = merged['total_citations'].astype(float).fillna(0).astype(int)
        out = merged[['title','total_citations']].to_dict(orient='records')
    else:
        out = merged[['title']].to_dict(orient='records')
else:
    out = []

res = json.dumps(out)
print("__RESULT__:")
print(res)"""

env_args = {'var_call_rQhO3J8ababzRmEaiUYRdlip': 'file_storage/call_rQhO3J8ababzRmEaiUYRdlip.json', 'var_call_syR0Ndh1j0mfqkBPI1WLJhad': 'file_storage/call_syR0Ndh1j0mfqkBPI1WLJhad.json'}

exec(code, env_args)
