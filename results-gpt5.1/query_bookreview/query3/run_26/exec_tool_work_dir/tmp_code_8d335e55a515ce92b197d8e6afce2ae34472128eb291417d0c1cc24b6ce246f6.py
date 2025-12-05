code = """import json, pandas as pd

# Load full books info
with open(var_call_KTxGM4aZMQi5ANx9tpYJCMCi, 'r') as f:
    books = json.load(f)
books_df = pd.DataFrame(books)

# Filter Children's Books
child_mask = books_df['categories'].fillna('').str.contains("Children's Books")
child_books = books_df[child_mask].copy()

# Load full reviews
with open(var_call_CTYFXUnMNnJiPRZHVu9O2aqi, 'r') as f:
    reviews = json.load(f)
rev_df = pd.DataFrame(reviews)

# Ensure rating is float
rev_df['rating'] = rev_df['rating'].astype(float)

# Compute avg rating per purchase_id
avg_ratings = rev_df.groupby('purchase_id')['rating'].mean().reset_index()

# Join on purchase_id == book_id (exact match as per provided ids)
merged = pd.merge(child_books, avg_ratings, left_on='book_id', right_on='purchase_id', how='inner')

# Filter by avg rating >= 4.5
high_rated = merged[merged['rating'] >= 4.5]

# Prepare result: unique titles with their book_id and avg rating
result_df = high_rated[['book_id', 'title', 'rating']].drop_duplicates().sort_values('rating', ascending=False)
result = result_df.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_KTxGM4aZMQi5ANx9tpYJCMCi': 'file_storage/call_KTxGM4aZMQi5ANx9tpYJCMCi.json', 'var_call_kEFzFwhDabfiRNe8UyOGDncf': ['review'], 'var_call_CTYFXUnMNnJiPRZHVu9O2aqi': 'file_storage/call_CTYFXUnMNnJiPRZHVu9O2aqi.json'}

exec(code, env_args)
