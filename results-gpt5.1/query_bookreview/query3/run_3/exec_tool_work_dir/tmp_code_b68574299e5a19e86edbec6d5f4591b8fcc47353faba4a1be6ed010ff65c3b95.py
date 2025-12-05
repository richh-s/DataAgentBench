code = """import json, pandas as pd, os

# Load full books data
with open(var_call_wvReiJ6pT0b8VMDGxXf6g51a, 'r') as f:
    books = json.load(f)

books_df = pd.DataFrame(books)

# Filter Children's Books by checking if the string contains "Children's Books"
childrens_books = books_df[books_df['categories'].astype(str).str.contains("Children's Books", na=False)].copy()

# Load full reviews data
with open(var_call_PZPXkqGr7xVAMsV2ADkUXUKg, 'r') as f:
    reviews = json.load(f)

reviews_df = pd.DataFrame(reviews)

# Ensure rating is float
reviews_df['rating'] = reviews_df['rating'].astype(float)

# Compute average rating per purchase_id from 2020 onwards (already filtered in SQL)
avg_ratings = reviews_df.groupby('purchase_id')['rating'].mean().reset_index()

# Filter for avg rating >= 4.5
high_rated = avg_ratings[avg_ratings['rating'] >= 4.5].copy()

# Join with children's books on purchase_id == book_id
merged = pd.merge(childrens_books, high_rated, left_on='book_id', right_on='purchase_id', how='inner')

# Prepare result: unique book titles
result_titles = sorted(merged['title'].unique().tolist())

out = json.dumps(result_titles)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_wvReiJ6pT0b8VMDGxXf6g51a': 'file_storage/call_wvReiJ6pT0b8VMDGxXf6g51a.json', 'var_call_sepybHzJBxUrAgyLRh9P18y6': ['review'], 'var_call_PZPXkqGr7xVAMsV2ADkUXUKg': 'file_storage/call_PZPXkqGr7xVAMsV2ADkUXUKg.json'}

exec(code, env_args)
