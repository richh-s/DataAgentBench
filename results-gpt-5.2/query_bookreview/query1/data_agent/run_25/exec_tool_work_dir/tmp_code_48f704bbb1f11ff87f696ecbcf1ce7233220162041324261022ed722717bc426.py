code = """import json, re, pandas as pd

# Load reviews
path_reviews = var_call_YevUi10fc17HFUqBhZOsKBtL
with open(path_reviews, 'r') as f:
    reviews = json.load(f)

df_r = pd.DataFrame(reviews)
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
df_r = df_r.dropna(subset=['purchase_id','rating'])

# Load books details
path_books = var_call_Fk9Amuu0srWMjgASHoTyMiiq
with open(path_books, 'r') as f:
    books = json.load(f)

df_b = pd.DataFrame(books)

def extract_year(details):
    if details is None:
        return None
    s = str(details)
    m = re.search(r'\b(19\d{2}|20\d{2})\b', s)
    if not m:
        return None
    y = int(m.group(1))
    if 1800 <= y <= 2026:
        return y
    return None

df_b['year'] = df_b['details'].apply(extract_year)
df_b = df_b.dropna(subset=['book_id','year'])
df_b['year'] = df_b['year'].astype(int)

# Fuzzy join purchaseid_<n> -> bookid_<n>
# convert purchase_id to corresponding book_id when numeric suffix exists
suffix = df_r['purchase_id'].astype(str).str.extract(r'_(\d+)$')[0]
df_r = df_r.assign(_num=pd.to_numeric(suffix, errors='coerce'))
df_r = df_r.dropna(subset=['_num'])
df_r['_num'] = df_r['_num'].astype(int)
df_r['book_id'] = 'bookid_' + df_r['_num'].astype(str)

# Merge and aggregate
m = df_r.merge(df_b[['book_id','year']], on='book_id', how='inner')
# rated distinct books per decade
m['decade_start'] = (m['year'] // 10) * 10
m['decade'] = m['decade_start'].astype(str) + 's'

# compute average rating across all reviews in decade; require >=10 distinct books rated
agg = m.groupby('decade').agg(
    avg_rating=('rating','mean'),
    distinct_books=('book_id', pd.Series.nunique),
    review_count=('rating','size')
).reset_index()

eligible = agg[agg['distinct_books'] >= 10]
if eligible.empty:
    out = None
else:
    best = eligible.sort_values(['avg_rating','distinct_books','review_count'], ascending=[False, False, False]).iloc[0]
    out = {'decade': best['decade'], 'avg_rating': float(best['avg_rating']), 'distinct_books': int(best['distinct_books']), 'review_count': int(best['review_count'])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Fk9Amuu0srWMjgASHoTyMiiq': 'file_storage/call_Fk9Amuu0srWMjgASHoTyMiiq.json', 'var_call_l3wlHXYBurXGhV4Vs7OJ4AGW': ['review'], 'var_call_YevUi10fc17HFUqBhZOsKBtL': 'file_storage/call_YevUi10fc17HFUqBhZOsKBtL.json'}

exec(code, env_args)
