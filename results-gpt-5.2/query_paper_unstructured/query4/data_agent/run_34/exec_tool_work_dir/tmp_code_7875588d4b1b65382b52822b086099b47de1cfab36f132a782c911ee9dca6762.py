code = """import json
import pandas as pd
from collections import Counter

mongo_res = var_call_W6fqRVov3KWCsjikuA2KCNcS
if isinstance(mongo_res, str):
    with open(mongo_res, 'r', encoding='utf-8') as f:
        mongo_res = json.load(f)

cit_res = var_call_52SDZglZvXds3zraoOkaQ6ZV
if isinstance(cit_res, str):
    with open(cit_res, 'r', encoding='utf-8') as f:
        cit_res = json.load(f)


def pub_year_simple(text):
    head = (text or '')[:6000]
    years=[]
    for y in range(1990, 2027):
        if str(y) in head:
            years.append(y)
    if not years:
        return None
    if 2016 in years:
        return 2016
    return Counter(years).most_common(1)[0][0]

papers=[]
for d in mongo_res:
    fn=d.get('filename','')
    title=fn[:-4] if fn.lower().endswith('.txt') else fn
    if pub_year_simple(d.get('text',''))==2016:
        papers.append({'title': title})

papers_df=pd.DataFrame(papers).drop_duplicates()

cit_df=pd.DataFrame(cit_res)
if 'total_citations' not in cit_df.columns and 'SUM(citation_count)' in cit_df.columns:
    cit_df=cit_df.rename(columns={'SUM(citation_count)':'total_citations'})
for c in list(cit_df.columns):
    if c.lower()=='title' and c!='title':
        cit_df=cit_df.rename(columns={c:'title'})

cit_df['total_citations']=pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

out=pd.merge(papers_df, cit_df[['title','total_citations']], on='title', how='left')
out['total_citations']=out['total_citations'].fillna(0).astype(int)
out=out.sort_values(['total_citations','title'], ascending=[False, True])

result=out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_uPGY0m7t0J8lvXs36c68DQ0U': 'file_storage/call_uPGY0m7t0J8lvXs36c68DQ0U.json', 'var_call_52SDZglZvXds3zraoOkaQ6ZV': 'file_storage/call_52SDZglZvXds3zraoOkaQ6ZV.json', 'var_call_Dk5Vo5n9nazf7vWqaJWACDub': [], 'var_call_W6fqRVov3KWCsjikuA2KCNcS': 'file_storage/call_W6fqRVov3KWCsjikuA2KCNcS.json'}

exec(code, env_args)
