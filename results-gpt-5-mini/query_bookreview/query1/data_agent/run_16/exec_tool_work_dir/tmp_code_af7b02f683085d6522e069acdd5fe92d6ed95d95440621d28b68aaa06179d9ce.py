code = """import json
import pandas as pd
import re

# Load full datasets from storage file paths
with open(var_call_hndkNQFMfuQK8SaHkLvz5O0L, 'r', encoding='utf-8') as f:
    reviews = json.load(f)
with open(var_call_t0GZFT2c0Y17HavLXvuLx1Pb, 'r', encoding='utf-8') as f:
    books = json.load(f)

rev_df = pd.DataFrame(reviews)
books_df = pd.DataFrame(books)

# Clean ratings
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
rev_df = rev_df.dropna(subset=['rating','purchase_id'])

# Extract numeric suffix
rev_df['id_num'] = rev_df['purchase_id'].astype(str).str.extract(r'(\d+)$')
rev_df['id_num'] = pd.to_numeric(rev_df['id_num'], errors='coerce')
rev_df = rev_df.dropna(subset=['id_num'])
rev_df['id_num'] = rev_df['id_num'].astype(int)

# Book-level average rating
book_avg = rev_df.groupby('id_num')['rating'].mean().reset_index().rename(columns={'rating':'book_avg_rating'})

# Process books
books_df['id_num'] = books_df['book_id'].astype(str).str.extract(r'(\d+)$')
books_df['id_num'] = pd.to_numeric(books_df['id_num'], errors='coerce')
books_df = books_df.dropna(subset=['id_num'])
books_df['id_num'] = books_df['id_num'].astype(int)

# Extract publication year from details
def extract_year(text):
    if not isinstance(text, str):
        return None
    years = re.findall(r'\b(1[0-9]{3}|20[0-2][0-9]|2023)\b', text)
    if years:
        try:
            return int(years[0])
        except:
            return None
    return None

books_df['pub_year'] = books_df['details'].apply(extract_year)

# Merge
merged = pd.merge(book_avg, books_df[['id_num','book_id','title','pub_year']], on='id_num', how='left')
merged = merged.dropna(subset=['pub_year'])
merged['pub_year'] = merged['pub_year'].astype(int)

# Decade
merged['decade_start'] = (merged['pub_year'] // 10) * 10
merged['decade'] = merged['decade_start'].astype(str) + 's'

# Group by decade
group = merged.groupby('decade').agg(
    num_books=('book_id','nunique'),
    avg_rating=('book_avg_rating','mean')
).reset_index()

eligible = group[group['num_books'] >= 10]

if eligible.empty:
    result = None
else:
    # pick highest avg_rating; on tie choose earliest decade_start
    max_avg = eligible['avg_rating'].max()
    tops = eligible[eligible['avg_rating'] == max_avg].copy()
    # compute decade_start as int
    tops['decade_start'] = tops['decade'].str.replace('s','').astype(int)
    top = tops.sort_values('decade_start').iloc[0]
    result = top['decade']

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_gVrjlMDRfW7rZT4TL4wLpz22': ['review'], 'var_call_58BZpGxJ9vOGaH0guXgfeuaF': ['books_info'], 'var_call_CR8z9E9ctk84x7pqzfPltmDI': 'file_storage/call_CR8z9E9ctk84x7pqzfPltmDI.json', 'var_call_t0GZFT2c0Y17HavLXvuLx1Pb': 'file_storage/call_t0GZFT2c0Y17HavLXvuLx1Pb.json', 'var_call_LxotQdGGyzEK4zrTWUGznZAj': None, 'var_call_hndkNQFMfuQK8SaHkLvz5O0L': 'file_storage/call_hndkNQFMfuQK8SaHkLvz5O0L.json'}

exec(code, env_args)
