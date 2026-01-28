code = """import json, re, pandas as pd

books_src = var_call_UhDxoTRC19dsQohfefHP8FDf
with open(books_src, 'r', encoding='utf-8') as f:
    books = json.load(f)

rev_src = var_call_T3DIgRz8rKqUzNFvaFIj51I7
with open(rev_src, 'r', encoding='utf-8') as f:
    revs = json.load(f)

bdf = pd.DataFrame(books)
rdf = pd.DataFrame(revs)

pat_year = re.compile(r'\b(18|19|20)\d{2}\b')

def extract_year(s):
    if not isinstance(s, str):
        return None
    # try month day year patterns (with optional comma)
    m = re.search(r'\b(?:on|released on|published on|publication date[:]?|released)\s+[A-Za-z]+\s+\d{1,2},?\s+((18|19|20)\d{2})\b', s, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    m = pat_year.search(s)
    if m:
        return int(m.group(0))
    return None

bdf['year'] = bdf['details'].map(extract_year)
bdf = bdf.dropna(subset=['year'])

rdf['book_id'] = rdf['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
rdf = rdf.dropna(subset=['rating','book_id'])

j = rdf.merge(bdf[['book_id','year']], on='book_id', how='inner')

j['decade'] = (j['year']//10)*10

agg = j.groupby('decade').agg(avg_rating=('rating','mean'), distinct_books=('book_id', pd.Series.nunique)).reset_index()
agg_f = agg[agg['distinct_books']>=10].sort_values(['avg_rating','distinct_books'], ascending=[False, False])

out = None
if not agg_f.empty:
    top = agg_f.iloc[0]
    out = f"{int(top['decade'])}s"

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Q8NEqPTtlcm9biChevom1oDq': 'file_storage/call_Q8NEqPTtlcm9biChevom1oDq.json', 'var_call_ZDcER239fsRZwjy6NrSwbU7O': ['review'], 'var_call_T3DIgRz8rKqUzNFvaFIj51I7': 'file_storage/call_T3DIgRz8rKqUzNFvaFIj51I7.json', 'var_call_zdzvT5FAlrJdQDswSRrIUZ1f': {'decade': None, 'avg_rating': None, 'distinct_books': 0}, 'var_call_UhDxoTRC19dsQohfefHP8FDf': 'file_storage/call_UhDxoTRC19dsQohfefHP8FDf.json'}

exec(code, env_args)
