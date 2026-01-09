code = """import json, re, pandas as pd

# load reviews
p = var_call_kxgpBMgwGgLMPeOzGsPyeYmA
with open(p, 'r', encoding='utf-8') as f:
    reviews = json.load(f)
dfr = pd.DataFrame(reviews)
dfr['rating'] = pd.to_numeric(dfr['rating'], errors='coerce')
dfr = dfr.dropna(subset=['purchase_id','rating'])

# load books details
p2 = var_call_tR5CDTXu99mxZFnMIBKFlqf1
with open(p2, 'r', encoding='utf-8') as f:
    books = json.load(f)
dfb = pd.DataFrame(books)
dfb = dfb.dropna(subset=['book_id','details'])

# extract publication year from details
pat = re.compile(r'\b(?:released on|on)\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b|\b(?:released|published)\s+(?:on\s+)?(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b|\b(?:first edition of this book was released on)\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b')

def get_year(s):
    if not isinstance(s,str):
        return None
    m = re.search(r'\b(19\d{2}|20\d{2})\b', s)
    if not m:
        return None
    y = int(m.group(1))
    if y < 1800 or y > 2026:
        return None
    return y

dfb['year'] = dfb['details'].map(get_year)
dfb = dfb.dropna(subset=['year'])
dfb['year'] = dfb['year'].astype(int)
dfb['decade_start'] = (dfb['year']//10)*10

# fuzzy join purchase_id_<n> to bookid_<n>
# extract numeric suffix

def suffix_num(x, prefix):
    if not isinstance(x,str):
        return None
    m = re.search(r'(\d+)$', x)
    return int(m.group(1)) if m else None

dfr['num'] = dfr['purchase_id'].map(lambda x: suffix_num(x,'purchaseid_'))
dfb['num'] = dfb['book_id'].map(lambda x: suffix_num(x,'bookid_'))

df = dfr.merge(dfb[['num','decade_start']], on='num', how='inner')

# restrict to books that have been rated (distinct books)
# compute per decade: avg rating across all reviews, and distinct books count
agg = df.groupby('decade_start').agg(avg_rating=('rating','mean'), distinct_books=('num', pd.Series.nunique))
agg = agg[agg['distinct_books'] >= 10]
if agg.empty:
    out = None
else:
    best = agg.sort_values(['avg_rating','distinct_books'], ascending=[False, False]).head(1).reset_index()
    decade = int(best.loc[0,'decade_start'])
    out = f"{decade}s"

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_tR5CDTXu99mxZFnMIBKFlqf1': 'file_storage/call_tR5CDTXu99mxZFnMIBKFlqf1.json', 'var_call_VtnvHka928viImULzNKmIC3d': ['review'], 'var_call_kxgpBMgwGgLMPeOzGsPyeYmA': 'file_storage/call_kxgpBMgwGgLMPeOzGsPyeYmA.json'}

exec(code, env_args)
