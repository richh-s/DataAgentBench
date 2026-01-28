code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

books = load_records(var_call_bI9Q294bak9ak7apqvZONiKS)
reviews = load_records(var_call_e9DyEWiH6hw0IEZyWFFYVICh)

year_re = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_year(details):
    if not details:
        return None
    ys = year_re.findall(details)
    if not ys:
        return None
    return int(ys[-1])

book_year = []
for r in books:
    bid = r.get('book_id')
    if not bid:
        continue
    y = extract_year(r.get('details'))
    if y is not None:
        book_year.append({'purchase_id': bid, 'year': y})

bdf = pd.DataFrame(book_year)
if not bdf.empty:
    bdf = bdf.dropna(subset=['purchase_id','year'])
    bdf = bdf[(bdf['year']>=1500) & (bdf['year']<=2026)].drop_duplicates('purchase_id')

rdf = pd.DataFrame(reviews)
rdf['rating'] = pd.to_numeric(rdf.get('rating'), errors='coerce')
rdf = rdf.dropna(subset=['purchase_id','rating'])

if bdf.empty:
    out = {'decade': None, 'error':'No publication years parsed from books details.'}
else:
    merged = rdf.merge(bdf, on='purchase_id', how='inner')
    if merged.empty:
        out = {'decade': None, 'error':'No matches between review purchase_id and book_id (exact join).'}
    else:
        merged['decade_start'] = (merged['year'].astype(int)//10)*10
        merged['decade'] = merged['decade_start'].astype(int).astype(str) + 's'
        agg = merged.groupby('decade').agg(avg_rating=('rating','mean'), distinct_books=('purchase_id','nunique')).reset_index()
        agg = agg[agg['distinct_books']>=10]
        if agg.empty:
            out = {'decade': None, 'error':'No decades with >=10 distinct rated books after join.', 'decade_stats': merged.groupby('decade').agg(avg_rating=('rating','mean'), distinct_books=('purchase_id','nunique')).reset_index().sort_values('distinct_books', ascending=False).head(20).to_dict(orient='records')}
        else:
            best_row = agg.sort_values(['avg_rating','distinct_books'], ascending=[False, False]).iloc[0]
            out = {'decade': best_row['decade'], 'avg_rating': float(best_row['avg_rating']), 'distinct_books': int(best_row['distinct_books'])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_jMkFlOuc59m05cKrFcBdHNzh': 'file_storage/call_jMkFlOuc59m05cKrFcBdHNzh.json', 'var_call_bI9Q294bak9ak7apqvZONiKS': 'file_storage/call_bI9Q294bak9ak7apqvZONiKS.json', 'var_call_3DuR13sc2CwOcoAXrRhoqU4p': ['review'], 'var_call_e9DyEWiH6hw0IEZyWFFYVICh': 'file_storage/call_e9DyEWiH6hw0IEZyWFFYVICh.json'}

exec(code, env_args)
