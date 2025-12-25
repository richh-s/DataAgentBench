code = """import json, pandas as pd

# Load full books_info result
with open(var_call_GJdO55XxFVZz1E3Ly1rCEHIq, 'r') as f:
    books = json.load(f)

books_df = pd.DataFrame(books)

# Filter for Children's Books in categories string
child_books = books_df[books_df['categories'].str.contains("Children's Books", na=False)].copy()

# Load full reviews result
with open(var_call_qqFrk6pEOrXcZa5ILtdWBd9H, 'r') as f:
    reviews = json.load(f)

reviews_df = pd.DataFrame(reviews)

# Ensure numeric rating
df = reviews_df.copy()
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# Fuzzy join: purchase_id == book_id
merged = pd.merge(df, child_books, left_on='purchase_id', right_on='book_id', how='inner')

# Compute average rating per book from 2020 onwards (already filtered in SQL)
avg = merged.groupby(['book_id', 'title'])['rating'].mean().reset_index()

# Filter by avg rating >= 4.5
result_df = avg[avg['rating'] >= 4.5].sort_values('rating', ascending=False)

result = result_df.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_GJdO55XxFVZz1E3Ly1rCEHIq': 'file_storage/call_GJdO55XxFVZz1E3Ly1rCEHIq.json', 'var_call_oLWuvUNDtprOMCDfnk0kStyo': ['review'], 'var_call_qqFrk6pEOrXcZa5ILtdWBd9H': 'file_storage/call_qqFrk6pEOrXcZa5ILtdWBd9H.json'}

exec(code, env_args)
