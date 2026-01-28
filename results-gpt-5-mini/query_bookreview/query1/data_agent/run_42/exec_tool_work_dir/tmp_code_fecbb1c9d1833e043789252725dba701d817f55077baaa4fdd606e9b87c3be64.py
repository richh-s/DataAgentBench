code = """import pandas as pd
import re
import json

books = pd.read_json(var_call_FukkLQLQdaO9YopesUQhMLDr)
reviews = pd.read_json(var_call_XzGZFNKIb7EjKaCc6zXQZPD5)

# Prepare numeric ids
books['book_num'] = books['book_id'].astype(str).str.extract(r'(\d+)', expand=False)
reviews['purchase_num'] = reviews['purchase_id'].astype(str).str.extract(r'(\d+)', expand=False)

# Normalize ratings
reviews['rating'] = pd.to_numeric(reviews['rating'], errors='coerce')
reviews = reviews.dropna(subset=['rating'])

# Try several regex patterns to extract year
patterns = [r"\b(17|18|19|20)\d{2}\b", r"(\d{4})", r"\b(20\d{2})\b"]

def extract_year_any(s):
    if not isinstance(s, str):
        return None
    # First attempt common pattern
    m = re.search(r"\b(17|18|19|20)\d{2}\b", s)
    if m:
        return int(m.group(0))
    # fallback: find any 4-digit number between 1700 and 2029
    m_all = re.findall(r"\d{4}", s)
    for mm in m_all:
        yy = int(mm)
        if 1700 <= yy <= 2029:
            return yy
    return None

books['pub_year'] = books['details'].apply(extract_year_any)

# Statistics on extraction
total_books = len(books)
books_with_year = books[books['pub_year'].notna()]
count_with_year = len(books_with_year)

# Show some examples
examples_with_year = books_with_year[['book_id','title','pub_year']].head(10).to_dict(orient='records')
examples_without = books[books['pub_year'].isna()][['book_id','title','details']].head(10).to_dict(orient='records')

# Compute per-book average rating by matching numeric ids
# Use purchase_num to map to book_num
reviews_map = reviews.copy()
reviews_map['purchase_num'] = reviews_map['purchase_num']

# Filter reviews to those with a purchase_num present in books
books_nums = set(books['book_num'].dropna())
reviews_map = reviews_map[reviews_map['purchase_num'].isin(books_nums)].copy()

book_avg = reviews_map.groupby('purchase_num', as_index=False).agg({'rating':'mean','purchase_id':'count'})
book_avg.rename(columns={'purchase_num':'book_num','rating':'avg_rating','purchase_id':'num_reviews'}, inplace=True)

# Merge with books
books = books.merge(book_avg, on='book_num', how='left')

# Drop books without avg_rating
books_rated = books.dropna(subset=['avg_rating', 'pub_year']).copy()

# Compute decade label
books_rated['decade_start'] = (books_rated['pub_year'] // 10) * 10
books_rated['decade'] = books_rated['decade_start'].astype(int).astype(str) + 's'

# Compute decade stats
decade_stats = books_rated.groupby('decade').agg(
    num_books=('book_id','nunique'),
    decade_avg_rating=('avg_rating','mean')
).reset_index()

eligible = decade_stats[decade_stats['num_books'] >= 10].copy()

if eligible.empty:
    result = {'decade': None, 'avg_rating': None, 'num_books': 0, 'debug': {'total_books': total_books, 'books_with_year': count_with_year}}
else:
    best = eligible.sort_values(['decade_avg_rating','decade'], ascending=[False, True]).iloc[0]
    result = {'decade': best['decade'], 'avg_rating': round(float(best['decade_avg_rating']),4), 'num_books': int(best['num_books'])}

out = {'result': result, 'examples_with_year': examples_with_year, 'examples_without_year': examples_without, 'decade_stats_all': decade_stats.sort_values('decade').to_dict(orient='records')}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ezqgJidiWrVV9KQClC1SYwJN': ['books_info'], 'var_call_9PtZvw5YFFNmXmEGDeU099yO': ['review'], 'var_call_TXclsw9steCSaXDXnCCBgdZY': 'file_storage/call_TXclsw9steCSaXDXnCCBgdZY.json', 'var_call_XzGZFNKIb7EjKaCc6zXQZPD5': 'file_storage/call_XzGZFNKIb7EjKaCc6zXQZPD5.json', 'var_call_FukkLQLQdaO9YopesUQhMLDr': 'file_storage/call_FukkLQLQdaO9YopesUQhMLDr.json', 'var_call_xohFAnEAGnqtlyeLL6V38yh9': {'decade': None, 'avg_rating': None, 'num_books': 0}, 'var_call_hX6Q8h3AEqNOiGGWGn0f9hLD': {'unique_books_total': 200, 'unique_purchase_ids_in_reviews': 200, 'books_with_numeric_id_count': 200, 'reviews_with_numeric_purchase_count': 1833, 'overlap_numeric_ids_count': 200, 'decade_counts_sample': {}, 'top_purchase_nums_in_reviews_sample': {'196': 194, '8': 190, '3': 146, '178': 118, '186': 80, '20': 42, '10': 40, '145': 36, '190': 34, '154': 29, '148': 29, '48': 27, '5': 25, '158': 24, '95': 23, '62': 22, '165': 22, '99': 20, '72': 19, '89': 18}}}

exec(code, env_args)
