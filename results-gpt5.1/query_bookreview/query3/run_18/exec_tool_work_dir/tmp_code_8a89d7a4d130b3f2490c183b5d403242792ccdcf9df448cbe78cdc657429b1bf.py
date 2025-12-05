code = """import json, pandas as pd

books_path = var_call_NarDSH90HH1P3RI7VN0mP2DD
with open(books_path, 'r') as f:
    books = json.load(f)

reviews_path = var_call_CNclHvqRq2sF46zlYknt882U
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

children_books = books_df[books_df['categories'].str.contains("Children's Books")]

merged = reviews_df.merge(children_books, left_on='purchase_id', right_on='book_id', how='inner')
merged['rating'] = pd.to_numeric(merged['rating'])

avg_ratings = merged.groupby(['book_id', 'title'])['rating'].mean().reset_index()
result_df = avg_ratings[avg_ratings['rating'] >= 4.5].sort_values('rating', ascending=False)

result = result_df.to_dict(orient='records')
result_json = json.dumps(result)

print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_NarDSH90HH1P3RI7VN0mP2DD': 'file_storage/call_NarDSH90HH1P3RI7VN0mP2DD.json', 'var_call_AopkPhdi2tproRqbZVo2NteE': ['review'], 'var_call_CNclHvqRq2sF46zlYknt882U': 'file_storage/call_CNclHvqRq2sF46zlYknt882U.json'}

exec(code, env_args)
