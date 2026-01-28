code = """import json, re
import pandas as pd

# Load data from storage-provided file paths
with open(var_call_y1Tx7d5jbxthUjoKbarSZn6t, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(var_call_7WJPf7muozLZut10OuOdjvFo, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Create DataFrames
df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# Extract numeric IDs from book_id and purchase_id
import re

def extract_num(s):
    if pd.isna(s):
        return None
    m = re.search(r"(\d+)", str(s))
    return int(m.group(1)) if m else None

df_books['num_id'] = df_books['book_id'].apply(extract_num)
df_reviews['num_id'] = df_reviews['purchase_id'].apply(extract_num)

# Extract year from details (first 4-digit year between 1000 and 2029)
def extract_year(s):
    if pd.isna(s):
        return None
    m = re.search(r"\b(1[0-9]{3}|20[0-2][0-9])\b", str(s))
    return int(m.group(0)) if m else None

# Some details may be missing; extract year
if 'details' in df_books.columns:
    df_books['year'] = df_books['details'].apply(extract_year)
else:
    df_books['year'] = None

# Merge reviews with books on numeric id
# Drop reviews or books without numeric id
df_books_clean = df_books.dropna(subset=['num_id'])
df_reviews_clean = df_reviews.dropna(subset=['num_id'])

# Convert rating to numeric
if 'rating' in df_reviews_clean.columns:
    df_reviews_clean['rating'] = pd.to_numeric(df_reviews_clean['rating'], errors='coerce')
else:
    df_reviews_clean['rating'] = None

# Merge
df_merged = pd.merge(df_reviews_clean, df_books_clean, on='num_id', how='inner', suffixes=('_rev','_book'))

# Keep rows with valid year and rating
df_merged = df_merged.dropna(subset=['year','rating'])

# Compute decade label
df_merged['decade_start'] = (df_merged['year']//10)*10
df_merged['decade'] = df_merged['decade_start'].astype(int).astype(str) + 's'

# For each decade, compute distinct book count and average rating (across all reviews)
agg = df_merged.groupby('decade').agg(
    book_count = ('book_id', lambda x: x.nunique()),
    avg_rating = ('rating', 'mean')
).reset_index()

# Filter decades with at least 10 distinct books
agg_filtered = agg[agg['book_count'] >= 10]

result = None
if agg_filtered.empty:
    result = {"decade": None, "average_rating": None, "book_count": 0}
else:
    # Find decade with highest average rating
    best = agg_filtered.sort_values(['avg_rating','book_count'], ascending=[False, False]).iloc[0]
    result = {
        "decade": best['decade'],
        "average_rating": round(float(best['avg_rating']), 4),
        "book_count": int(best['book_count'])
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_y1Tx7d5jbxthUjoKbarSZn6t': 'file_storage/call_y1Tx7d5jbxthUjoKbarSZn6t.json', 'var_call_AoGVRqzQ10M2wVo911ReA77F': ['review'], 'var_call_7WJPf7muozLZut10OuOdjvFo': 'file_storage/call_7WJPf7muozLZut10OuOdjvFo.json'}

exec(code, env_args)
