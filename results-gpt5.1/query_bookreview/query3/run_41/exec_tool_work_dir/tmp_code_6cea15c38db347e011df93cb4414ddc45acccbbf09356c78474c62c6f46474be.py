code = """import json, pandas as pd

books_path = var_call_cvTA0zy28zpqSWJDesKrUFnE
reviews_path = var_call_1lG59cDOCSxCiMYYnBoJvOIm

with open(books_path, 'r') as f:
    books = json.load(f)
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

children_books = books_df[books_df['categories'].str.contains("Children's Books", na=False)].copy()

merged = reviews_df.merge(children_books, left_on='purchase_id', right_on='book_id', how='inner')

merged['rating'] = merged['rating'].astype(float)

agg = merged.groupby(['book_id', 'title'], as_index=False)['rating'].mean()

result_df = agg[agg['rating'] >= 4.5].sort_values('rating', ascending=False)

result = result_df.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_cvTA0zy28zpqSWJDesKrUFnE': 'file_storage/call_cvTA0zy28zpqSWJDesKrUFnE.json', 'var_call_0vvUcxZWgL25y32vQm85YuVC': ['review'], 'var_call_1lG59cDOCSxCiMYYnBoJvOIm': 'file_storage/call_1lG59cDOCSxCiMYYnBoJvOIm.json'}

exec(code, env_args)
