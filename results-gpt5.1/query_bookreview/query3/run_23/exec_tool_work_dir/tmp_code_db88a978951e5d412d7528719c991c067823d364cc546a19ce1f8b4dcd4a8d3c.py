code = """import json, pandas as pd

# Load full books data from file
with open(var_call_Bf0Ok0y0lEoMGMlUauiYvvAt, 'r') as f:
    books = json.load(f)

books_df = pd.DataFrame(books)

# Filter Children's Books by checking substring in categories string
child_books_df = books_df[books_df['categories'].str.contains("Children's Books", na=False)].copy()

# Keep only relevant columns
child_books_df = child_books_df[['book_id', 'title']]

# Load full review data
with open(var_call_zHu68piN7sjKAYYi1giherqN, 'r') as f:
    reviews = json.load(f)

reviews_df = pd.DataFrame(reviews)

# ratings may be strings; convert to float
reviews_df['rating'] = reviews_df['rating'].astype(float)

# Compute average rating per purchase_id from 2020 onwards (already filtered in SQL)
avg_ratings = reviews_df.groupby('purchase_id', as_index=False)['rating'].mean()

# Fuzzy join: purchase_id in reviews matches book_id in books
merged = pd.merge(child_books_df, avg_ratings, left_on='book_id', right_on='purchase_id', how='inner')

# Filter for average rating >= 4.5
high_rated = merged[merged['rating'] >= 4.5].copy()

# Sort by rating descending, then title
high_rated = high_rated.sort_values(['rating', 'title'], ascending=[False, True])

result = high_rated[['title', 'book_id', 'rating']].to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Bf0Ok0y0lEoMGMlUauiYvvAt': 'file_storage/call_Bf0Ok0y0lEoMGMlUauiYvvAt.json', 'var_call_8O7kqCCAH8XU4GtO2Gzw0V1f': ['review'], 'var_call_zHu68piN7sjKAYYi1giherqN': 'file_storage/call_zHu68piN7sjKAYYi1giherqN.json'}

exec(code, env_args)
