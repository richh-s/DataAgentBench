code = """import json, re, pandas as pd

# load books
books_src = var_call_WdvIQu2TzwIishyRCqjIAD05
if isinstance(books_src, str):
    with open(books_src, 'r') as f:
        books = json.load(f)
else:
    books = books_src

# load reviews
rev_src = var_call_guaAbct5I46myL51HlRJ9bVJ
if isinstance(rev_src, str):
    with open(rev_src, 'r') as f:
        reviews = json.load(f)
else:
    reviews = rev_src

bdf = pd.DataFrame(books)
rdf = pd.DataFrame(reviews)

# parse year from details
year_re = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_year(s):
    if not isinstance(s, str):
        return None
    # prefer phrases like released/published on
    m = re.search(r'(?:released on|published on|publication date|first edition on|reprint edition on|edition on)\s+[A-Za-z]+\s+\d{1,2},\s*((?:19|20)\d{2})', s, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    # next: any year
    m2 = year_re.search(s)
    if m2:
        return int(m2.group(1))
    return None

bdf['year'] = bdf['details'].apply(extract_year)
bdf = bdf.dropna(subset=['year']).copy()
bdf['year'] = bdf['year'].astype(int)

# map purchaseid_x -> bookid_x by shared numeric suffix
bdf['suffix'] = bdf['book_id'].astype(str).str.extract(r'(\d+)$')[0]
rdf['suffix'] = rdf['purchase_id'].astype(str).str.extract(r'(\d+)$')[0]

# numeric suffix join
m = rdf.merge(bdf[['suffix','book_id','year']], on='suffix', how='inner')

# ratings to float
m['rating'] = pd.to_numeric(m['rating'], errors='coerce')
m = m.dropna(subset=['rating'])

m['decade_start'] = (m['year']//10)*10
m['decade'] = m['decade_start'].astype(int).astype(str) + 's'

# decades with at least 10 distinct books that have been rated
agg = m.groupby('decade').agg(
    avg_rating=('rating','mean'),
    distinct_books=('book_id', pd.Series.nunique)
).reset_index()
agg = agg[agg['distinct_books']>=10].copy()

if agg.empty:
    ans = None
else:
    best = agg.sort_values(['avg_rating','distinct_books','decade'], ascending=[False,False,True]).iloc[0]
    ans = {'decade': best['decade'], 'average_rating': float(best['avg_rating']), 'distinct_books': int(best['distinct_books'])}

print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_WdvIQu2TzwIishyRCqjIAD05': 'file_storage/call_WdvIQu2TzwIishyRCqjIAD05.json', 'var_call_vEzFIbxwYqK3mbk0Mv9RRHSQ': ['review'], 'var_call_guaAbct5I46myL51HlRJ9bVJ': 'file_storage/call_guaAbct5I46myL51HlRJ9bVJ.json'}

exec(code, env_args)
