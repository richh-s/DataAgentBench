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
cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

# Find docs with physical activity and 2016 near header
rows=[]
for d in md:
    text = d.get('text','')
    if re.search(r'physical\s+activity', text, flags=re.I):
        # year from copyright
        m = re.search(r'Copyright\s+(\d{4})', text[:4000], flags=re.I)
        year = int(m.group(1)) if m else None
        if year==2016:
            title = d.get('filename','')
            if title.lower().endswith('.txt'):
                title = title[:-4]
            rows.append({'title': title})

papers=pd.DataFrame(rows).drop_duplicates()
out = papers.merge(cit_df, on='title', how='left')
out['total_citations']=out['total_citations'].fillna(0).astype(int)
out=out.sort_values(['total_citations','title'], ascending=[False,True])
result=out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_zYyrGcCxbdn8jeAcpsO8OfVU': 'file_storage/call_zYyrGcCxbdn8jeAcpsO8OfVU.json', 'var_call_ld2V1lYUHjPBEP7CbAaRSHh9': 'file_storage/call_ld2V1lYUHjPBEP7CbAaRSHh9.json', 'var_call_oDvXuC619CaSfcHzdYDWIS43': [], 'var_call_Vt4ZcXEWFh6qX1mVKUcZSUIZ': 'file_storage/call_Vt4ZcXEWFh6qX1mVKUcZSUIZ.json'}

exec(code, env_args)
