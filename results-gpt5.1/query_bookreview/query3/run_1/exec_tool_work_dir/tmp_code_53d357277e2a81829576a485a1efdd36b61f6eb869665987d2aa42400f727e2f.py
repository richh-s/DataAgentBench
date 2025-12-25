code = """import json, pandas as pd

books_file = var_call_Xcf99LhkynK3cj0sFgq2HSo4
reviews_file = var_call_DthkxhT7Q9ejITmA4GvI4KtD

with open(books_file, 'r') as f:
    books = json.load(f)
with open(reviews_file, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

children_books = books_df[books_df['categories'].str.contains("Children's Books", na=False)].copy()

merged = reviews_df.merge(children_books, left_on='purchase_id', right_on='book_id', how='inner')
merged['rating'] = merged['rating'].astype(float)

avg_ratings = merged.groupby(['book_id', 'title'], as_index=False)['rating'].mean()
result_df = avg_ratings[avg_ratings['rating'] >= 4.5].sort_values('rating', ascending=False)

result = result_df.to_dict(orient='records')

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_Xcf99LhkynK3cj0sFgq2HSo4': 'file_storage/call_Xcf99LhkynK3cj0sFgq2HSo4.json', 'var_call_xKi7nrBGnvAbMGNseGHHTlr8': ['review'], 'var_call_DthkxhT7Q9ejITmA4GvI4KtD': 'file_storage/call_DthkxhT7Q9ejITmA4GvI4KtD.json'}

exec(code, env_args)
