code = """import json
import pandas as pd
import re

# Load query results from storage file paths
with open(var_call_ahSeu74lplrW2uWVFYFbYKof, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(var_call_t8s9j3CLGS3oQRddFrBguw0a, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Normalize rating to float
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')

# Helper to extract numeric id from book_id or purchase_id
def extract_num_id(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'_(\d+)$', s)
    if m:
        return m.group(1)
    # fallback: find any number
    m2 = re.search(r'(\d+)', s)
    return m2.group(1) if m2 else None

books_df['num_id'] = books_df['book_id'].apply(extract_num_id)
reviews_df['num_id'] = reviews_df['purchase_id'].apply(extract_num_id)

# Create a synthetic book_id in reviews to match books
reviews_df['book_id'] = reviews_df['num_id'].apply(lambda x: f'bookid_{x}' if pd.notnull(x) else None)

# Merge reviews with books on book_id
merged = reviews_df.merge(books_df[['book_id', 'details']], on='book_id', how='left')

# Extract year from details
def extract_year(details):
    if not isinstance(details, str):
        return None
    # find all 4-digit numbers
    years = re.findall(r'\b(1[5-9]\d{2}|20\d{2})\b', details)
    if not years:
        return None
    # years is list of tuples due to groups; flatten
    # re.findall with group returns strings; handle
    for y in years:
        # y may be like '2004' or tuple; ensure string
        ys = y if isinstance(y, str) else (y[0] if isinstance(y, (list, tuple)) else str(y))
        try:
            yi = int(ys)
            if 1500 <= yi <= 2023:
                return yi
        except:
            continue
    return None

merged['year'] = merged['details'].apply(extract_year)

# Drop entries without year or rating
merged = merged[merged['year'].notnull() & merged['rating'].notnull()]
merged['year'] = merged['year'].astype(int)

# compute decade string
merged['decade_start'] = (merged['year'] // 10) * 10
merged['decade'] = merged['decade_start'].astype(str) + 's'

# For each decade, count distinct books that have at least one rating
decade_book_counts = merged.groupby('decade')['book_id'].nunique().reset_index().rename(columns={'book_id':'distinct_books'})

# Compute average rating per decade (across all reviews for books in that decade)
decade_avg = merged.groupby('decade')['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})

decade_stats = pd.merge(decade_avg, decade_book_counts, on='decade')

# Filter decades with at least 10 distinct books
valid_decades = decade_stats[decade_stats['distinct_books'] >= 10]

result = None
if not valid_decades.empty:
    # find decade with highest avg_rating
    best = valid_decades.sort_values(['avg_rating','decade'], ascending=[False, True]).iloc[0]
    result = best['decade']
else:
    result = None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_25XrTT1v8MA76LlhO9Ah0Qpu': ['review'], 'var_call_CaaMHIphba5mhsgrjOW70AAl': ['books_info'], 'var_call_ahSeu74lplrW2uWVFYFbYKof': 'file_storage/call_ahSeu74lplrW2uWVFYFbYKof.json', 'var_call_t8s9j3CLGS3oQRddFrBguw0a': 'file_storage/call_t8s9j3CLGS3oQRddFrBguw0a.json'}

exec(code, env_args)
