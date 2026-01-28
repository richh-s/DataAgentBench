code = """import json
import pandas as pd
import re

# Load tool results from storage file paths
with open(var_call_clwW1HpxqxlCKDXJvn9Iim9W, 'r') as f:
    reviews_data = json.load(f)
with open(var_call_mC9eh9kdqR7TFrzmoKhf7oa0, 'r') as f:
    books_data = json.load(f)

rv = pd.DataFrame(reviews_data)
bk = pd.DataFrame(books_data)

# Normalize and convert types
rv['avg_rating'] = pd.to_numeric(rv['avg_rating'], errors='coerce')
rv['purchase_id'] = rv['purchase_id'].astype(str)
rv['book_id'] = rv['purchase_id'].str.replace('purchaseid_', 'bookid_', regex=False)

# Function to extract first plausible year from details
year_re = re.compile(r"\b(1[0-9]{3}|20[0-9]{2})\b")

def extract_year(text):
    if not isinstance(text, str):
        return None
    matches = year_re.findall(text)
    for m in matches:
        try:
            y = int(m)
            if 1000 <= y <= 2023:
                return y
        except:
            continue
    return None

bk['year'] = bk['details'].apply(extract_year)

# Merge reviews avg per purchase (book) with books info
merged = pd.merge(bk, rv[['book_id', 'avg_rating']], on='book_id', how='inner')

# Keep only entries with a valid year and valid avg_rating
merged = merged[merged['year'].notna() & merged['avg_rating'].notna()].copy()
merged['year'] = merged['year'].astype(int)

# For each distinct book, keep its avg_rating and year (some duplicates shouldn't exist but ensure uniqueness)
books_unique = merged.drop_duplicates(subset=['book_id'])[['book_id','title','year','avg_rating']].copy()

# Compute decade label
books_unique['decade_start'] = (books_unique['year'] // 10) * 10
books_unique['decade'] = books_unique['decade_start'].astype(int).astype(str) + 's'

# Group by decade, compute count of distinct books and average of avg_rating (average across books)
decade_stats = books_unique.groupby('decade').agg(
    book_count=('book_id','nunique'),
    avg_rating_by_book=('avg_rating','mean')
).reset_index()

# Filter decades with at least 10 distinct books
eligible = decade_stats[decade_stats['book_count'] >= 10].copy()

result_decade = None
if not eligible.empty:
    best = eligible.sort_values(['avg_rating_by_book','decade'], ascending=[False, True]).iloc[0]
    result_decade = best['decade']
else:
    result_decade = None

import json
print("__RESULT__:")
print(json.dumps(result_decade))"""

env_args = {'var_call_L3tZ220n99FgcRPeZvbhSpxY': ['review'], 'var_call_xqroN816bvY3rq0PLmDfvm3h': ['books_info'], 'var_call_clwW1HpxqxlCKDXJvn9Iim9W': 'file_storage/call_clwW1HpxqxlCKDXJvn9Iim9W.json', 'var_call_mC9eh9kdqR7TFrzmoKhf7oa0': 'file_storage/call_mC9eh9kdqR7TFrzmoKhf7oa0.json'}

exec(code, env_args)
