code = """import json, pandas as pd

# Load full books_info result
with open(var_call_B1YjH6Er9f5YBLD1s7QK6lOS, 'r') as f:
    books = json.load(f)

# Filter to Children's Books using the categories string
books_df = pd.DataFrame(books)
children_mask = books_df['categories'].astype(str).str.contains("Children's Books", regex=False)
children_books = books_df[children_mask].copy()

# Load reviews from 2020 onwards
with open(var_call_vhu1RtbfdFm8YEwVxFRiIj60, 'r') as f:
    reviews = json.load(f)

reviews_df = pd.DataFrame(reviews)

# Ensure types
reviews_df['rating'] = reviews_df['rating'].astype(float)

# Compute average rating per purchase_id
avg_ratings = reviews_df.groupby('purchase_id', as_index=False)['rating'].mean()

# Keep those with avg rating >= 4.5
high_rated = avg_ratings[avg_ratings['rating'] >= 4.5].copy()

# Join with children's books on purchase_id == book_id
merged = pd.merge(children_books, high_rated, left_on='book_id', right_on='purchase_id', how='inner')

# Select unique books with their titles and average rating
result_df = merged[['book_id', 'title', 'rating']].drop_duplicates().sort_values('title')

result = result_df.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_B1YjH6Er9f5YBLD1s7QK6lOS': 'file_storage/call_B1YjH6Er9f5YBLD1s7QK6lOS.json', 'var_call_9muAqeyaJB8Ve9fmnQlNWFPv': ['review'], 'var_call_vhu1RtbfdFm8YEwVxFRiIj60': 'file_storage/call_vhu1RtbfdFm8YEwVxFRiIj60.json'}

exec(code, env_args)
