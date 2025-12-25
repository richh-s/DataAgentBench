code = """import json, pandas as pd
from pathlib import Path

books_path = var_call_TrgowPlBoCGbb6mfpa5p253B
reviews_path = var_call_70Jy0sLghjQh9uBaLvXesfs3

books = pd.read_json(books_path)
reviews = pd.read_json(reviews_path)

children_books = books[books['categories'].str.contains("Children's Books", na=False)].copy()

reviews['rating'] = reviews['rating'].astype(float)

# compute avg rating per purchase_id
agg_reviews = reviews.groupby('purchase_id')['rating'].mean().reset_index(name='avg_rating')

merged = agg_reviews.merge(children_books, left_on='purchase_id', right_on='book_id', how='inner')

result_df = merged[merged['avg_rating'] >= 4.5][['book_id','title','avg_rating']].drop_duplicates().sort_values('avg_rating', ascending=False)

result = result_df.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_TrgowPlBoCGbb6mfpa5p253B': 'file_storage/call_TrgowPlBoCGbb6mfpa5p253B.json', 'var_call_dp5GE9aLYjaSbPyOd2cCTHNU': ['review'], 'var_call_70Jy0sLghjQh9uBaLvXesfs3': 'file_storage/call_70Jy0sLghjQh9uBaLvXesfs3.json', 'var_call_Vycx4i4TK9jEivKQgG9hsvUd': []}

exec(code, env_args)
