code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

books = load_records(var_call_bI9Q294bak9ak7apqvZONiKS)
reviews = load_records(var_call_e9DyEWiH6hw0IEZyWFFYVICh)

# extract 4-digit year from details (prefer explicit month day year patterns, but any 19xx/20xx)
year_re = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_year(details):
    if not details:
        return None
    ys = year_re.findall(details)
    if not ys:
        return None
    # choose the last year mentioned (often publication date year)
    return int(ys[-1])

book_year = []
for r in books:
    y = extract_year(r.get('details'))
    if y is not None:
        book_year.append({'purchase_id': r.get('book_id'), 'year': y})

bdf = pd.DataFrame(book_year).dropna()
# keep plausible years
bdf = bdf[(bdf['year']>=1500) & (bdf['year']<=2026)].drop_duplicates('purchase_id')

rdf = pd.DataFrame(reviews)
# coerce rating to float
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
rdf = rdf.dropna(subset=['purchase_id','rating'])

# join on exact id match (purchase_id equals book_id)
merged = rdf.merge(bdf, on='purchase_id', how='inner')
merged['decade_start'] = (merged['year']//10)*10
merged['decade'] = merged['decade_start'].astype(int).astype(str) + 's'

# for each decade, require at least 10 distinct books that have been rated
# distinct books = distinct purchase_id among merged
agg = merged.groupby('decade').agg(
    avg_rating=('rating','mean'),
    distinct_books=('purchase_id','nunique')
).reset_index()
agg = agg[agg['distinct_books']>=10]
if len(agg)==0:
    best = None
else:
    best = agg.sort_values(['avg_rating','distinct_books'], ascending=[False, False]).iloc[0]['decade']

print('__RESULT__:')
print(json.dumps({'decade': best, 'table': agg.sort_values('avg_rating', ascending=False).to_dict(orient='records')[:20]}))"""

env_args = {'var_call_jMkFlOuc59m05cKrFcBdHNzh': 'file_storage/call_jMkFlOuc59m05cKrFcBdHNzh.json', 'var_call_bI9Q294bak9ak7apqvZONiKS': 'file_storage/call_bI9Q294bak9ak7apqvZONiKS.json', 'var_call_3DuR13sc2CwOcoAXrRhoqU4p': ['review'], 'var_call_e9DyEWiH6hw0IEZyWFFYVICh': 'file_storage/call_e9DyEWiH6hw0IEZyWFFYVICh.json'}

exec(code, env_args)
