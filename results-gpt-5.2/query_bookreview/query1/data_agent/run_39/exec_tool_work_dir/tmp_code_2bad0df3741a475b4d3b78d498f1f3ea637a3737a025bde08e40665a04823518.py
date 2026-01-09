code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

books = load_records(var_call_vBEURZALKBXHI8jt5XGgwHZK)
reviews = load_records(var_call_nNOO6xF9tgjHIXW2YcB0sEsM)

# extract year from details
patterns = [
    re.compile(r'(?i)publication date\s*[:\-]?\s*([A-Za-z]+\s+\d{1,2},\s+)?(\d{4})'),
    re.compile(r'(?i)published\s+on\s+([A-Za-z]+\s+\d{1,2},\s+)?(\d{4})'),
    re.compile(r'(?i)released\s+on\s+([A-Za-z]+\s+\d{1,2},\s+)?(\d{4})'),
    re.compile(r'(?i)first\s+edition\s+(?:of\s+this\s+book\s+was\s+)?(?:released\s+on\s+)?([A-Za-z]+\s+\d{1,2},\s+)?(\d{4})'),
    re.compile(r'(?i)on\s+([A-Za-z]+\s+\d{1,2},\s+)?(\d{4})')
]

def extract_year(s):
    if not s:
        return None
    for p in patterns[:-1]:
        m = p.search(s)
        if m:
            return int(m.group(2))
    # fallback: any 4-digit year, prefer 1800-2026
    years = [int(y) for y in re.findall(r'(18\d{2}|19\d{2}|20\d{2})', s)]
    if not years:
        return None
    # prefer earliest plausible publication year mentioned
    return min(years)

book_year = []
for r in books:
    y = extract_year(r.get('details'))
    if y is not None:
        book_year.append({'book_id': r.get('book_id'), 'year': y})

bdf = pd.DataFrame(book_year).dropna()

rdf = pd.DataFrame(reviews)
# coerce rating
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
rdf = rdf.dropna(subset=['rating','purchase_id'])

# fuzzy join purchaseid_X <-> bookid_X by extracting numeric suffix
rdf['id_num'] = rdf['purchase_id'].astype(str).str.extract(r'(\d+)$')[0]
bdf['id_num'] = bdf['book_id'].astype(str).str.extract(r'(\d+)$')[0]

j = rdf.merge(bdf, on='id_num', how='inner')

# decade
j['decade_start'] = (j['year']//10)*10
j['decade'] = j['decade_start'].astype(int).astype(str) + 's'

# consider only decades with at least 10 distinct books that have been rated
# distinct books = distinct id_num within decade
agg = j.groupby('decade').agg(
    avg_rating=('rating','mean'),
    distinct_books=('id_num', pd.Series.nunique)
).reset_index()

eligible = agg[agg['distinct_books']>=10].copy()
if eligible.empty:
    result = None
else:
    best = eligible.sort_values(['avg_rating','distinct_books'], ascending=[False, False]).iloc[0]
    result = best['decade']

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_vBEURZALKBXHI8jt5XGgwHZK': 'file_storage/call_vBEURZALKBXHI8jt5XGgwHZK.json', 'var_call_SbLC5UlfUSFkaaaEoT85tPy9': ['review'], 'var_call_nNOO6xF9tgjHIXW2YcB0sEsM': 'file_storage/call_nNOO6xF9tgjHIXW2YcB0sEsM.json'}

exec(code, env_args)
