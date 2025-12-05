code = """import json, pandas as pd

# Load full books_info result from file
books_path = var_call_NHKfpmDmJTWFerBeaFM5hzov
with open(books_path, 'r') as f:
    books_data = json.load(f)
books_df = pd.DataFrame(books_data)

# Filter to Children's Books
child_books = books_df[books_df['categories'].str.contains("Children's Books", regex=False, na=False)].copy()
child_books = child_books[['book_id', 'title']]

# Load full review result
reviews_path = var_call_ONRtC9Jguhr6ITmJv4rBWb5z
with open(reviews_path, 'r') as f:
    reviews_data = json.load(f)
rev_df = pd.DataFrame(reviews_data)

# Ensure rating is float
rev_df['rating'] = rev_df['rating'].astype(float)

# Join on book_id == purchase_id (exact, as per provided IDs)
merged = rev_df.merge(child_books, left_on='purchase_id', right_on='book_id', how='inner')

# Compute average rating per book from 2020 onward
avg_ratings = merged.groupby(['book_id', 'title'])['rating'].mean().reset_index()

# Filter to average rating >= 4.5
high_rated = avg_ratings[avg_ratings['rating'] >= 4.5].sort_values('rating', ascending=False)

result = high_rated.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_NHKfpmDmJTWFerBeaFM5hzov': 'file_storage/call_NHKfpmDmJTWFerBeaFM5hzov.json', 'var_call_wSdy1iOnLeVVwNZF1rBLEu4M': ['review'], 'var_call_ONRtC9Jguhr6ITmJv4rBWb5z': 'file_storage/call_ONRtC9Jguhr6ITmJv4rBWb5z.json'}

exec(code, env_args)
