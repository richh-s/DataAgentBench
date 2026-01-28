code = """import json
import pandas as pd
import re
from datetime import datetime

# Load data from provided storage file paths
with open(var_call_1FcBgCKDIm7pwEtxeM28e23N, 'r') as f:
    reviews = json.load(f)
with open(var_call_17MEPLWTrGD9QV5OvoSDLmmZ, 'r') as f:
    books = json.load(f)

# Create DataFrames
rev_df = pd.DataFrame(reviews)
books_df = pd.DataFrame(books)

# Normalize review_time to datetime and filter from 2020-01-01
# Some review_time may include time with or without seconds
rev_df['review_time'] = pd.to_datetime(rev_df['review_time'], errors='coerce')
rev_df = rev_df[rev_df['review_time'] >= pd.to_datetime('2020-01-01')]

# Convert rating to numeric
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
rev_df = rev_df.dropna(subset=['rating','purchase_id'])

# Extract numeric suffix from purchase_id to map to book_id
def purchase_to_bookid(p):
    if not isinstance(p, str):
        return None
    m = re.search(r'(\d+)$', p)
    if m:
        return f"bookid_{m.group(1)}"
    return None

rev_df['book_id'] = rev_df['purchase_id'].apply(purchase_to_bookid)
rev_df = rev_df.dropna(subset=['book_id'])

# Ensure books_df has categories as string; filter for Children's Books
# Merge
merged = rev_df.merge(books_df[['book_id','title','categories']], on='book_id', how='left')
merged = merged.dropna(subset=['categories'])

# Filter categories string containing "Children's Books"
merged_children = merged[merged['categories'].str.contains("Children's Books", na=False)]

# Group by book_id and compute average rating and count
grouped = merged_children.groupby(['book_id','title']).agg(
    average_rating=('rating', 'mean'),
    review_count=('rating', 'count')
).reset_index()

# Filter average_rating >= 4.5
result_df = grouped[grouped['average_rating'] >= 4.5].sort_values(by=['average_rating','review_count'], ascending=[False, False])

# Prepare JSON-serializable result
result = []
for _, row in result_df.iterrows():
    result.append({
        'book_id': row['book_id'],
        'title': row['title'],
        'average_rating': round(float(row['average_rating']), 3),
        'review_count': int(row['review_count'])
    })

# Print in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_mVVpJoNT9uzr2PlzsQWzbkqG': ['review'], 'var_call_tRrgSzlaazg8qOSlICKzoF4A': ['books_info'], 'var_call_1FcBgCKDIm7pwEtxeM28e23N': 'file_storage/call_1FcBgCKDIm7pwEtxeM28e23N.json', 'var_call_17MEPLWTrGD9QV5OvoSDLmmZ': 'file_storage/call_17MEPLWTrGD9QV5OvoSDLmmZ.json'}

exec(code, env_args)
