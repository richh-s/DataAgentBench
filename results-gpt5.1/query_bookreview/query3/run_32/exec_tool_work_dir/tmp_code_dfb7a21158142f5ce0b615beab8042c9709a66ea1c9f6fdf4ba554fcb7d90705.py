code = """import json, pandas as pd

# Load full books_info result
with open(var_call_XqNY1hbnJX6bRuSofjfQgj5h, 'r') as f:
    books = json.load(f)
books_df = pd.DataFrame(books)

# Filter to Children's Books category
children = books_df[books_df['categories'].str.contains("Children's Books", na=False)].copy()

# Load full reviews result
with open(var_call_MTYud3dIq8XEYQi4evjL6OMW, 'r') as f:
    reviews = json.load(f)
reviews_df = pd.DataFrame(reviews)

# Ensure numeric rating
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')

# Aggregate average rating since 2020 by purchase_id
avg_ratings = reviews_df.groupby('purchase_id', as_index=False)['rating'].mean()

# Filter for avg rating >= 4.5
high_rated = avg_ratings[avg_ratings['rating'] >= 4.5].copy()

# Join high_rated with children's books on purchase_id == book_id
result = pd.merge(high_rated, children, left_on='purchase_id', right_on='book_id', how='inner')

# Select unique titles with their average ratings
final = result[['title','rating']].drop_duplicates().sort_values('title')

out = final.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_XqNY1hbnJX6bRuSofjfQgj5h': 'file_storage/call_XqNY1hbnJX6bRuSofjfQgj5h.json', 'var_call_bJtu9pqOy5DJcDvylmZjy9NB': ['review'], 'var_call_MTYud3dIq8XEYQi4evjL6OMW': 'file_storage/call_MTYud3dIq8XEYQi4evjL6OMW.json'}

exec(code, env_args)
