code = """import json
import re
import pandas as pd

# Load data from storage-provided file paths
books_path = var_call_qKM35cPEsE9Zq7UcMMxFgDxH
reviews_path = var_call_r7XrC6s4L2uNODJ8nRWr2dam

with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Create DataFrames
df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# Ensure relevant columns exist
if 'book_id' not in df_books.columns or 'details' not in df_books.columns:
    raise ValueError('books data missing required columns')
if 'purchase_id' not in df_reviews.columns or 'rating' not in df_reviews.columns:
    raise ValueError('reviews data missing required columns')

# Extract numeric id from book_id and purchase_id
def extract_num(s):
    if pd.isna(s):
        return None
    m = re.search(r"(\d+)", str(s))
    return int(m.group(1)) if m else None

df_books['book_num'] = df_books['book_id'].apply(extract_num)
df_reviews['purchase_num'] = df_reviews['purchase_id'].apply(extract_num)

# Extract year from details using regex
def extract_year(detail):
    if pd.isna(detail):
        return None
    m = re.search(r"\b(1[0-9]{3}|20[0-9]{2})\b", detail)
    return int(m.group(0)) if m else None

df_books['year'] = df_books['details'].apply(extract_year)

# Drop rows without numeric ids or year where applicable
df_books_clean = df_books.dropna(subset=['book_num']).copy()
df_reviews_clean = df_reviews.dropna(subset=['purchase_num', 'rating']).copy()

# Convert ratings to float
def to_float(x):
    try:
        return float(x)
    except:
        return None

df_reviews_clean['rating_f'] = df_reviews_clean['rating'].apply(to_float)
df_reviews_clean = df_reviews_clean.dropna(subset=['rating_f']).copy()

# Merge reviews to books on numeric id
merged = pd.merge(df_reviews_clean, df_books_clean, left_on='purchase_num', right_on='book_num', how='inner', suffixes=('_rev','_book'))

# Filter to entries with a valid year
merged = merged.dropna(subset=['year']).copy()
merged['year'] = merged['year'].astype(int)
merged['decade_start'] = (merged['year'] // 10) * 10
merged['decade'] = merged['decade_start'].astype(str) + 's'

# Compute average rating per book (distinct book_id)
book_avg = merged.groupby(['book_id','decade'], as_index=False).agg(book_avg_rating=('rating_f','mean'))

# For each decade, consider decades with at least 10 distinct books that have been rated
decade_stats = book_avg.groupby('decade', as_index=False).agg(
    book_count=('book_id','nunique'),
    decade_avg_rating=('book_avg_rating','mean')
)

# Filter decades with at least 10 books
decade_stats_filtered = decade_stats[decade_stats['book_count'] >= 10].copy()

# If no decades meet criteria, prepare None
if decade_stats_filtered.empty:
    result = {'decade': None, 'avg_rating': None, 'book_count': 0}
else:
    # Find decade with highest average rating
    top = decade_stats_filtered.sort_values(['decade_avg_rating','decade'], ascending=[False, True]).iloc[0]
    result = {
        'decade': top['decade'],
        'avg_rating': round(float(top['decade_avg_rating']), 4),
        'book_count': int(top['book_count'])
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_PLFPAmwUWk1s0Ff834zai3s8': ['review'], 'var_call_3mKJ9YNZO3qSvnfTN3BHZq8x': ['books_info'], 'var_call_qKM35cPEsE9Zq7UcMMxFgDxH': 'file_storage/call_qKM35cPEsE9Zq7UcMMxFgDxH.json', 'var_call_r7XrC6s4L2uNODJ8nRWr2dam': 'file_storage/call_r7XrC6s4L2uNODJ8nRWr2dam.json'}

exec(code, env_args)
