code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths or variables
books_path = var_call_HnUNYh2bLIdj7xB4bSETVDoS
reviews_path = var_call_Z81emQCw0hZuC39YvsPN8beP

with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# Normalize reviews rating to numeric
if 'rating' in df_reviews.columns:
    df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

# Normalize purchase_id to book_id by replacing prefix
if 'purchase_id' in df_reviews.columns:
    df_reviews['book_id'] = df_reviews['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)

# Extract year from details in books
year_re = re.compile(r"\b(1[0-9]{3}|20[0-9]{2})\b")

def extract_year(detail):
    if not isinstance(detail, str):
        return None
    m = year_re.search(detail)
    if m:
        try:
            y = int(m.group(0))
            return y
        except:
            return None
    return None

if 'details' in df_books.columns:
    df_books['year'] = df_books['details'].apply(extract_year)
else:
    df_books['year'] = None

# Drop books without year
df_books = df_books[df_books['year'].notna()].copy()

# Compute decade string
df_books['decade'] = df_books['year'].astype(int).floordiv(10).mul(10).astype(int).astype(str) + 's'

# Merge reviews with books on book_id
merged = pd.merge(df_reviews, df_books, on='book_id', how='inner')

# Compute mean rating per book
book_means = merged.groupby('book_id', as_index=False)['rating'].mean()
# Attach decade info
book_means = pd.merge(book_means, df_books[['book_id','decade']], on='book_id', how='left')

# Compute per-decade stats: number of distinct books and average of book means
decade_stats = book_means.groupby('decade').agg(book_count=('book_id','nunique'), avg_rating=('rating','mean')).reset_index()

# Filter decades with at least 10 distinct books
decade_stats_filtered = decade_stats[decade_stats['book_count'] >= 10].copy()

# If none meet criteria, return None
if decade_stats_filtered.empty:
    result = None
else:
    # Find decade with highest average rating
    top = decade_stats_filtered.sort_values(['avg_rating','decade'], ascending=[False, True]).iloc[0]
    result = top['decade']

# Print result in required format as a JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_xBQpKWODUVDAImguaCDS628l': ['review'], 'var_call_2gVleOlCtP1WYl4ysXkC8iM6': ['books_info'], 'var_call_HnUNYh2bLIdj7xB4bSETVDoS': 'file_storage/call_HnUNYh2bLIdj7xB4bSETVDoS.json', 'var_call_Z81emQCw0hZuC39YvsPN8beP': 'file_storage/call_Z81emQCw0hZuC39YvsPN8beP.json'}

exec(code, env_args)
