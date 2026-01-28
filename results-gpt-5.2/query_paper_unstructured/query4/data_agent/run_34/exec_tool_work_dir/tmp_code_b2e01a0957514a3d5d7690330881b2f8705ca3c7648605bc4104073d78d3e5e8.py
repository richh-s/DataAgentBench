code = """import json, re
import pandas as pd

mongo_res = var_call_uPGY0m7t0J8lvXs36c68DQ0U
if isinstance(mongo_res, str):
    with open(mongo_res, 'r', encoding='utf-8') as f:
        mongo_res = json.load(f)

cit_res = var_call_52SDZglZvXds3zraoOkaQ6ZV
if isinstance(cit_res, str):
    with open(cit_res, 'r', encoding='utf-8') as f:
        cit_res = json.load(f)


def extract_year(text):
    if re.search(r"\b2016\b", text):
        return 2016
    m = re.search(r"\b(19|20)\d{2}\b", text)
    return int(m.group(0)) if m else None

def is_physical_activity(text):
    return re.search(r"(?i)physical\s+activity", text) is not None

papers=[]
for d in mongo_res:
    fn=d.get('filename','')
    title=fn[:-4] if fn.lower().endswith('.txt') else fn
    text=d.get('text','') or ''
    if not is_physical_activity(text):
        continue
    yr=extract_year(text)
    if yr!=2016:
        continue
    papers.append({'title': title})

papers_df=pd.DataFrame(papers).drop_duplicates()

cit_df=pd.DataFrame(cit_res)
# normalize columns
if 'total_citations' not in cit_df.columns and 'SUM(citation_count)' in cit_df.columns:
    cit_df = cit_df.rename(columns={'SUM(citation_count)':'total_citations'})
if 'title' not in cit_df.columns:
    # try case variants
    for c in cit_df.columns:
        if c.lower()=='title':
            cit_df=cit_df.rename(columns={c:'title'})
            break

if not cit_df.empty:
    cit_df['total_citations']=pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

if papers_df.empty:
    result=[]
else:
    out=pd.merge(papers_df, cit_df[['title','total_citations']], on='title', how='left')
    out['total_citations']=out['total_citations'].fillna(0).astype(int)
    out=out.sort_values(['total_citations','title'], ascending=[False, True])
    result=out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_uPGY0m7t0J8lvXs36c68DQ0U': 'file_storage/call_uPGY0m7t0J8lvXs36c68DQ0U.json', 'var_call_52SDZglZvXds3zraoOkaQ6ZV': 'file_storage/call_52SDZglZvXds3zraoOkaQ6ZV.json'}

exec(code, env_args)
