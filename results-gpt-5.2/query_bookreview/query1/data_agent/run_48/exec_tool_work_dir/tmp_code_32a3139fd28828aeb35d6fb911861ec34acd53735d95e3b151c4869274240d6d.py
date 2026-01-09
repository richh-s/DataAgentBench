code = """import json, re, pandas as pd

# Load reviews
p = var_call_HprBMMht6NV6lhXPdykLBcKf
with open(p, 'r') as f:
    reviews = json.load(f)
dfr = pd.DataFrame(reviews)
dfr['rating'] = pd.to_numeric(dfr['rating'], errors='coerce')
dfr = dfr.dropna(subset=['purchase_id','rating'])

# Load books details
pb = var_call_So0ZyG1e2IsipAxjvITaW2nw
with open(pb, 'r') as f:
    books = json.load(f)
dfb = pd.DataFrame(books)
dfb = dfb.dropna(subset=['book_id','details'])

# Extract 4-digit year from details
year_re = re.compile(r'\b(1[5-9]\d{2}|20\d{2})\b')

def extract_year(s):
    if not isinstance(s, str):
        return None
    m = year_re.search(s)
    if not m:
        return None
    y = int(m.group(1))
    if 1500 <= y <= 2026:
        return y
    return None

dfb['year'] = dfb['details'].map(extract_year)
dfb = dfb.dropna(subset=['year'])
dfb['year'] = dfb['year'].astype(int)
dfb['decade'] = (dfb['year']//10)*10

# Fuzzy-ish join: purchaseid_123 <-> bookid_123 by numeric suffix
suffix_re = re.compile(r'(\d+)$')

def suffix(x):
    if not isinstance(x, str):
        return None
    m = suffix_re.search(x)
    return m.group(1) if m else None

dfr['sid'] = dfr['purchase_id'].map(suffix)
dfb['sid'] = dfb['book_id'].map(suffix)

# Only rated books: distinct book entity (sid) with >=1 rating
# Join on sid
joined = dfr.merge(dfb[['sid','decade']], on='sid', how='inner')

# For decades with at least 10 distinct books that have been rated
# compute avg rating across all reviews in that decade
# and count distinct books (sid)
agg = joined.groupby('decade').agg(
    avg_rating=('rating','mean'),
    distinct_books=('sid', pd.Series.nunique),
    n_reviews=('rating','size')
).reset_index()
agg10 = agg[agg['distinct_books']>=10].copy()
if agg10.empty:
    best = None
else:
    best = agg10.sort_values(['avg_rating','distinct_books','n_reviews'], ascending=[False,False,False]).iloc[0]
    best = f"{int(best['decade'])}s"

print('__RESULT__:')
print(json.dumps({'best_decade': best}))"""

env_args = {'var_call_So0ZyG1e2IsipAxjvITaW2nw': 'file_storage/call_So0ZyG1e2IsipAxjvITaW2nw.json', 'var_call_aSYdc23lzvaRfmsKTJ53iD56': ['review'], 'var_call_HprBMMht6NV6lhXPdykLBcKf': 'file_storage/call_HprBMMht6NV6lhXPdykLBcKf.json'}

exec(code, env_args)
