code = """import json, re, pandas as pd

def load_var(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

books = load_var(var_call_t7F2UOjrHLEiZQbpcWKguFKB)
reviews = load_var(var_call_euBjiFMaGwZFPQxT9Kw30JKZ)

dfb = pd.DataFrame(books)
dfr = pd.DataFrame(reviews)

# extract a 4-digit publication year from details
pat = re.compile(r'\b(18\d{2}|19\d{2}|20\d{2})\b')

def extract_year(s):
    if s is None:
        return None
    m = pat.search(str(s))
    if not m:
        return None
    y = int(m.group(1))
    if 1800 <= y <= 2026:
        return y
    return None

dfb['year'] = dfb['details'].map(extract_year)
dfb = dfb.dropna(subset=['year'])
dfb['year'] = dfb['year'].astype(int)

# normalize ids for fuzzy join purchaseid_XX <-> bookid_XX
idnum_pat = re.compile(r'(\d+)')

def id_num(x):
    if x is None:
        return None
    m = idnum_pat.search(str(x))
    return int(m.group(1)) if m else None

dfb['id_num'] = dfb['book_id'].map(id_num)
dfr['id_num'] = dfr['purchase_id'].map(id_num)

# ratings to numeric
r = pd.to_numeric(dfr['rating'], errors='coerce')
dfr = dfr.assign(rating_num=r).dropna(subset=['rating_num','id_num'])
dfr['rating_num'] = dfr['rating_num'].astype(float)
dfr['id_num'] = dfr['id_num'].astype(int)

# join and compute decade stats
joined = pd.merge(dfr[['id_num','rating_num']], dfb[['id_num','year']], on='id_num', how='inner')
joined['decade'] = (joined['year']//10)*10

# only decades with >=10 distinct books rated
# book count distinct id_num within decade among joined
agg = joined.groupby('decade').agg(
    avg_rating=('rating_num','mean'),
    distinct_books=('id_num', pd.Series.nunique),
    n_reviews=('rating_num','size')
).reset_index()

eligible = agg[agg['distinct_books']>=10].copy()
if eligible.empty:
    result = None
else:
    top = eligible.sort_values(['avg_rating','distinct_books','n_reviews'], ascending=[False,False,False]).iloc[0]
    decade_label = f"{int(top['decade'])}s"
    result = {'decade': decade_label, 'avg_rating': float(top['avg_rating']), 'distinct_books': int(top['distinct_books']), 'n_reviews': int(top['n_reviews'])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_t7F2UOjrHLEiZQbpcWKguFKB': 'file_storage/call_t7F2UOjrHLEiZQbpcWKguFKB.json', 'var_call_5uFYE7IkuuEM5s32Tv4hZP4u': ['review'], 'var_call_euBjiFMaGwZFPQxT9Kw30JKZ': 'file_storage/call_euBjiFMaGwZFPQxT9Kw30JKZ.json'}

exec(code, env_args)
