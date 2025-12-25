code = """import json, pandas as pd
from pathlib import Path

books_path = var_call_TrgowPlBoCGbb6mfpa5p253B
reviews_path = var_call_70Jy0sLghjQh9uBaLvXesfs3

books = pd.read_json(books_path)
reviews = pd.read_json(reviews_path)

children_books = books[books['categories'].str.contains("Children's Books", na=False)].copy()

reviews['rating'] = reviews['rating'].astype(float)

merged = reviews.merge(children_books, left_on='purchase_id', right_on='book_id', how='inner')

agg = merged.groupby(['book_id','title'])['rating'].mean().reset_index()
result_df = agg[agg['rating'] >= 4.5].sort_values('rating', ascending=False)

result = result_df.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_TrgowPlBoCGbb6mfpa5p253B': 'file_storage/call_TrgowPlBoCGbb6mfpa5p253B.json', 'var_call_dp5GE9aLYjaSbPyOd2cCTHNU': ['review'], 'var_call_70Jy0sLghjQh9uBaLvXesfs3': 'file_storage/call_70Jy0sLghjQh9uBaLvXesfs3.json'}

exec(code, env_args)
