code = """import json, re, pandas as pd

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

mongo_recs = load_maybe_path(var_call_8AQzsnVK3pjf8qv96fVixUDd)
cit_recs = load_maybe_path(var_call_Gcy9OwZ4BPgbXR3BKg8KmU3S)

cit_df = pd.DataFrame(cit_recs)
# normalize column names
if not cit_df.empty:
    if 'total_citations' not in cit_df.columns and 'SUM(citation_count)' in cit_df.columns:
        cit_df = cit_df.rename(columns={'SUM(citation_count)':'total_citations'})
    cit_df['total_citations'] = pd.to_numeric(cit_df.get('total_citations', 0), errors='coerce').fillna(0).astype(int)
    cit_map = dict(zip(cit_df['title'], cit_df['total_citations']))
else:
    cit_map = {}

year_pat = re.compile(r'\b(19\d{2}|20\d{2})\b')

def infer_year(text):
    head = text[:1500]
    yrs = [int(y) for y in year_pat.findall(head)]
    if not yrs:
        yrs = [int(y) for y in year_pat.findall(text[:5000])]
    yrs = [y for y in yrs if 2000 <= y <= 2026]
    if not yrs:
        return None
    return min(yrs)

rows = []
for r in mongo_recs:
    fn = r.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = r.get('text','') or ''
    if re.search(r'(?i)physical activity', text) is None:
        continue
    yr = infer_year(text)
    if yr != 2016:
        continue
    rows.append({'title': title, 'total_citations': int(cit_map.get(title, 0))})

out_df = pd.DataFrame(rows)
if not out_df.empty:
    out_df = out_df.sort_values(['total_citations','title'], ascending=[False, True])
result = out_df.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_8AQzsnVK3pjf8qv96fVixUDd': 'file_storage/call_8AQzsnVK3pjf8qv96fVixUDd.json', 'var_call_Gcy9OwZ4BPgbXR3BKg8KmU3S': 'file_storage/call_Gcy9OwZ4BPgbXR3BKg8KmU3S.json'}

exec(code, env_args)
