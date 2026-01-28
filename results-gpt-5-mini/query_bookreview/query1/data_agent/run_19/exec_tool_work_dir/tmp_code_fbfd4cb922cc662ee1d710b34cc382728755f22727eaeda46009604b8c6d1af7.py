code = """import json
import pandas as pd
import re

# Load data from storage file paths
with open(var_call_Wv01vezERIxQWQNp3uhDCQDy, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(var_call_4RvMVzQw6ae3RUi3uTmH3BkO, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Create DataFrames
df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# Clean and convert ratings to float
# Some ratings may be strings like '5' or numbers
df_reviews = df_reviews[df_reviews.get('purchase_id').notnull()]

def to_float(x):
    try:
        return float(x)
    except:
        return None

if 'rating' in df_reviews.columns:
    df_reviews['rating'] = df_reviews['rating'].apply(to_float)

# Map purchase_id to book_id by replacing prefix
# e.g., purchaseid_3 -> bookid_3
df_reviews['book_id'] = df_reviews['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)

# Compute per-book average rating (only include reviews with valid ratings)
df_reviews_valid = df_reviews[df_reviews['rating'].notnull()]
book_avg = df_reviews_valid.groupby('book_id', dropna=False)['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})

# Merge with books to get details
merged = pd.merge(book_avg, df_books[['book_id','details']], on='book_id', how='left')

# Extract year from details using regex
def extract_year(text):
    if not isinstance(text, str):
        return None
    # find 4-digit years between 1000 and 2023
    years = re.findall(r'\b(1[0-9]{3}|20[0-2][0-9]|2030)\b', text)
    # Note: regex returns matched strings; if none, try a more permissive search
    if years:
        for y in years:
            try:
                yi = int(y)
                if 1000 <= yi <= 2023:
                    return yi
            except:
                continue
    # fallback: find any 4-digit number
    years_all = re.findall(r'\b(\d{4})\b', text)
    for y in years_all:
        try:
            yi = int(y)
            if 1000 <= yi <= 2023:
                return yi
        except:
            continue
    return None

merged['year'] = merged['details'].apply(extract_year)
# Drop rows without year
merged = merged[merged['year'].notnull()].copy()
merged['year'] = merged['year'].astype(int)
# Compute decade string
merged['decade'] = merged['year'].floordiv(10).mul(10).astype(int).astype(str) + 's'

# For each decade, consider distinct books count and average of book avg ratings
decade_stats = merged.groupby('decade').agg(
    book_count = ('book_id', 'nunique'),
    decade_avg_rating = ('avg_rating', 'mean')
).reset_index()

# Filter decades with at least 10 distinct books
eligible = decade_stats[decade_stats['book_count'] >= 10]

result_decade = None
if not eligible.empty:
    # choose decade with highest decade_avg_rating
    best = eligible.loc[eligible['decade_avg_rating'].idxmax()]
    result_decade = best['decade']

# Prepare output
import json as _json
output = _json.dumps(result_decade)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_1sQwuGiVh9Xaqbw0U8PvXHJS': ['review'], 'var_call_s2vic9F4hCbhlVidy06HXrHS': ['books_info'], 'var_call_Wv01vezERIxQWQNp3uhDCQDy': 'file_storage/call_Wv01vezERIxQWQNp3uhDCQDy.json', 'var_call_4RvMVzQw6ae3RUi3uTmH3BkO': 'file_storage/call_4RvMVzQw6ae3RUi3uTmH3BkO.json'}

exec(code, env_args)
