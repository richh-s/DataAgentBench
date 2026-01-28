code = """import json, pandas as pd

# load books
p_books = var_call_gMLoZJDwqy50BasFQ72Ifvh0
with open(p_books, 'r') as f:
    books = json.load(f)
books_df = pd.DataFrame(books)
# filter Children's Books by categories string contains
child_df = books_df[books_df['categories'].fillna('').str.contains("Children's Books", regex=False)].copy()

# load reviews 2020+
p_reviews = var_call_STWpXBP0oa6U9Qz50TvTz59C
with open(p_reviews, 'r') as f:
    rev = json.load(f)
rev_df = pd.DataFrame(rev)
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

# join purchaseid_x to bookid_x by numeric suffix
child_df['id_num'] = pd.to_numeric(child_df['book_id'].str.extract(r'(\d+)$')[0], errors='coerce')
rev_df['id_num'] = pd.to_numeric(rev_df['purchase_id'].str.extract(r'(\d+)$')[0], errors='coerce')
merged = pd.merge(rev_df, child_df[['book_id','title','id_num']], on='id_num', how='inner')

# average ratings per book based on 2020+ reviews
agg = merged.groupby(['book_id','title'], as_index=False).agg(avg_rating=('rating','mean'), review_count=('rating','size'))
res = agg[agg['avg_rating']>=4.5].sort_values(['avg_rating','review_count'], ascending=[False, False])

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_gMLoZJDwqy50BasFQ72Ifvh0': 'file_storage/call_gMLoZJDwqy50BasFQ72Ifvh0.json', 'var_call_SBhsjADBn9t6ARUdfeTckIxy': ['review'], 'var_call_STWpXBP0oa6U9Qz50TvTz59C': 'file_storage/call_STWpXBP0oa6U9Qz50TvTz59C.json'}

exec(code, env_args)
