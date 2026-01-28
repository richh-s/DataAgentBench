code = """import json, re, pandas as pd

# load reviews
path_reviews = var_call_XbQbVxSFohL8xGhailGYgakG
with open(path_reviews, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

df_r = pd.DataFrame(reviews)
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
df_r = df_r.dropna(subset=['purchase_id','rating'])

# load books details
path_books = var_call_hb79lcbUdFKOCAqHDyhp92b0
with open(path_books, 'r', encoding='utf-8') as f:
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
    if y < 1500 or y > 2026:
        return None
    return y

df_b['year'] = df_b['details'].apply(extract_year)
df_b = df_b.dropna(subset=['book_id','year'])
df_b['year'] = df_b['year'].astype(int)

# fuzzy join by numeric suffix id (purchaseid_186 -> bookid_186)
def suffix_num(x):
    m = re.search(r'(\d+)$', str(x))
    return int(m.group(1)) if m else None

df_r['id_num'] = df_r['purchase_id'].apply(suffix_num)
df_b['id_num'] = df_b['book_id'].apply(suffix_num)

joined = df_r.merge(df_b[['id_num','year']], on='id_num', how='inner')

# compute per-book avg rating (distinct books that have been rated)
per_book = joined.groupby(['id_num','year'], as_index=False).agg(avg_rating=('rating','mean'))
per_book['decade_start'] = (per_book['year']//10)*10
per_book['decade'] = per_book['decade_start'].astype(str) + 's'

# decade stats with at least 10 distinct books
stats = per_book.groupby('decade', as_index=False).agg(
    distinct_books=('id_num','nunique'),
    avg_rating=('avg_rating','mean')
)
stats = stats[stats['distinct_books']>=10]

if stats.empty:
    result = {"decade": None, "avg_rating": None, "distinct_books": 0}
else:
    top = stats.sort_values(['avg_rating','distinct_books'], ascending=[False, False]).iloc[0]
    result = {"decade": str(top['decade']), "avg_rating": float(top['avg_rating']), "distinct_books": int(top['distinct_books'])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_hb79lcbUdFKOCAqHDyhp92b0': 'file_storage/call_hb79lcbUdFKOCAqHDyhp92b0.json', 'var_call_pGSgxYOUMnP7tyRjvkwGrPxg': ['review'], 'var_call_XbQbVxSFohL8xGhailGYgakG': 'file_storage/call_XbQbVxSFohL8xGhailGYgakG.json'}

exec(code, env_args)
