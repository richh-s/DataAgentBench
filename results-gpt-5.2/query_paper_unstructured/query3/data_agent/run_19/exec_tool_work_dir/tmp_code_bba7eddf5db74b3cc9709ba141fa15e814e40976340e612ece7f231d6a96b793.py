code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

paper_docs = load_records(var_call_sOIW3ikbUyrK3nh2HD04zUJF)
cites = load_records(var_call_TKBAZjAKqOeT0XvtrB583Ksm)

def extract_year(text):
    # look for 4-digit year 2000-2026, prefer first occurrence near top
    head = text[:4000]
    years = re.findall(r'\b(20\d{2})\b', head)
    if years:
        return int(years[0])
    years = re.findall(r'\b(19\d{2}|20\d{2})\b', text)
    if years:
        return int(years[0])
    return None

def has_empirical(text):
    # heuristic: match 'empirical' as word anywhere
    return re.search(r'\bempirical\b', text, flags=re.IGNORECASE) is not None

rows=[]
for d in paper_docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    year = extract_year(text)
    empirical = has_empirical(text)
    rows.append({'title': title, 'year': year, 'empirical': empirical})

pdf = pd.DataFrame(rows)
pdf = pdf[(pdf['empirical']==True) & (pdf['year'].notna()) & (pdf['year']>2016)]

cdf = pd.DataFrame(cites)
# citation_count may be str
cdf['citation_count'] = pd.to_numeric(cdf['citation_count'], errors='coerce').fillna(0).astype(int)

tag = cdf.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})

out = pd.merge(pdf[['title']], tag, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out.sort_values(['total_citations','title'], ascending=[False, True])
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_sOIW3ikbUyrK3nh2HD04zUJF': 'file_storage/call_sOIW3ikbUyrK3nh2HD04zUJF.json', 'var_call_TKBAZjAKqOeT0XvtrB583Ksm': 'file_storage/call_TKBAZjAKqOeT0XvtrB583Ksm.json'}

exec(code, env_args)
