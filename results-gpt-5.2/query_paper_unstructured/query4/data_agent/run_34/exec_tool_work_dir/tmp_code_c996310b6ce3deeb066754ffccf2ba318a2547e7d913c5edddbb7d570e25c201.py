code = """import json, re
import pandas as pd

# Load mongo docs (may be in file)
mongo_res = var_call_uPGY0m7t0J8lvXs36c68DQ0U
if isinstance(mongo_res, str):
    with open(mongo_res, 'r', encoding='utf-8') as f:
        mongo_res = json.load(f)

cit_res = var_call_52SDZglZvXds3zraoOkaQ6ZV
if isinstance(cit_res, str):
    with open(cit_res, 'r', encoding='utf-8') as f:
        cit_res = json.load(f)

# helper extract year and domain from text
venue_re = re.compile(r"\b(CHI|Ubicomp|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\b")

def extract_year(text):
    # look for typical citation line like 'CHI 2016' or '2016,'
    m = re.search(r"\b(19|20)\d{2}\b", text)
    if not m:
        return None
    # prefer 2016 if present
    if re.search(r"\b2016\b", text):
        return 2016
    return int(m.group(0))

def is_physical_activity(text):
    # domain contains matching
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
if not cit_df.empty:
    # total_citations might be string
    cit_df['total_citations']=pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

out=pd.merge(papers_df, cit_df, on='title', how='left')
out['total_citations']=out['total_citations'].fillna(0).astype(int)
out=out.sort_values(['total_citations','title'], ascending=[False, True])
result=out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_uPGY0m7t0J8lvXs36c68DQ0U': 'file_storage/call_uPGY0m7t0J8lvXs36c68DQ0U.json', 'var_call_52SDZglZvXds3zraoOkaQ6ZV': 'file_storage/call_52SDZglZvXds3zraoOkaQ6ZV.json'}

exec(code, env_args)
