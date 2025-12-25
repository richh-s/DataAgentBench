code = """import json, re, pandas as pd
from pathlib import Path

# Load full books_info details
path_books = Path(var_call_5zVzyU5npQkiqgmKvgj7mQBa)
books = json.loads(path_books.read_text())

# Load full reviews
path_reviews = Path(var_call_DRvCYMzp7V6HsrljFtikSKou)
reviews = json.loads(path_reviews.read_text())

# Build DataFrames
books_df = pd.DataFrame(books)[['book_id','details']]
rev_df = pd.DataFrame(reviews)[['purchase_id','rating']]

# Extract publication year from details text using regex
# Look for patterns like 'on January 1, 2004' or 'on May 18, 2014' etc.
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

def extract_year(text):
    if not isinstance(text,str):
        return None
    years = year_pattern.findall(text)
    # findall with groups returns tuples ("19","97"), so re-run with finditer
    yrs = re.findall(r'(19|20)\d{2}', text)
    # But that still gives '1997' etc; simplest: another pattern
    years2 = re.findall(r'\b(?:19|20)\d{2}\b', text)
    return int(years2[0]) if years2 else None

books_df['year'] = books_df['details'].apply(extract_year)

# Drop rows without year
books_df = books_df.dropna(subset=['year'])
books_df['year'] = books_df['year'].astype(int)

# Compute decade label like '1980s'
books_df['decade_start'] = (books_df['year'] // 10) * 10
books_df['decade'] = books_df['decade_start'].astype(str) + 's'

# Join reviews to books on purchase_id == book_id
rev_df['rating'] = rev_df['rating'].astype(float)
merged = rev_df.merge(books_df[['book_id','decade']], left_on='purchase_id', right_on='book_id', how='inner')

# For each book_id, compute its average rating
book_avg = merged.groupby(['book_id','decade'])['rating'].mean().reset_index(name='book_avg_rating')

# For each decade, filter decades with at least 10 distinct books that have been rated
decade_stats = book_avg.groupby('decade').agg(num_books=('book_id','nunique'), avg_rating=('book_avg_rating','mean')).reset_index()

eligible = decade_stats[decade_stats['num_books'] >= 10]

if eligible.empty:
    result = None
else:
    # Get decade with highest avg_rating; in tie, choose earliest decade (by decade_start)
    # Need decade_start back
    eligible['decade_start'] = eligible['decade'].str.slice(0,4).astype(int)
    max_rating = eligible['avg_rating'].max()
    top = eligible[eligible['avg_rating'] == max_rating].sort_values('decade_start').iloc[0]
    result = top['decade']

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_5zVzyU5npQkiqgmKvgj7mQBa': 'file_storage/call_5zVzyU5npQkiqgmKvgj7mQBa.json', 'var_call_DdqoSvPex3aTEESwVRP22KwT': ['books_info'], 'var_call_2QYGO7orgosunGHejPWEzt6y': ['review'], 'var_call_DRvCYMzp7V6HsrljFtikSKou': 'file_storage/call_DRvCYMzp7V6HsrljFtikSKou.json'}

exec(code, env_args)
