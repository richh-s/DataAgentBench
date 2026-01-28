code = """import json
import pandas as pd
import re

# Load the stored query results from files (paths are in the provided variables)
with open(var_call_baCgn49jPHxnQJK16IQjX61X, 'r') as f:
    reviews = json.load(f)
with open(var_call_r5T3DCItRxZawqK9uYbTtAyu, 'r') as f:
    books = json.load(f)

# Create DataFrames
rev_df = pd.DataFrame(reviews)
books_df = pd.DataFrame(books)

# Clean and convert ratings
rev_df = rev_df[['purchase_id', 'rating']].copy()
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
rev_df = rev_df.dropna(subset=['rating'])

# Map purchase_id to book_id by extracting numeric part
def purchase_to_book(pid):
    m = re.search(r"(\d+)", str(pid))
    if m:
        return f"bookid_{m.group(1)}"
    return None

rev_df['book_id'] = rev_df['purchase_id'].apply(purchase_to_book)
rev_df = rev_df.dropna(subset=['book_id'])

# Extract publication year from books details
def extract_year(details):
    if not isinstance(details, str):
        return None
    # find all 4-digit years between 1000 and 2023
    m = re.search(r"\b(1[0-9]{3}|20[0-2][0-9]|2023)\b", details)
    if m:
        try:
            y = int(m.group(0))
            return y
        except:
            return None
    return None

books_df['year'] = books_df['details'].apply(extract_year)
books_df = books_df.dropna(subset=['year'])
books_df['year'] = books_df['year'].astype(int)
books_df['decade'] = (books_df['year'] // 10 * 10).astype(int).astype(str) + 's'

# Merge reviews with books on book_id
merged = pd.merge(rev_df, books_df[['book_id','decade']], on='book_id', how='inner')

# Compute average rating per book
book_avg = merged.groupby('book_id', as_index=False)['rating'].mean()
# attach decade for each book
book_avg = pd.merge(book_avg, books_df[['book_id','decade']], on='book_id', how='left')

# For each decade, compute number of distinct books and average of book averages
decade_stats = book_avg.groupby('decade').agg(
    num_books=('book_id','nunique'),
    avg_rating=('rating','mean')
).reset_index()

# Filter decades with at least 10 distinct books
decade_stats_filtered = decade_stats[decade_stats['num_books'] >= 10]

# If none meet criteria, return None
if decade_stats_filtered.empty:
    result = {"decade": None, "average_rating": None, "num_books": 0}
else:
    # Find decade with highest average_rating (tie-breaker: highest num_books, then alphabetically)
    best = decade_stats_filtered.sort_values(by=['avg_rating','num_books','decade'], ascending=[False, False, True]).iloc[0]
    result = {"decade": best['decade'], "average_rating": round(float(best['avg_rating']), 4), "num_books": int(best['num_books'])}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rq6McKRItXFHwYvE32VIxknB': ['review'], 'var_call_ZbTtSFT3RuKciYn44AstiVVR': ['books_info'], 'var_call_baCgn49jPHxnQJK16IQjX61X': 'file_storage/call_baCgn49jPHxnQJK16IQjX61X.json', 'var_call_r5T3DCItRxZawqK9uYbTtAyu': 'file_storage/call_r5T3DCItRxZawqK9uYbTtAyu.json'}

exec(code, env_args)
