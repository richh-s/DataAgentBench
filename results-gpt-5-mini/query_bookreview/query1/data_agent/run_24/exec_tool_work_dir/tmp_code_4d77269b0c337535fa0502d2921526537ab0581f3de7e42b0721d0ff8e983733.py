code = """import json
import re
import pandas as pd

# Load data from storage file paths provided by previous tool calls
books_path = var_call_k9ovkrj1PGjsNoXc3VPCVhaU
reviews_path = var_call_hOJSgnYdAmhFbg1euaKkiTd3

with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# Normalize types
if 'rating' in df_reviews.columns:
    df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

# Extract numeric id suffix from book_id and purchase_id
def extract_num(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'(\d+)$', s)
    return int(m.group(1)) if m else None

if 'book_id' in df_books.columns:
    df_books['id_num'] = df_books['book_id'].apply(extract_num)
if 'purchase_id' in df_reviews.columns:
    df_reviews['id_num'] = df_reviews['purchase_id'].apply(extract_num)

# Merge on numeric id
merged = pd.merge(df_reviews, df_books, on='id_num', how='inner', suffixes=('_rev','_book'))

# If merge empty, fallback to no-merge

# Extract year from details
import math

def extract_year(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'(?:(?:19|20)\d{2})', s)
    return int(m.group(0)) if m else None

merged['year'] = merged['details'].apply(extract_year)

# Drop rows without year or rating
merged = merged[merged['year'].notna() & merged['rating'].notna()]

# Compute average rating per distinct book (by book_id)
per_book = merged.groupby(['book_id','title','year'], as_index=False).agg({'rating':'mean'})
per_book.rename(columns={'rating':'avg_rating'}, inplace=True)

# Compute decade label
per_book['decade_start'] = (per_book['year'] // 10) * 10
per_book['decade'] = per_book['decade_start'].astype(int).astype(str) + 's'

# Compute per-decade stats
decade_stats = per_book.groupby('decade').agg(
    num_books=('book_id','nunique'),
    decade_avg_rating=('avg_rating','mean')
).reset_index()

# Filter decades with at least 10 distinct books
candidates = decade_stats[decade_stats['num_books'] >= 10]

result = None
if not candidates.empty:
    best = candidates.sort_values(['decade_avg_rating','decade'], ascending=[False, True]).iloc[0]
    result = {
        'decade': best['decade'],
        'avg_rating': round(float(best['decade_avg_rating']), 4),
        'num_books': int(best['num_books'])
    }
else:
    # No decade meets threshold
    result = None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WdE7PvdYf9BmQqEq30uJ7RRf': ['books_info'], 'var_call_evJZr5fpcWpPFshl1eLzjN54': ['review'], 'var_call_k9ovkrj1PGjsNoXc3VPCVhaU': 'file_storage/call_k9ovkrj1PGjsNoXc3VPCVhaU.json', 'var_call_hOJSgnYdAmhFbg1euaKkiTd3': 'file_storage/call_hOJSgnYdAmhFbg1euaKkiTd3.json'}

exec(code, env_args)
