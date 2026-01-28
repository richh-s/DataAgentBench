code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_cJG0WNqxf3XU1J9jW3V3joUy, 'r') as f:
    books = json.load(f)
with open(var_call_a6luheMSxRTXMqOXulAgYxeK, 'r') as f:
    reviews = json.load(f)

# Create dataframes
df_books = pd.DataFrame(books)
if 'details' not in df_books.columns:
    df_books['details'] = None

# Extract year from 'details' using regex
def extract_year(s):
    if not isinstance(s, str):
        return None
    m = re.search(r"(17|18|19|20)\d{2}", s)
    if m:
        try:
            return int(m.group(0))
        except:
            return None
    return None

df_books['year'] = df_books['details'].apply(extract_year)
# Drop books without a detected year
df_books = df_books[df_books['year'].notnull()].copy()
if df_books.empty:
    result = {"decade": None, "avg_rating": None, "book_count": 0}
else:
    df_books['decade'] = df_books['year'].apply(lambda y: f"{int(y)//10*10}s")

    df_reviews = pd.DataFrame(reviews)
    # Keep only relevant columns
    df_reviews = df_reviews[[c for c in ['purchase_id','rating'] if c in df_reviews.columns]].copy()
    # Coerce rating to numeric
    df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')
    df_reviews = df_reviews[df_reviews['rating'].notnull()].copy()
    # Map purchase_id -> book_id
    df_reviews['book_id'] = df_reviews['purchase_id'].astype(str).str.replace('purchaseid_','bookid_', regex=False)

    # Merge reviews with books to get decades
    merged = pd.merge(df_reviews, df_books[['book_id','decade']], on='book_id', how='inner')

    if merged.empty:
        result = {"decade": None, "avg_rating": None, "book_count": 0}
    else:
        # Compute per-book average rating
        book_avg = merged.groupby(['book_id','decade'], as_index=False).agg({'rating':'mean'})
        # Compute per-decade average of per-book averages and count of distinct books
        decade_stats = book_avg.groupby('decade').agg(avg_rating=('rating','mean'), book_count=('book_id','nunique')).reset_index()
        # Filter decades with at least 10 distinct books
        decade_stats = decade_stats[decade_stats['book_count'] >= 10].copy()
        if decade_stats.empty:
            result = {"decade": None, "avg_rating": None, "book_count": 0}
        else:
            # Find decade with highest average rating
            best = decade_stats.sort_values(['avg_rating','book_count'], ascending=[False,False]).iloc[0]
            result = {"decade": best['decade'], "avg_rating": round(float(best['avg_rating']), 4), "book_count": int(best['book_count'])}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_V5evvePOxVOJq1Wq8Gfwy7wV': ['review'], 'var_call_qqVWWtOkeoQRPzJGpnhEOz1K': ['books_info'], 'var_call_cJG0WNqxf3XU1J9jW3V3joUy': 'file_storage/call_cJG0WNqxf3XU1J9jW3V3joUy.json', 'var_call_a6luheMSxRTXMqOXulAgYxeK': 'file_storage/call_a6luheMSxRTXMqOXulAgYxeK.json'}

exec(code, env_args)
