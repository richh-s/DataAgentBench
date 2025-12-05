code = """import json, pandas as pd

# Load full books_info result
with open(var_call_8yRtVd8OEi7ukl5aERzwBayw, 'r') as f:
    books = json.load(f)

books_df = pd.DataFrame(books)

# Filter Children's Books using substring match on categories string
child_books = books_df[books_df['categories'].str.contains("Children's Books", na=False)].copy()

# Load full reviews result
with open(var_call_wvub8Yw2CE3xVP5FKoQHRX0r, 'r') as f:
    reviews = json.load(f)

reviews_df = pd.DataFrame(reviews)

# Ensure rating is float
reviews_df['rating'] = reviews_df['rating'].astype(float)

# Compute average rating from 2020 onwards per purchase_id
avg_ratings = reviews_df.groupby('purchase_id', as_index=False)['rating'].mean().rename(columns={'rating': 'avg_rating'})

# Fuzzy join: purchase_id like book_id (exact string match here)
merged = pd.merge(child_books, avg_ratings, left_on='book_id', right_on='purchase_id', how='inner')

# Filter for avg_rating >= 4.5
result_df = merged[merged['avg_rating'] >= 4.5][['title', 'book_id', 'avg_rating']].sort_values('avg_rating', ascending=False)

result = result_df.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_8yRtVd8OEi7ukl5aERzwBayw': 'file_storage/call_8yRtVd8OEi7ukl5aERzwBayw.json', 'var_call_aPE0xoJ7bDFKhwN80xiCTbNV': ['review'], 'var_call_wvub8Yw2CE3xVP5FKoQHRX0r': 'file_storage/call_wvub8Yw2CE3xVP5FKoQHRX0r.json'}

exec(code, env_args)
