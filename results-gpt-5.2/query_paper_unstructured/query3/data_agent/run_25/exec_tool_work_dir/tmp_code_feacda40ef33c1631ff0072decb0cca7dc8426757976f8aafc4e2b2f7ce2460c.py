code = """import json, re, pandas as pd

cit_path = var_call_U0lcnZKHih4sfzLUna4TquRB
with open(cit_path,'r',encoding='utf-8') as f:
    cit = json.load(f)

dfc = pd.DataFrame(cit)
if not dfc.empty:
    dfc['citation_count'] = pd.to_numeric(dfc['citation_count'], errors='coerce').fillna(0).astype(int)

docs_path = var_call_Je3SoVz4YZtloNvEzc1vUPot
with open(docs_path,'r',encoding='utf-8') as f:
    docs = json.load(f)

def title_from_filename(fn):
    return re.sub(r'\.txt$','',fn)

def extract_year(text):
    years = [int(y) for y in re.findall(r'\b(19\d{2}|20\d{2})\b', text or '')]
    years = [y for y in years if 1990 <= y <= 2026]
    if not years:
        return None
    from collections import Counter
    c = Counter(years)
    yr = sorted(c.items(), key=lambda kv:(-kv[1], -kv[0]))[0][0]
    return yr

rows=[]
for d in docs:
    t = title_from_filename(d.get('filename','') or '')
    year = extract_year(d.get('text',''))
    rows.append({'title': t, 'year': year})

dfd = pd.DataFrame(rows).drop_duplicates(subset=['title'])

if dfd.empty:
    res=[]
else:
    dfd['year_num'] = pd.to_numeric(dfd['year'], errors='coerce')
    post = dfd[dfd['year_num'] > 2016][['title']].copy()
    merged = post.merge(dfc, on='title', how='left')
    merged['citation_count'] = merged['citation_count'].fillna(0).astype(int)
    agg = merged.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citation_count'})
    res = agg.sort_values('total_citation_count', ascending=False).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_ULK3sMfRoEwsNpJE1cmbWOF4': 'file_storage/call_ULK3sMfRoEwsNpJE1cmbWOF4.json', 'var_call_U0lcnZKHih4sfzLUna4TquRB': 'file_storage/call_U0lcnZKHih4sfzLUna4TquRB.json', 'var_call_Je3SoVz4YZtloNvEzc1vUPot': 'file_storage/call_Je3SoVz4YZtloNvEzc1vUPot.json'}

exec(code, env_args)
