code = """import json, pandas as pd

books_path = var_call_Wut65reKpgF3V2yZIOHdmpWt
reviews_path = var_call_GAZM1gwv1w4cz5yzWUNpZpJb

with open(books_path, 'r') as f:
    books = json.load(f)
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

child_books = books_df[books_df['categories'].str.contains("Children's Books", na=False)].copy()

avg_ratings = reviews_df.groupby('purchase_id', as_index=False)['rating'].mean()

merged = child_books.merge(avg_ratings, left_on='book_id', right_on='purchase_id', how='inner')

result_df = merged[merged['rating'] >= 4.5][['title']].drop_duplicates().sort_values('title')

result = result_df['title'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Wut65reKpgF3V2yZIOHdmpWt': 'file_storage/call_Wut65reKpgF3V2yZIOHdmpWt.json', 'var_call_TuO809lEKRRMm6fQlvu2oy0X': ['review'], 'var_call_GAZM1gwv1w4cz5yzWUNpZpJb': 'file_storage/call_GAZM1gwv1w4cz5yzWUNpZpJb.json'}

exec(code, env_args)
