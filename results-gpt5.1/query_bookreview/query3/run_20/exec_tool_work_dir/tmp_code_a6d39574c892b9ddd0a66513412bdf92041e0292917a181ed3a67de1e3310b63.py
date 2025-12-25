code = """import json, pandas as pd

# Load full books_info result
books_path = var_call_6Miy7nl5FFo5k7yiWPcZcLfL
with open(books_path, 'r') as f:
    books = json.load(f)

books_df = pd.DataFrame(books)

# Filter Children's Books
child_mask = books_df['categories'].fillna('').str.contains("Children's Books")
child_books = books_df[child_mask].copy()

# Load full reviews result
reviews_path = var_call_6kajwvG7JvYpVhX7OOG6BjVe
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

reviews_df = pd.DataFrame(reviews)

# Ensure numeric rating
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'])

# Compute average rating per purchase_id from 2020 onwards
avg_ratings = reviews_df.groupby('purchase_id', as_index=False)['rating'].mean()

# Join with child_books on purchase_id (purchase_id ~ book_id)
merged = child_books.merge(avg_ratings, left_on='book_id', right_on='purchase_id', how='inner')

# Filter for avg rating >= 4.5
high_rated = merged[merged['rating'] >= 4.5]

# Prepare result: unique books with their titles and avg rating
result_df = high_rated[['book_id', 'title', 'rating']].drop_duplicates().sort_values('title')

result = result_df.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_6Miy7nl5FFo5k7yiWPcZcLfL': 'file_storage/call_6Miy7nl5FFo5k7yiWPcZcLfL.json', 'var_call_riyuY4FYNg1xSsnMdp1BIpgG': ['review'], 'var_call_6kajwvG7JvYpVhX7OOG6BjVe': 'file_storage/call_6kajwvG7JvYpVhX7OOG6BjVe.json'}

exec(code, env_args)
