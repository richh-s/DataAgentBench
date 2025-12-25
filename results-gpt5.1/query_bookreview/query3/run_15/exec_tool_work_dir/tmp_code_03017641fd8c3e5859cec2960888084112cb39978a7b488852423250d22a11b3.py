code = """import json, pandas as pd

# Load full books_info and review data from files
with open(var_call_hMqcQHTihltvWT6dHqGz7hR6, 'r') as f:
    books = json.load(f)
with open(var_call_mSzjPDkaKDJoLfcNto2tq35W, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Filter to Children's Books via categories string
child_books = books_df[books_df['categories'].str.contains("Children's Books", na=False)].copy()

# Join reviews (purchase_id ~ book_id)
merged = reviews_df.merge(child_books, left_on='purchase_id', right_on='book_id', how='inner')

# Ensure rating is float
merged['rating'] = merged['rating'].astype(float)

# Compute average rating per book_id from 2020 onwards (already filtered in SQL)
avg_ratings = merged.groupby(['book_id', 'title'])['rating'].mean().reset_index()

# Filter for avg rating >= 4.5
res = avg_ratings[avg_ratings['rating'] >= 4.5].sort_values('rating', ascending=False)

result = res.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_hMqcQHTihltvWT6dHqGz7hR6': 'file_storage/call_hMqcQHTihltvWT6dHqGz7hR6.json', 'var_call_gqzeQ6irP3olPsgX6AD7FZ1F': ['review'], 'var_call_mSzjPDkaKDJoLfcNto2tq35W': 'file_storage/call_mSzjPDkaKDJoLfcNto2tq35W.json'}

exec(code, env_args)
