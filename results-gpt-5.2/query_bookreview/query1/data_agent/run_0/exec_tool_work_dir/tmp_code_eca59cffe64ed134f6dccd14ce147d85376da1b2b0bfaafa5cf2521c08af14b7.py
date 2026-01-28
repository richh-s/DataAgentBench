code = """import json, re, pandas as pd

# load reviews
path = var_call_rFMibxSq3hBz5fT8TkrLEynf
with open(path, 'r') as f:
    reviews = json.load(f)
rev = pd.DataFrame(reviews)
rev['rating'] = pd.to_numeric(rev['rating'], errors='coerce')
rev = rev.dropna(subset=['purchase_id','rating'])

# load books
pathb = var_call_SYMxhsmJcvQ2ZfX5vBbmtCng
with open(pathb, 'r') as f:
    books = json.load(f)
bk = pd.DataFrame(books)

# fuzzy join: purchaseid_123 -> bookid_123
rev['num'] = rev['purchase_id'].astype(str).str.extract(r'(\d+)')
bk['num'] = bk['book_id'].astype(str).str.extract(r'(\d+)')

# extract publication year from details
pat = re.compile(r'\b(19\d{2}|20\d{2})\b')

def get_year(s):
    if s is None:
        return None
    m = pat.findall(str(s))
    if not m:
        return None
    years = [int(x) for x in m]
    # choose plausible publication year: smallest year found
    return min(years)

bk['pub_year'] = bk['details'].apply(get_year)

# join and compute decade stats
m = rev.merge(bk[['num','pub_year']], on='num', how='inner')
m = m.dropna(subset=['pub_year'])
m['pub_year'] = m['pub_year'].astype(int)
m['decade'] = (m['pub_year']//10)*10

# only decades with at least 10 distinct books rated
agg = m.groupby('decade').agg(avg_rating=('rating','mean'), distinct_books=('num','nunique'))
agg = agg[agg['distinct_books']>=10].sort_values('avg_rating', ascending=False)
if agg.empty:
    out = None
else:
    best_decade = int(agg.index[0])
    out = f"{best_decade}s"

print('__RESULT__:')
print(json.dumps({'decade': out}))"""

env_args = {'var_call_I5tgTUm44kQTDK1CNBsPkReq': [{'book_id': 'bookid_53', 'details': 'This book, published by Frank Amato Publications on January 1, 1997, is written in English and features a spiral binding with a total of 31 pages. It has an ISBN-10 number of 1571880879 and an ISBN-13 number of 978-1571880871. The item weighs 3.2 ounces and has dimensions of 5.5 x 0.25 x 8.75 inches.'}, {'book_id': 'bookid_54', 'details': 'This book, published by Dover Publications on August 1, 2006, is written in English and is suitable for readers aged 8 to 9 years. It has an ISBN-10 of 0486457117 and an ISBN-13 of 978-0486457116. The book weighs 1.01 pounds and has dimensions of 5.25 x 1.5 x 8.5 inches.'}], 'var_call_brmxbsPCdF6OoMIsr9bbsJ3b': ['review'], 'var_call_rFMibxSq3hBz5fT8TkrLEynf': 'file_storage/call_rFMibxSq3hBz5fT8TkrLEynf.json', 'var_call_SYMxhsmJcvQ2ZfX5vBbmtCng': 'file_storage/call_SYMxhsmJcvQ2ZfX5vBbmtCng.json'}

exec(code, env_args)
