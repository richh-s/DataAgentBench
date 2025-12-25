code = """import json, pandas as pd

# Load full books data
with open(var_call_LGMuWFq92KOhtZUZ7f3T96uy, 'r') as f:
    books = json.load(f)

books_df = pd.DataFrame(books)

# Filter to Children's Books
child_mask = books_df['categories'].fillna('').str.contains("Children's Books")
child_books = books_df[child_mask].copy()

# Load full reviews data
with open(var_call_ZLAjqnfWsOALdMWNYyCtkMIb, 'r') as f:
    reviews = json.load(f)

rev_df = pd.DataFrame(reviews)

# Ensure numeric rating
rev_df['rating'] = pd.to_numeric(rev_df['rating'])

# Fuzzy join: assume purchase_id like 'purchaseid_8' maps to 'bookid_8'
rev_df['book_id'] = rev_df['purchase_id'].str.replace('purchaseid_', 'bookid_', regex=False)

# Aggregate average rating per book from 2020 onwards (already filtered in SQL)
avg_ratings = rev_df.groupby('book_id')['rating'].mean().reset_index(name='avg_rating')

# Merge with children's books
merged = child_books.merge(avg_ratings, on='book_id', how='inner')

# Filter avg rating >= 4.5
result_df = merged[merged['avg_rating'] >= 4.5][['book_id', 'title', 'avg_rating']].sort_values('avg_rating', ascending=False)

result = result_df.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_LGMuWFq92KOhtZUZ7f3T96uy': 'file_storage/call_LGMuWFq92KOhtZUZ7f3T96uy.json', 'var_call_oSljn8CcjPyc3SRtbhPgH8YI': ['review'], 'var_call_ZLAjqnfWsOALdMWNYyCtkMIb': 'file_storage/call_ZLAjqnfWsOALdMWNYyCtkMIb.json'}

exec(code, env_args)
