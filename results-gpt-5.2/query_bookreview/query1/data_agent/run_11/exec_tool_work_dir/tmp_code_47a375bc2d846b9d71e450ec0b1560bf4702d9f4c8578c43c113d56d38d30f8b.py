code = """import json, re, pandas as pd

# load reviews
path_rev = var_call_IQzup4JjmWTwLdGZNqKg3M0d
with open(path_rev, 'r') as f:
    reviews = json.load(f)
df_r = pd.DataFrame(reviews)
if df_r.empty:
    out = {"error":"no reviews"}
else:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
    df_r = df_r.dropna(subset=['purchase_id','rating'])

# load books details
path_books = var_call_ZGY5xwAz1kt9LDymFadPxdV6
with open(path_books, 'r') as f:
    books = json.load(f)
df_b = pd.DataFrame(books)

def extract_year(s):
    if s is None:
        return None
    # prefer explicit 'released on <Month> <d>, <yyyy>' or 'on <Month> <d>, <yyyy>'
    m = re.search(r'\b(19\d{2}|20\d{2})\b', str(s))
    if not m:
        return None
    return int(m.group(1))

df_b['year'] = df_b['details'].map(extract_year)
# join by numeric suffix mapping purchaseid_X -> bookid_X

def get_suffix(x):
    m = re.search(r'_(\d+)$', str(x))
    return m.group(1) if m else None

df_r['suffix'] = df_r['purchase_id'].map(get_suffix)
df_b['suffix'] = df_b['book_id'].map(get_suffix)

# inner join
j = df_r.merge(df_b[['book_id','suffix','year']], on='suffix', how='inner')

# rated books with known year
oj = j.dropna(subset=['year'])
oj['year'] = oj['year'].astype(int)
oj['decade_start'] = (oj['year']//10)*10
oj['decade'] = oj['decade_start'].astype(str) + 's'

# compute distinct books per decade (distinct book_id) that have been rated
books_per_decade = oj.groupby('decade')['book_id'].nunique()
valid_decades = books_per_decade[books_per_decade >= 10].index

oj_valid = oj[oj['decade'].isin(valid_decades)]

avg_by_decade = oj_valid.groupby('decade')['rating'].mean().sort_values(ascending=False)
if avg_by_decade.empty:
    out = {"error":"no decade with at least 10 distinct rated books"}
else:
    top_decade = avg_by_decade.index[0]
    out = {"decade": top_decade}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ZGY5xwAz1kt9LDymFadPxdV6': 'file_storage/call_ZGY5xwAz1kt9LDymFadPxdV6.json', 'var_call_TprPfm8FTHYq6g5ZgF5AoWUv': ['review'], 'var_call_IQzup4JjmWTwLdGZNqKg3M0d': 'file_storage/call_IQzup4JjmWTwLdGZNqKg3M0d.json'}

exec(code, env_args)
