code = """import json, re
import pandas as pd

md = var_call_Vt4ZcXEWFh6qX1mVKUcZSUIZ
if isinstance(md, str):
    with open(md, 'r', encoding='utf-8') as f:
        md = json.load(f)

cit = var_call_ld2V1lYUHjPBEP7CbAaRSHh9
if isinstance(cit, str):
    with open(cit, 'r', encoding='utf-8') as f:
        cit = json.load(f)

cit_df = pd.DataFrame(cit)
if 'total_citations' not in cit_df.columns and 'SUM(citation_count)' in cit_df.columns:
    cit_df = cit_df.rename(columns={'SUM(citation_count)':'total_citations'})

cit_df['title'] = cit_df['title'].astype(str)
cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

rows=[]
for d in md:
    text = d.get('text','') or ''
    if re.search(r'physical\s+activity', text, flags=re.I):
        m = re.search(r'Copyright\s+(\d{4})', text[:4000], flags=re.I)
        year = int(m.group(1)) if m else None
        if year==2016:
            title = d.get('filename','') or ''
            if title.lower().endswith('.txt'):
                title = title[:-4]
            rows.append({'title': title})

papers=pd.DataFrame(rows)
if papers.empty:
    result=[]
else:
    papers=papers.drop_duplicates('title')
    out = papers.merge(cit_df[['title','total_citations']], on='title', how='left')
    out['total_citations']=out['total_citations'].fillna(0).astype(int)
    out=out.sort_values(['total_citations','title'], ascending=[False,True])
    result=out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_zYyrGcCxbdn8jeAcpsO8OfVU': 'file_storage/call_zYyrGcCxbdn8jeAcpsO8OfVU.json', 'var_call_ld2V1lYUHjPBEP7CbAaRSHh9': 'file_storage/call_ld2V1lYUHjPBEP7CbAaRSHh9.json', 'var_call_oDvXuC619CaSfcHzdYDWIS43': [], 'var_call_Vt4ZcXEWFh6qX1mVKUcZSUIZ': 'file_storage/call_Vt4ZcXEWFh6qX1mVKUcZSUIZ.json'}

exec(code, env_args)
