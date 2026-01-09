code = """import json, pandas as pd

# load reviews (2020+)
rev_src = var_call_gb5dIlMYUWNAEuqhH9sM5IHd
if isinstance(rev_src, str):
    with open(rev_src, 'r') as f:
        reviews = json.load(f)
else:
    reviews = rev_src

# load books
books_src = var_call_rCo5BaBGx3dT0h1Fp0IICMON
if isinstance(books_src, str):
    with open(books_src, 'r') as f:
        books = json.load(f)
else:
    books = books_src

rev_df = pd.DataFrame(reviews)
books_df = pd.DataFrame(books)

# normalize ids to join (purchaseid_123 -> 123, bookid_123 -> 123)
rev_df['id_num'] = rev_df['purchase_id'].astype(str).str.extract(r'(\d+)')[0]
books_df['id_num'] = books_df['book_id'].astype(str).str.extract(r'(\d+)')[0]

# parse rating numeric
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

# keep children's books by categories string containing "Children's Books"
books_df['is_children'] = books_df['categories'].astype(str).str.contains("Children's Books", na=False)
child_books = books_df[books_df['is_children']].copy()

# join and aggregate average rating from 2020 onwards
merged = rev_df.merge(child_books[['book_id','title','categories','id_num']], on='id_num', how='inner')
agg = merged.groupby(['book_id','title'], as_index=False).agg(avg_rating=('rating','mean'), review_count=('rating','size'))
res = agg[agg['avg_rating'] >= 4.5].sort_values(['avg_rating','review_count'], ascending=[False, False])

# format answer lines
lines = []
for _, r in res.iterrows():
    lines.append(f"{r['title']} (book_id: {r['book_id']}) - avg_rating: {r['avg_rating']:.2f} ({int(r['review_count'])} reviews since 2020)")
answer = "\n".join(lines) if lines else "No Children's Books found with average rating >= 4.5 based on reviews from 2020 onwards."

print('__RESULT__:')
print(json.dumps({'answer': answer, 'count': int(res.shape[0])}))"""

env_args = {'var_call_rCo5BaBGx3dT0h1Fp0IICMON': 'file_storage/call_rCo5BaBGx3dT0h1Fp0IICMON.json', 'var_call_79hsuOGmuMNVpGSY8YWjkwn8': ['review'], 'var_call_gb5dIlMYUWNAEuqhH9sM5IHd': 'file_storage/call_gb5dIlMYUWNAEuqhH9sM5IHd.json'}

exec(code, env_args)
