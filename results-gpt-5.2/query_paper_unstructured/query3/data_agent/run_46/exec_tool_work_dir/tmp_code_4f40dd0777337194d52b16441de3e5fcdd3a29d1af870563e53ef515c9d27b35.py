code = """import json, re, pandas as pd

path = var_call_tceA0ijmJOUOkbKam3TWFmL6
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def extract_year(text):
    head = (text or '')[:2500]
    yrs = [int(y) for y in re.findall(r"\b(20\d{2})\b", head)]
    if yrs:
        from collections import Counter
        c = Counter(yrs)
        m = max(c.values())
        cand = [y for y,v in c.items() if v==m]
        return max(cand)
    return None

def has_empirical(text):
    return re.search(r"\bempirical\b", text or '', flags=re.IGNORECASE) is not None

rows=[]
for d in docs:
    title = d['filename'].rsplit('.txt',1)[0]
    text = d.get('text','') or ''
    if not has_empirical(text):
        continue
    year = extract_year(text)
    if year is None or year<=2016:
        continue
    rows.append({'title': title, 'year': year})

papers_df = pd.DataFrame(rows).drop_duplicates('title')

cit_path = var_call_KqWpDGKnYGXGtW0dbCqmSD8r
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

cit_df = pd.DataFrame(cit)
# normalize citation df columns
if not cit_df.empty:
    if 'title' not in cit_df.columns and 'Title' in cit_df.columns:
        cit_df = cit_df.rename(columns={'Title':'title'})
    cit_df['citation_count'] = pd.to_numeric(cit_df.get('citation_count'), errors='coerce').fillna(0).astype(int)
    tot = cit_df.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})
else:
    tot = pd.DataFrame(columns=['title','total_citations'])

out = papers_df.merge(tot, on='title', how='left') if not papers_df.empty else papers_df.assign(total_citations=[])
if not out.empty:
    out['total_citations'] = out['total_citations'].fillna(0).astype(int)
    out = out.sort_values(['total_citations','title'], ascending=[False, True])

result = (out[['title','total_citations']].to_dict('records') if not out.empty else [])
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_8i47lMSYBgdOkF2dYzuuZIpo': 'file_storage/call_8i47lMSYBgdOkF2dYzuuZIpo.json', 'var_call_KqWpDGKnYGXGtW0dbCqmSD8r': 'file_storage/call_KqWpDGKnYGXGtW0dbCqmSD8r.json', 'var_call_tceA0ijmJOUOkbKam3TWFmL6': 'file_storage/call_tceA0ijmJOUOkbKam3TWFmL6.json'}

exec(code, env_args)
