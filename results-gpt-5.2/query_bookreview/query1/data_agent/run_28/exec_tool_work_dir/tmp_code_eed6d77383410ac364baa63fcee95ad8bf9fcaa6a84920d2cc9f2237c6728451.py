code = """import json, re, pandas as pd

# load reviews
p = var_call_ohSVdJnKHzzi87qXbMjvdxnj
with open(p, 'r', encoding='utf-8') as f:
    reviews = json.load(f)
df_r = pd.DataFrame(reviews)
# ensure numeric rating
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
df_r = df_r.dropna(subset=['purchase_id','rating'])
# distinct rated books
rated_books = set(df_r['purchase_id'].astype(str).unique())

# load books details
p2 = var_call_SgLJPPR0zEfqMDBTw1dZ3gwF
with open(p2, 'r', encoding='utf-8') as f:
    books = json.load(f)
df_b = pd.DataFrame(books)
df_b = df_b[df_b['book_id'].astype(str).isin(rated_books)].copy()

# extract publication year from details
pat = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_year(s):
    if not isinstance(s, str):
        return None
    m = pat.findall(s)
    if not m:
        return None
    # choose earliest plausible year as publication year
    years = [int(x) for x in m]
    # filter reasonable range
    years = [y for y in years if 1500 <= y <= 2026]
    if not years:
        return None
    return min(years)

df_b['pub_year'] = df_b['details'].map(extract_year)
df_b = df_b.dropna(subset=['pub_year'])
df_b['pub_year'] = df_b['pub_year'].astype(int)
df_b['decade_start'] = (df_b['pub_year']//10)*10

# average rating per book (distinct books)
df_book_avg = df_r.groupby('purchase_id', as_index=False)['rating'].mean().rename(columns={'purchase_id':'book_id','rating':'book_avg_rating'})

# join with decade
df = pd.merge(df_book_avg, df_b[['book_id','decade_start']].drop_duplicates('book_id'), on='book_id', how='inner')

# compute per decade: avg of book avg ratings and count distinct books
agg = df.groupby('decade_start').agg(distinct_books=('book_id','nunique'), avg_rating=('book_avg_rating','mean')).reset_index()
agg = agg[agg['distinct_books']>=10]
if agg.empty:
    out = None
else:
    best = agg.sort_values(['avg_rating','distinct_books','decade_start'], ascending=[False,False,True]).iloc[0]
    out = f"{int(best['decade_start'])}s"

print('__RESULT__:')
print(json.dumps({'decade': out}))"""

env_args = {'var_call_SgLJPPR0zEfqMDBTw1dZ3gwF': 'file_storage/call_SgLJPPR0zEfqMDBTw1dZ3gwF.json', 'var_call_4DHWpswiVG4kBe85N7SCv0xI': ['review'], 'var_call_ohSVdJnKHzzi87qXbMjvdxnj': 'file_storage/call_ohSVdJnKHzzi87qXbMjvdxnj.json'}

exec(code, env_args)
