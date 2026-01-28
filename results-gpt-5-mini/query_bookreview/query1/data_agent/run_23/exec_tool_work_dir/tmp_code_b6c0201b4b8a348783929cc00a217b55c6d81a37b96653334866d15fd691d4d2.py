code = """import json, re
import pandas as pd

# Load data from storage file paths provided by previous tool calls
with open(var_call_zGUgjy4lWENiSbAfnRjr3yQp, 'r') as f:
    reviews = json.load(f)
with open(var_call_WAeKRz4UH0REUSEjkdb7jvw8, 'r') as f:
    books = json.load(f)

# Create DataFrames
df_rev = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

# Clean and convert ratings
df_rev['rating'] = pd.to_numeric(df_rev.get('rating'), errors='coerce')

# Extract numeric ids from purchase_id and book_id for fuzzy join
df_rev['num_id'] = df_rev.get('purchase_id', '').astype(str).str.extract(r'(\d+)')[0]
df_books['num_id'] = df_books.get('book_id', '').astype(str).str.extract(r'(\d+)')[0]

# Extract publication year from details using regex
def extract_year(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'(1[7-9]\d{2}|20\d{2})', s)
    return int(m.group(0)) if m else None

# Some books may have missing details; handle gracefully
df_books['year'] = df_books.get('details').apply(extract_year)

# Merge reviews with books on the numeric id
df = pd.merge(df_rev, df_books, on='num_id', how='inner', suffixes=('_rev', '_book'))

# Keep only rows with valid year and rating
df = df[df['year'].notna() & df['rating'].notna()]

# Compute per-book average rating (group by book_id/title/year)
book_avg = df.groupby(['book_id', 'title', 'year'], dropna=False).agg(avg_rating=('rating', 'mean')).reset_index()

# Compute decade label
book_avg['decade'] = (book_avg['year'] // 10 * 10).astype(int).astype(str) + 's'

# For each decade, compute number of distinct books and mean of per-book averages
decade_stats = book_avg.groupby('decade').agg(num_books=('book_id', 'nunique'), avg_of_avgs=('avg_rating', 'mean')).reset_index()

# Filter decades with at least 10 distinct books
decade_stats = decade_stats[decade_stats['num_books'] >= 10]

if not decade_stats.empty:
    # Select decade with highest average (break ties by alphabetical decade)
    best_row = decade_stats.sort_values(['avg_of_avgs', 'decade'], ascending=[False, True]).iloc[0]
    result = best_row['decade']
else:
    result = None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_mUmJhpMJzNTwBC5lUbdifyCW': ['review'], 'var_call_vSTyvE3eZKN7C17t1cVodx4Y': ['books_info'], 'var_call_zGUgjy4lWENiSbAfnRjr3yQp': 'file_storage/call_zGUgjy4lWENiSbAfnRjr3yQp.json', 'var_call_WAeKRz4UH0REUSEjkdb7jvw8': 'file_storage/call_WAeKRz4UH0REUSEjkdb7jvw8.json'}

exec(code, env_args)
