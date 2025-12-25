code = """import json, pandas as pd
from pathlib import Path

# Load full books data
books_path = var_call_5DdV2gMgRvrJI0ksmcWSroUq
with open(books_path, 'r') as f:
    books = json.load(f)

books_df = pd.DataFrame(books)

# Filter Children's Books
child_mask = books_df['categories'].fillna('').str.contains("Children's Books")
child_books = books_df[child_mask].copy()

# Load full reviews data
reviews_path = var_call_puzmx4ebi3Kyrer17awk4P8F
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

reviews_df = pd.DataFrame(reviews)

# Ensure rating is float
reviews_df['rating'] = reviews_df['rating'].astype(float)

# Compute average rating per purchase_id from 2020 onwards
avg_ratings = reviews_df.groupby('purchase_id', as_index=False)['rating'].mean()

# Join with child books on book_id == purchase_id
merged = pd.merge(child_books, avg_ratings, left_on='book_id', right_on='purchase_id', how='inner')

# Filter by avg rating >= 4.5
result_df = merged[merged['rating'] >= 4.5][['book_id', 'title', 'rating']].sort_values('rating', ascending=False)

result = result_df.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_5DdV2gMgRvrJI0ksmcWSroUq': 'file_storage/call_5DdV2gMgRvrJI0ksmcWSroUq.json', 'var_call_kwlSlnJIeqAGTFQDvpDbh1pe': ['review'], 'var_call_puzmx4ebi3Kyrer17awk4P8F': 'file_storage/call_puzmx4ebi3Kyrer17awk4P8F.json'}

exec(code, env_args)
