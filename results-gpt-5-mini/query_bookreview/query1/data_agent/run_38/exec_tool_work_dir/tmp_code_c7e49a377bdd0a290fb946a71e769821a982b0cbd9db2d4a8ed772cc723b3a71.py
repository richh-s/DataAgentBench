code = """import json
import pandas as pd
import re

# Load data from storage files
books_path = var_call_mrYdlboFzl9G57ytTacnGU7G
reviews_path = var_call_6NoSNH05X8sJgbkbVj7l2nj3

with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Extract year from details using regex (first 4-digit year between 1000 and 2099)
def extract_year(text):
    if not isinstance(text, str):
        return None
    m = re.search(r"\b(1[0-9]{3}|20[0-9]{2})\b", text)
    if m:
        try:
            return int(m.group(0))
        except:
            return None
    return None

books_df['year'] = books_df['details'].apply(extract_year)
books_df = books_df.dropna(subset=['year'])
books_df['year'] = books_df['year'].astype(int)
books_df['decade'] = books_df['year'].apply(lambda y: f"{(y//10)*10}s")

# Prepare reviews
# Convert rating to float
reviews_df['rating'] = reviews_df['rating'].astype(float)
# Map purchase_id to book_id by replacing prefix
reviews_df['book_id'] = reviews_df['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_')

# Join reviews with books to get publication decades
merged = reviews_df.merge(books_df[['book_id', 'decade']], on='book_id', how='inner')

# Compute per-book average rating
book_avg = merged.groupby('book_id', as_index=False)['rating'].mean().rename(columns={'rating': 'book_avg_rating'})
# Attach decade to book_avg
book_decade = merged[['book_id', 'decade']].drop_duplicates(subset=['book_id'])
book_stats = book_avg.merge(book_decade, on='book_id', how='left')

# Compute decade-level stats: number of distinct books and average of book averages
decade_stats = book_stats.groupby('decade').agg(num_books=('book_id', 'nunique'), decade_avg_rating=('book_avg_rating', 'mean')).reset_index()
# Filter decades with at least 10 distinct books
decade_stats_filtered = decade_stats[decade_stats['num_books'] >= 10]

result = None
if len(decade_stats_filtered) > 0:
    # Find decade with highest average rating
    top = decade_stats_filtered.sort_values(['decade_avg_rating', 'decade'], ascending=[False, True]).iloc[0]
    result = {
        'decade': top['decade'],
        'avg_rating': round(float(top['decade_avg_rating']), 4),
        'num_books': int(top['num_books'])
    }
else:
    result = {'decade': None, 'avg_rating': None, 'num_books': 0}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GjNzoWQnRvyKwNg6LbF4sB18': ['review'], 'var_call_VOIuBFFiaaROCAaHKQDN6wCg': ['books_info'], 'var_call_quFFQMpcDMVNXSP15SxsDcSJ': 'file_storage/call_quFFQMpcDMVNXSP15SxsDcSJ.json', 'var_call_6NoSNH05X8sJgbkbVj7l2nj3': 'file_storage/call_6NoSNH05X8sJgbkbVj7l2nj3.json', 'var_call_mrYdlboFzl9G57ytTacnGU7G': 'file_storage/call_mrYdlboFzl9G57ytTacnGU7G.json'}

exec(code, env_args)
