code = """import json, pandas as pd

# Load full books_info result
with open(var_call_aMSx3YxfvFVhK8VVpBu7A6pu, 'r') as f:
    books = json.load(f)

books_df = pd.DataFrame(books)

# Filter children's books using categories string
child_mask = books_df['categories'].astype(str).str.contains("Children's Books", regex=False)
child_books = books_df[child_mask][['book_id', 'title', 'categories']].copy()

# Load full review result
with open(var_call_Jw1jfzwYysYnjr7j40BZM1kc, 'r') as f:
    reviews = json.load(f)

rev_df = pd.DataFrame(reviews)
rev_df['rating'] = rev_df['rating'].astype(float)

# Aggregate average rating per purchase_id (book_id equivalent)
avg_ratings = rev_df.groupby('purchase_id', as_index=False)['rating'].mean()

# Join with children's books on book_id == purchase_id
merged = child_books.merge(avg_ratings, left_on='book_id', right_on='purchase_id', how='inner')

# Filter by avg rating >= 4.5
result_df = merged[merged['rating'] >= 4.5][['book_id', 'title', 'rating']].sort_values('rating', ascending=False)

result = result_df.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_aMSx3YxfvFVhK8VVpBu7A6pu': 'file_storage/call_aMSx3YxfvFVhK8VVpBu7A6pu.json', 'var_call_nbgXyvMYDPFpJWtO1p27GzOf': ['review'], 'var_call_Jw1jfzwYysYnjr7j40BZM1kc': 'file_storage/call_Jw1jfzwYysYnjr7j40BZM1kc.json'}

exec(code, env_args)
