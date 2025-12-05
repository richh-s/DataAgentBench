code = """import json, pandas as pd

# Load full books_info
with open(var_call_61PxSOGeTnAVp4SrEcapfXoz, 'r') as f:
    books = json.load(f)

# Filter Children's Books
books_df = pd.DataFrame(books)
child_books = books_df[books_df['categories'].str.contains("Children's Books", na=False)].copy()

# Load full reviews from file
with open(var_call_qHPfgWHUbDrP1YxpBn5hG37d, 'r') as f:
    reviews = json.load(f)

rev_df = pd.DataFrame(reviews)
rev_df['rating'] = rev_df['rating'].astype(float)

# Join on purchase_id/book_id
merged = rev_df.merge(child_books[['book_id', 'title']], left_on='purchase_id', right_on='book_id', how='inner')

# Compute average rating per book from 2020 onwards (already filtered in SQL)
agg = merged.groupby(['book_id', 'title'])['rating'].mean().reset_index()
result_df = agg[agg['rating'] >= 4.5].sort_values('rating', ascending=False)

result = result_df.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_61PxSOGeTnAVp4SrEcapfXoz': 'file_storage/call_61PxSOGeTnAVp4SrEcapfXoz.json', 'var_call_WaNifVdd9GmVw9qMCNW5bP5p': ['review'], 'var_call_qHPfgWHUbDrP1YxpBn5hG37d': 'file_storage/call_qHPfgWHUbDrP1YxpBn5hG37d.json'}

exec(code, env_args)
