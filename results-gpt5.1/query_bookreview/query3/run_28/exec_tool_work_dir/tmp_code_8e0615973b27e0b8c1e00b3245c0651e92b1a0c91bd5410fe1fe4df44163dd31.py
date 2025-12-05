code = """import json, pandas as pd, datetime

# Load full books_info
with open(var_call_N1VhO3qdNtHgNjV6BcVioQjP, 'r') as f:
    books = json.load(f)
books_df = pd.DataFrame(books)

# Filter to Children's Books category
def is_children(cat_str):
    try:
        cats = json.loads(cat_str)
    except Exception:
        return False
    return any("Children's Books" in c for c in cats)

books_df_children = books_df[books_df['categories'].apply(is_children)][['book_id','title']]

# Load full reviews
with open(var_call_wt0SfDlbBUT4HJxHvL2Ub7gD, 'r') as f:
    reviews = json.load(f)
rev_df = pd.DataFrame(reviews)

# Parse times and filter >= 2020-01-01
rev_df['review_time'] = pd.to_datetime(rev_df['review_time'])
rev_df = rev_df[rev_df['review_time'] >= pd.Timestamp('2020-01-01')]

# ratings to float
rev_df['rating'] = rev_df['rating'].astype(float)

# Compute average rating per purchase_id
avg_ratings = rev_df.groupby('purchase_id')['rating'].mean().reset_index()

# Join on purchase_id == book_id
merged = pd.merge(books_df_children, avg_ratings, left_on='book_id', right_on='purchase_id', how='inner')

# Filter avg rating >= 4.5
eligible = merged[merged['rating'] >= 4.5].sort_values('title')

result = eligible[['title','rating']].to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_N1VhO3qdNtHgNjV6BcVioQjP': 'file_storage/call_N1VhO3qdNtHgNjV6BcVioQjP.json', 'var_call_Rw282CCqohjoE3h6xmHGfXJB': ['review'], 'var_call_wt0SfDlbBUT4HJxHvL2Ub7gD': 'file_storage/call_wt0SfDlbBUT4HJxHvL2Ub7gD.json'}

exec(code, env_args)
