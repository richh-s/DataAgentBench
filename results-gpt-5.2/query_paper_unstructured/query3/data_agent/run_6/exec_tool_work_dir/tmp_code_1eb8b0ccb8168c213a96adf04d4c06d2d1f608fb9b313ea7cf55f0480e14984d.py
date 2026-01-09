code = """import json, re
import pandas as pd

md = var_call_EDcGVBgTMMuXSnOwHmNgY5Aw
if isinstance(md, str):
    with open(md, 'r', encoding='utf-8') as f:
        md = json.load(f)

cit = var_call_EgkA3sjpolGOy0GMEUN2oiBN
if isinstance(cit, str):
    with open(cit, 'r', encoding='utf-8') as f:
        cit = json.load(f)

year_re = re.compile(r'\\b(19\\d{2}|20\\d{2})\\b')

def extract_year(text):
    m = re.search(r'Copyright\\s*(?:©|\\(c\\))?\\s*(19\\d{2}|20\\d{2})', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    m = re.search(r'\\b(?:CHI|CSCW|UBICOMP|UbiComp|DIS|IUI|WWW|OzCHI|TEI|AH|PervasiveHealth)\\b[^\\n]{0,40}\\b(19\\d{2}|20\\d{2})\\b', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    years = [int(y) for y in year_re.findall(text)]
    years = [y for y in years if 1990 <= y <= 2026]
    return min(years) if years else None

def is_empirical(text):
    t = (text or '').lower()
    keys = ['we conducted','we ran','we performed','we interviewed','we survey','we surveyed','we carried out','user study','field study','lab study','experiment','participants']
    return any(k in t for k in keys)

rows = []
for d in md:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    year = extract_year(text)
    if year is None or year <= 2016:
        continue
    if not is_empirical(text):
        continue
    rows.append({'title': title, 'year': year})

papers = pd.DataFrame(rows).drop_duplicates(subset=['title'])

citedf = pd.DataFrame(cit)
if not citedf.empty:
    citedf['citation_count'] = pd.to_numeric(citedf['citation_count'], errors='coerce').fillna(0).astype(int)
    tot = citedf.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})
else:
    tot = pd.DataFrame(columns=['title','total_citations'])

res = papers.merge(tot, on='title', how='left')
res['total_citations'] = res['total_citations'].fillna(0).astype(int)
res = res.sort_values(['total_citations','title'], ascending=[False, True])

out = res[['title','total_citations']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_EDcGVBgTMMuXSnOwHmNgY5Aw': 'file_storage/call_EDcGVBgTMMuXSnOwHmNgY5Aw.json', 'var_call_EgkA3sjpolGOy0GMEUN2oiBN': 'file_storage/call_EgkA3sjpolGOy0GMEUN2oiBN.json'}

exec(code, env_args)
