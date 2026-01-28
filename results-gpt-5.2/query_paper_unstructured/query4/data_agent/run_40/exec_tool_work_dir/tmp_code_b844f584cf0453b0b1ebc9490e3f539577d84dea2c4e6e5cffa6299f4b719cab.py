code = """import json, re, pandas as pd

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

mongo_recs = load_maybe_path(var_call_sTOTPpLvdzZRAbkte2NRypwi)
cit_recs = load_maybe_path(var_call_Gcy9OwZ4BPgbXR3BKg8KmU3S)

cit_df = pd.DataFrame(cit_recs)
if not cit_df.empty:
    if 'total_citations' not in cit_df.columns and 'SUM(citation_count)' in cit_df.columns:
        cit_df = cit_df.rename(columns={'SUM(citation_count)':'total_citations'})
    cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)
    cit_map = dict(zip(cit_df['title'], cit_df['total_citations']))
else:
    cit_map = {}

year_pat = re.compile(r'\b(19\d{2}|20\d{{2}})\b')
# fix regex typo by compiling correctly
year_pat = re.compile(r'\b(19\d{2}|20\d{2})\b')

def infer_year(text):
    head = text[:2000]
    yrs = [int(y) for y in year_pat.findall(head)]
    yrs = [y for y in yrs if 2000 <= y <= 2026]
    if not yrs:
        return None
    return min(yrs)

rows=[]
for r in mongo_recs:
    title = (r.get('filename','') or '').replace('.txt','')
    yr = infer_year(r.get('text','') or '')
    if yr==2016:
        rows.append({'title': title, 'total_citations': int(cit_map.get(title,0))})

out_df=pd.DataFrame(rows).drop_duplicates().sort_values(['total_citations','title'], ascending=[False,True])
print('__RESULT__:')
print(json.dumps(out_df.to_dict(orient='records'), ensure_ascii=False))"""

env_args = {'var_call_8AQzsnVK3pjf8qv96fVixUDd': 'file_storage/call_8AQzsnVK3pjf8qv96fVixUDd.json', 'var_call_Gcy9OwZ4BPgbXR3BKg8KmU3S': 'file_storage/call_Gcy9OwZ4BPgbXR3BKg8KmU3S.json', 'var_call_CuwislDkhq3PJKeBDgFmstlY': [], 'var_call_sTOTPpLvdzZRAbkte2NRypwi': 'file_storage/call_sTOTPpLvdzZRAbkte2NRypwi.json'}

exec(code, env_args)
