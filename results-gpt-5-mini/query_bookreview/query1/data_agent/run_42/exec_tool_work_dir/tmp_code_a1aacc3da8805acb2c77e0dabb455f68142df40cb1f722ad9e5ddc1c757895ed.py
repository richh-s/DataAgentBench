code = """import pandas as pd
import re
import json

# Load data from the stored JSON files
books = pd.read_json(var_call_FukkLQLQdaO9YopesUQhMLDr)
reviews = pd.read_json(var_call_XzGZFNKIb7EjKaCc6zXQZPD5)

# Normalize ratings to numeric
reviews = reviews.dropna(subset=['rating', 'purchase_id']).copy()
# Some ratings may be strings
reviews['rating'] = pd.to_numeric(reviews['rating'], errors='coerce')
reviews = reviews.dropna(subset=['rating'])

# Map purchase_id to book_id by extracting digits and prefixing 'bookid_'
def purchase_to_bookid(pid):
    m = re.search(r"(\d+)", str(pid))
    return f"bookid_{m.group(1)}" if m else None

reviews['book_id'] = reviews['purchase_id'].apply(purchase_to_bookid)

# Extract publication year from books.details using regex
def extract_year(details):
    if not isinstance(details, str):
        return None
    m = re.search(r"\b(17|18|19|20)\d{2}\b", details)
    if m:
        return int(m.group(0))
    return None

books['pub_year'] = books['details'].apply(extract_year)
# Drop rows without book_id or pub_year
books = books.dropna(subset=['book_id', 'pub_year']).copy()

# Compute per-book average rating from reviews
book_avg = reviews.groupby('book_id', as_index=False).agg({'rating': 'mean'})
book_avg.rename(columns={'rating': 'avg_rating'}, inplace=True)

# Join books and book_avg on book_id
books_with_ratings = pd.merge(books, book_avg, on='book_id', how='inner')

# Compute decade label
books_with_ratings['decade_start'] = (books_with_ratings['pub_year'] // 10) * 10
books_with_ratings['decade'] = books_with_ratings['decade_start'].astype(int).astype(str) + 's'

# For each decade, compute number of distinct books and average of per-book average ratings
decade_stats = books_with_ratings.groupby('decade').agg(
    num_books=('book_id', 'nunique'),
    decade_avg_rating=('avg_rating', 'mean')
).reset_index()

# Filter decades with at least 10 distinct books
eligible = decade_stats[decade_stats['num_books'] >= 10].copy()

# If no eligible decades, prepare a message
if eligible.empty:
    result = {"decade": None, "avg_rating": None, "num_books": 0}
else:
    # Find decade with highest average rating
    best = eligible.sort_values(['decade_avg_rating', 'decade'], ascending=[False, True]).iloc[0]
    result = {
        "decade": best['decade'],
        "avg_rating": round(float(best['decade_avg_rating']), 4),
        "num_books": int(best['num_books'])
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ezqgJidiWrVV9KQClC1SYwJN': ['books_info'], 'var_call_9PtZvw5YFFNmXmEGDeU099yO': ['review'], 'var_call_TXclsw9steCSaXDXnCCBgdZY': 'file_storage/call_TXclsw9steCSaXDXnCCBgdZY.json', 'var_call_XzGZFNKIb7EjKaCc6zXQZPD5': 'file_storage/call_XzGZFNKIb7EjKaCc6zXQZPD5.json', 'var_call_FukkLQLQdaO9YopesUQhMLDr': 'file_storage/call_FukkLQLQdaO9YopesUQhMLDr.json'}

exec(code, env_args)
