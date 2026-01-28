code = """import json
import re
import pandas as pd

# Load data from storage-provided JSON file paths
books_path = var_call_03HqTeDs4DKrPFDQwTStfqC0
reviews_path = var_call_RDcfowpRgBHqrtT1r4kJQOJf

with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Create DataFrames
df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# Normalize IDs by extracting numeric suffix
def extract_num(s):
    if pd.isna(s):
        return None
    m = re.search(r"(\d+)", str(s))
    return int(m.group(1)) if m else None

if 'book_id' in df_books.columns:
    df_books['id_num'] = df_books['book_id'].apply(extract_num)
else:
    df_books['id_num'] = None

if 'purchase_id' in df_reviews.columns:
    df_reviews['id_num'] = df_reviews['purchase_id'].apply(extract_num)
else:
    df_reviews['id_num'] = None

# Convert rating to float
if 'rating' in df_reviews.columns:
    df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

# Merge reviews with books on numeric id
df_merged = pd.merge(df_reviews, df_books, on='id_num', how='inner', suffixes=('_rev','_bk'))

# Extract publication year from details using regex for 4-digit years between 1000 and 2023
def extract_year(details):
    if pd.isna(details):
        return None
    # find all 4-digit numbers
    years = re.findall(r"\b(1[0-9]{3}|20[0-2][0-9]|2030)\b", details)
    # If none found with above, fallback to any 4-digit
    if not years:
        years_all = re.findall(r"\b(\d{4})\b", details)
        years = [y for y in years_all if 1000 <= int(y) <= 2023]
    if years:
        try:
            y = int(years[0])
            if 1000 <= y <= 2023:
                return y
        except:
            return None
    return None

# Apply extraction to books dataframe
# Use books details; some merged rows contain details from books
if 'details' in df_merged.columns:
    df_merged['pub_year'] = df_merged['details'].apply(extract_year)
else:
    df_merged['pub_year'] = None

# Keep only rows where pub_year is present
df_merged = df_merged[df_merged['pub_year'].notna()].copy()

# Compute decade label
df_merged['decade'] = (df_merged['pub_year'] // 10 * 10).astype(int)
# Format as e.g., '1990s'
df_merged['decade_label'] = df_merged['decade'].astype(str) + 's'

# For each distinct book (book_id), compute its average rating
# Use book_id from books table
book_avg = df_merged.groupby(['book_id','decade_label'], dropna=False)['rating'].mean().reset_index()
book_avg.rename(columns={'rating':'avg_rating'}, inplace=True)

# Count distinct books per decade and compute decade average of book averages
decade_stats = book_avg.groupby('decade_label').agg(
    books_count=('book_id','nunique'),
    decade_avg_rating=('avg_rating','mean')
).reset_index()

# Filter decades with at least 10 distinct books
decade_stats_filtered = decade_stats[decade_stats['books_count'] >= 10].copy()

# If none meet criteria, prepare a message
if decade_stats_filtered.empty:
    result = {"error": "No decade has at least 10 distinct rated books."}
else:
    # Find decade with highest average rating
    best = decade_stats_filtered.sort_values(['decade_avg_rating','books_count'], ascending=[False,False]).iloc[0]
    result = {
        "decade": best['decade_label'],
        "average_rating": round(float(best['decade_avg_rating']), 4),
        "books_count": int(best['books_count'])
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_6udBt1EGST39VOXA0i28JxoL': ['books_info'], 'var_call_03HqTeDs4DKrPFDQwTStfqC0': 'file_storage/call_03HqTeDs4DKrPFDQwTStfqC0.json', 'var_call_z9wLY9N5qW7zm86lOoEdRrz4': ['review'], 'var_call_RDcfowpRgBHqrtT1r4kJQOJf': 'file_storage/call_RDcfowpRgBHqrtT1r4kJQOJf.json'}

exec(code, env_args)
