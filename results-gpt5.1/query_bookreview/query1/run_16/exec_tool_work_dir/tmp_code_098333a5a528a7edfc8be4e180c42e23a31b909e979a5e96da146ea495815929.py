code = """import json, pandas as pd

# Load full books_info result
with open(var_call_JAr2AtbtT6LhBJEPdjPJh03U, 'r') as f:
    books = json.load(f)

# Convert to DataFrame
books_df = pd.DataFrame(books)

# Extract publication year from details using simple heuristics
import re

def extract_year(details):
    if not isinstance(details, str):
        return None
    # Look for patterns like 'January 1, 2004' or 'May 20, 1996' or 'in 2004'
    # First, search for 4-digit years between 1500 and 2100
    years = re.findall(r'(1[5-9]\d{2}|20\d{2}|2100)', details)
    if not years:
        return None
    # Heuristic: earliest year is likely original publication
    years_int = sorted(int(y) for y in years)
    return years_int[0]

books_df['year'] = books_df['details'].apply(extract_year)
books_df['decade'] = books_df['year'].apply(lambda y: None if pd.isna(y) else int(y//10*10))

# Load reviews
with open(var_call_ojJvGhY7pQfqUtLwKZl656po, 'r') as f:
    reviews = json.load(f)

reviews_df = pd.DataFrame(reviews)

# ratings to float
reviews_df['rating'] = reviews_df['rating'].astype(float)

# Join on purchase_id = book_id
merged = pd.merge(reviews_df, books_df[['book_id','decade']], left_on='purchase_id', right_on='book_id', how='inner')

# Filter out rows without decade
merged = merged.dropna(subset=['decade'])

# Compute per-book average rating
book_avg = merged.groupby(['book_id','decade'])['rating'].mean().reset_index(name='book_avg_rating')

# Now compute per-decade stats, counting distinct books and average of book averages
decade_stats = book_avg.groupby('decade').agg(distinct_books=('book_id','nunique'), avg_rating=('book_avg_rating','mean')).reset_index()

# Filter decades with at least 10 distinct books
eligible = decade_stats[decade_stats['distinct_books'] >= 10]

if eligible.empty:
    result = None
else:
    best_row = eligible.sort_values(['avg_rating','decade'], ascending=[False, True]).iloc[0]
    decade_int = int(best_row['decade'])
    decade_str = f"{decade_int}s"
    result = {'decade': decade_str, 'average_rating': round(float(best_row['avg_rating']), 3), 'distinct_books': int(best_row['distinct_books'])}

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_JAr2AtbtT6LhBJEPdjPJh03U': 'file_storage/call_JAr2AtbtT6LhBJEPdjPJh03U.json', 'var_call_UkdUMXRfYMCM302eebnrvesE': [{'name': 'review'}], 'var_call_ojJvGhY7pQfqUtLwKZl656po': 'file_storage/call_ojJvGhY7pQfqUtLwKZl656po.json'}

exec(code, env_args)
