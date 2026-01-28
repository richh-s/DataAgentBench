code = """import json, re, pandas as pd

# Load books details (from file path)
books_src = var_call_Q8NEqPTtlcm9biChevom1oDq
if isinstance(books_src, str):
    with open(books_src, 'r', encoding='utf-8') as f:
        books = json.load(f)
else:
    books = books_src

# Load reviews (from file path)
rev_src = var_call_T3DIgRz8rKqUzNFvaFIj51I7
if isinstance(rev_src, str):
    with open(rev_src, 'r', encoding='utf-8') as f:
        revs = json.load(f)
else:
    revs = rev_src

bdf = pd.DataFrame(books)
rdf = pd.DataFrame(revs)

# Parse a publication year from details text
pat_year = re.compile(r'\b(18|19|20)\d{2}\b')

def extract_year(s):
    if not isinstance(s, str):
        return None
    # Prefer explicit 'on <Month> <d>, <yyyy>' or 'on <Month> <d> <yyyy>'
    m = re.search(r'\bon\s+[A-Za-z]+\s+\d{1,2},?\s+((18|19|20)\d{2})\b', s)
    if m:
        return int(m.group(1))
    # Prefer 'released on ... <yyyy>'
    m = re.search(r'\breleased\s+on\s+[A-Za-z]+\s+\d{1,2},?\s+((18|19|20)\d{2})\b', s)
    if m:
        return int(m.group(1))
    # Otherwise take first reasonable year
    m = pat_year.search(s)
    if m:
        return int(m.group(0))
    return None

bdf['year'] = bdf['details'].map(extract_year)
bdf = bdf.dropna(subset=['year'])

# map purchaseid_X -> bookid_X as hinted
rdf['book_id'] = rdf['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
rdf = rdf.dropna(subset=['rating','book_id'])

# join
j = rdf.merge(bdf[['book_id','year']], on='book_id', how='inner')

j['decade'] = (j['year']//10)*10

# decades with at least 10 distinct rated books
agg = j.groupby('decade').agg(
    avg_rating=('rating','mean'),
    distinct_books=('book_id', pd.Series.nunique)
).reset_index()

agg_f = agg[agg['distinct_books']>=10].sort_values(['avg_rating','distinct_books'], ascending=[False, False])

if agg_f.empty:
    out = {"decade": None, "avg_rating": None, "distinct_books": 0}
else:
    top = agg_f.iloc[0]
    out = {"decade": f"{int(top['decade'])}s", "avg_rating": float(top['avg_rating']), "distinct_books": int(top['distinct_books'])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Q8NEqPTtlcm9biChevom1oDq': 'file_storage/call_Q8NEqPTtlcm9biChevom1oDq.json', 'var_call_ZDcER239fsRZwjy6NrSwbU7O': ['review'], 'var_call_T3DIgRz8rKqUzNFvaFIj51I7': 'file_storage/call_T3DIgRz8rKqUzNFvaFIj51I7.json'}

exec(code, env_args)
