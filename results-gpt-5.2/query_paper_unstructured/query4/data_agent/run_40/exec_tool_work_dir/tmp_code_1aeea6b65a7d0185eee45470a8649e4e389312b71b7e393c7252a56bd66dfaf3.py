code = """import json, re, pandas as pd

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

mongo_recs = load_maybe_path(var_call_sTOTPpLvdzZRAbkte2NRypwi)
cit_recs = load_maybe_path(var_call_Gcy9OwZ4BPgbXR3BKg8KmU3S)

cit_df = pd.DataFrame(cit_recs)
cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)
cit_map = dict(zip(cit_df['title'], cit_df['total_citations']))

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
    title = (r.get('filename','') or '')
    if title.lower().endswith('.txt'):
        title = title[:-4]
    yr = infer_year(r.get('text','') or '')
    if yr==2016:
        rows.append({'title': title, 'total_citations': int(cit_map.get(title,0))})

out_df=pd.DataFrame(rows)
if not out_df.empty:
    out_df=out_df.drop_duplicates().sort_values(['total_citations','title'], ascending=[False,True])
result=out_df.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_8AQzsnVK3pjf8qv96fVixUDd': 'file_storage/call_8AQzsnVK3pjf8qv96fVixUDd.json', 'var_call_Gcy9OwZ4BPgbXR3BKg8KmU3S': 'file_storage/call_Gcy9OwZ4BPgbXR3BKg8KmU3S.json', 'var_call_CuwislDkhq3PJKeBDgFmstlY': [], 'var_call_sTOTPpLvdzZRAbkte2NRypwi': 'file_storage/call_sTOTPpLvdzZRAbkte2NRypwi.json', 'var_call_53iSUuuy40M0TesDhNqEkEr4': [{'cid': '0', 'name': 'id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '1'}, {'cid': '1', 'name': 'title', 'type': 'TEXT', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'citation_count', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'citation_year', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}], 'var_call_jqJR2YFJJb1Bd6RAubD6yT4q': {'columns': ['title', 'total_citations'], 'head': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'total_citations': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'total_citations': '313'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}]}}

exec(code, env_args)
