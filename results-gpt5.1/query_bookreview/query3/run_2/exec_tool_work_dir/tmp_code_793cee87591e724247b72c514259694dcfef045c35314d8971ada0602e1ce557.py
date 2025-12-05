code = """import json, pandas as pd
books_path = var_call_naxKxyzf5NiGElQXdbKlBquM
reviews_path = var_call_IGWKVNSCTSBK8Iv9TfF92Wj3
books = pd.read_json(books_path)
reviews = pd.read_json(reviews_path)
books_children = books[books['categories'].str.contains("Children's Books", na=False)].copy()
reviews['rating'] = reviews['rating'].astype(float)
merged = reviews.merge(books_children, left_on='purchase_id', right_on='book_id', how='inner')
avg = merged.groupby(['book_id','title'], as_index=False)['rating'].mean()
res = avg[avg['rating']>=4.5].sort_values('rating', ascending=False)
result = res.to_dict(orient='records')
result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_naxKxyzf5NiGElQXdbKlBquM': 'file_storage/call_naxKxyzf5NiGElQXdbKlBquM.json', 'var_call_kmWX61OuEnQl522UMESmxktx': ['review'], 'var_call_IGWKVNSCTSBK8Iv9TfF92Wj3': 'file_storage/call_IGWKVNSCTSBK8Iv9TfF92Wj3.json'}

exec(code, env_args)
