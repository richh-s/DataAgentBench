code = """import json
import pandas as pd
import re

# Load the query results from storage file paths
with open(var_call_CR8z9E9ctk84x7pqzfPltmDI, 'r', encoding='utf-8') as f:
    reviews = json.load(f)
with open(var_call_t0GZFT2c0Y17HavLXvuLx1Pb, 'r', encoding='utf-8') as f:
    books = json.load(f)

# Create DataFrames
rev_df = pd.DataFrame(reviews)
books_df = pd.DataFrame(books)

# Clean and convert ratings to numeric
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
rev_df = rev_df.dropna(subset=['rating', 'purchase_id'])

# Extract numeric id suffix from purchase_id
rev_df['id_num'] = rev_df['purchase_id'].astype(str).str.extract(r'(\d+)$')
# Convert to int
rev_df['id_num'] = pd.to_numeric(rev_df['id_num'], errors='coerce').astype(pd.Int64Dtype())
rev_df = rev_df.dropna(subset=['id_num'])
rev_df['id_num'] = rev_df['id_num'].astype(int)

# Aggregate per book (book-level average rating)
book_avg = rev_df.groupby('id_num', dropna=True)['rating'].mean().reset_index().rename(columns={'rating':'book_avg_rating'})

# Extract numeric suffix from books.book_id
books_df['id_num'] = books_df['book_id'].astype(str).str.extract(r'(\d+)$')
books_df['id_num'] = pd.to_numeric(books_df['id_num'], errors='coerce').astype(pd.Int64Dtype())
books_df = books_df.dropna(subset=['id_num'])
books_df['id_num'] = books_df['id_num'].astype(int)

# Extract publication year from details using regex for years between 1000 and 2023
def extract_year(text):
    if not isinstance(text, str):
        return None
    # find all 4-digit numbers
    years = re.findall(r'\b(1[0-9]{3}|20[0-2][0-9]|2023)\b', text)
    if years:
        # years is list of strings (matched groups), take first
        try:
            y = int(years[0])
            return y
        except:
            return None
    return None

books_df['pub_year'] = books_df['details'].apply(extract_year)

# Merge book averages with books info on id_num
merged = pd.merge(book_avg, books_df[['id_num','book_id','title','pub_year']], on='id_num', how='left')

# Keep only entries with a pub_year
merged = merged.dropna(subset=['pub_year'])
merged['pub_year'] = merged['pub_year'].astype(int)

# Compute decade label
merged['decade_start'] = (merged['pub_year'] // 10) * 10
merged['decade'] = merged['decade_start'].astype(str) + 's'

# Group by decade: need at least 10 distinct books that have been rated
group = merged.groupby('decade').agg(
    num_books = ('book_id','nunique'),
    avg_rating = ('book_avg_rating','mean')
).reset_index()

# Filter decades with at least 10 distinct books
eligible = group[group['num_books'] >= 10]

# If no eligible decades, return None
if eligible.empty:
    result = None
else:
    # Find decade with highest average rating. If tie, pick the decade with highest avg then smallest decade_start? We'll pick the max avg and then earliest decade_start.
    max_avg = eligible['avg_rating'].max()
    top = eligible[eligible['avg_rating'] == max_avg].sort_values('decade').iloc[0]
    result = top['decade']

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_gVrjlMDRfW7rZT4TL4wLpz22': ['review'], 'var_call_58BZpGxJ9vOGaH0guXgfeuaF': ['books_info'], 'var_call_CR8z9E9ctk84x7pqzfPltmDI': 'file_storage/call_CR8z9E9ctk84x7pqzfPltmDI.json', 'var_call_t0GZFT2c0Y17HavLXvuLx1Pb': 'file_storage/call_t0GZFT2c0Y17HavLXvuLx1Pb.json'}

exec(code, env_args)
