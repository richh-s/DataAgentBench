code = """import json, pandas as pd
books_path = var_call_1iZhFspWFAz6HvWkiwOTfFZB
reviews_path = var_call_klDB0Aa5mZxoQ7VZFoOcDYkf
with open(books_path) as f:
    books = json.load(f)
with open(reviews_path) as f:
    reviews = json.load(f)
books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)
children_books = books_df[books_df['categories'].str.contains("Children's Books", na=False)].copy()
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')
rev = reviews_df.groupby('purchase_id', as_index=False)['rating'].mean()
merged = children_books.merge(rev, left_on='book_id', right_on='purchase_id', how='inner')
result_df = merged[merged['rating'] >= 4.5][['title','rating']].sort_values('title')
result = result_df.to_dict(orient='records')
result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_1iZhFspWFAz6HvWkiwOTfFZB': 'file_storage/call_1iZhFspWFAz6HvWkiwOTfFZB.json', 'var_call_yaTRN3EmwJr2Uku6OvJVIocJ': ['review'], 'var_call_klDB0Aa5mZxoQ7VZFoOcDYkf': 'file_storage/call_klDB0Aa5mZxoQ7VZFoOcDYkf.json'}

exec(code, env_args)
