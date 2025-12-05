code = """import json, pandas as pd

books_path = var_call_sNGTcHprym5v9lfqi8VzGCsn
reviews_path = var_call_bIDSLwezs8rgh2CsLSfEF0co

with open(books_path, 'r') as f:
    books = json.load(f)
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

children_books = books_df[books_df['categories'].str.contains("Children's Books", na=False)].copy()

reviews_df['review_time'] = pd.to_datetime(reviews_df['review_time'])
reviews_2020 = reviews_df[reviews_df['review_time'] >= '2020-01-01'].copy()

reviews_2020['rating'] = reviews_2020['rating'].astype(float)

avg_ratings = reviews_2020.groupby('purchase_id')['rating'].mean().reset_index()

merged = children_books.merge(avg_ratings, left_on='book_id', right_on='purchase_id', how='inner')

result_df = merged[merged['rating'] >= 4.5][['book_id', 'title', 'rating']].sort_values(by='rating', ascending=False)

result = result_df.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_sNGTcHprym5v9lfqi8VzGCsn': 'file_storage/call_sNGTcHprym5v9lfqi8VzGCsn.json', 'var_call_XHKFzYeDMQDwFZq7sJJY1Cww': ['review'], 'var_call_bIDSLwezs8rgh2CsLSfEF0co': 'file_storage/call_bIDSLwezs8rgh2CsLSfEF0co.json'}

exec(code, env_args)
