code = """import json, re, pandas as pd

# Load reviews
path_reviews = var_call_80ZsjY42fMAZdgRbAQ154Y7D
with open(path_reviews, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

df_r = pd.DataFrame(reviews)
df_r = df_r.dropna(subset=['purchase_id','rating']).copy()
df_r['purchase_id'] = df_r['purchase_id'].astype(str)
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
df_r = df_r.dropna(subset=['rating'])

# Load books details
path_books = var_call_BVv1FP74Wew6YrfJd7WwIYdE
with open(path_books, 'r', encoding='utf-8') as f:
    books = json.load(f)

df_b = pd.DataFrame(books)
df_b = df_b.dropna(subset=['book_id','details']).copy()
df_b['book_id'] = df_b['book_id'].astype(str)

def extract_year(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'\b(19\d{2}|20\d{2})\b', s)
    if not m:
        return None
    y = int(m.group(1))
    if 1400 <= y <= 2100:
        return y
    return None

df_b['pub_year'] = df_b['details'].map(extract_year)
df_b = df_b.dropna(subset=['pub_year']).copy()
df_b['pub_year'] = df_b['pub_year'].astype(int)
df_b['decade'] = (df_b['pub_year'] // 10) * 10

# Join exact purchase_id -> book_id
merged = df_r.merge(df_b[['book_id','decade']], left_on='purchase_id', right_on='book_id', how='inner')

# Count distinct books per decade and avg rating across all reviews
agg = merged.groupby('decade').agg(
    distinct_books=('book_id','nunique'),
    avg_rating=('rating','mean')
).reset_index()

eligible = agg[agg['distinct_books'] >= 10].copy()
if eligible.empty:
    result = None
else:
    top = eligible.sort_values(['avg_rating','distinct_books','decade'], ascending=[False, False, True]).iloc[0]
    decade_str = f"{int(top['decade'])}s"
    result = decade_str

print('__RESULT__:')
print(json.dumps({'decade': result}))"""

env_args = {'var_call_OYOTDM5ZKUel8WEjRSRoEYUa': ['review'], 'var_call_mlItZdRoYBnuONRLD8QWNXm9': ['books_info'], 'var_call_80ZsjY42fMAZdgRbAQ154Y7D': 'file_storage/call_80ZsjY42fMAZdgRbAQ154Y7D.json', 'var_call_BVv1FP74Wew6YrfJd7WwIYdE': 'file_storage/call_BVv1FP74Wew6YrfJd7WwIYdE.json'}

exec(code, env_args)
