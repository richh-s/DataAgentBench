code = """import json, pandas as pd

books_path = var_call_L5sYQEeWEE7u1mU5YyWrcWbB
reviews_path = var_call_xWR3CeWTXeHvgCNlXwaa8GeN

with open(books_path, 'r') as f:
    books = json.load(f)
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

children_books = books_df[books_df['categories'].str.contains("Children's Books", na=False)].copy()

merged = reviews_df.merge(children_books, left_on='purchase_id', right_on='book_id', how='inner')
merged['rating'] = merged['rating'].astype(float)

avg_ratings = merged.groupby(['book_id', 'title'])['rating'].mean().reset_index()

high_rated = avg_ratings[avg_ratings['rating'] >= 4.5].sort_values('rating', ascending=False)

result = high_rated.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_L5sYQEeWEE7u1mU5YyWrcWbB': 'file_storage/call_L5sYQEeWEE7u1mU5YyWrcWbB.json', 'var_call_2qviaiizxf4JlPdvZGFqI3GS': ['review'], 'var_call_xWR3CeWTXeHvgCNlXwaa8GeN': 'file_storage/call_xWR3CeWTXeHvgCNlXwaa8GeN.json'}

exec(code, env_args)
