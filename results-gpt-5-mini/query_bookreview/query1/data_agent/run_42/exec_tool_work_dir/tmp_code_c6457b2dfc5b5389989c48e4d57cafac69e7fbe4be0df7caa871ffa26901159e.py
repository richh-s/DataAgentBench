code = """import pandas as pd
import re
import json

books = pd.read_json(var_call_FukkLQLQdaO9YopesUQhMLDr)
reviews = pd.read_json(var_call_XzGZFNKIb7EjKaCc6zXQZPD5)

# Basic counts
unique_books = books['book_id'].nunique()
unique_reviews_books = reviews['purchase_id'].nunique()

# Extract book numeric id from book_id and purchase_id
books['book_num'] = books['book_id'].astype(str).str.extract(r'(\d+)', expand=False)
reviews['purchase_num'] = reviews['purchase_id'].astype(str).str.extract(r'(\d+)', expand=False)

# Counts of numeric ids
num_books_with_num = books['book_num'].notna().sum()
num_reviews_with_num = reviews['purchase_num'].notna().sum()

# Join on numeric id
books_num = books.copy()
books_num['book_num'] = books_num['book_num']
reviews_num = reviews.copy()
reviews_num['purchase_num'] = reviews_num['purchase_num']

# Compute overlap
overlap_nums = set(books_num['book_num'].dropna().unique()) & set(reviews_num['purchase_num'].dropna().unique())
overlap_count = len(overlap_nums)

# Distribution of books by decade (using extract year heuristic)
def extract_year(details):
    m = re.search(r"\b(17|18|19|20)\d{2}\b", str(details))
    return int(m.group(0)) if m else None

books['pub_year'] = books['details'].apply(extract_year)
books_with_year = books[books['pub_year'].notna()]

decade_counts = (books_with_year['pub_year'] // 10 * 10).value_counts().sort_index().to_dict()

# Top 10 most common purchase_num values in reviews
top_purchase_nums = reviews['purchase_num'].value_counts().head(20).to_dict()

result = {
    'unique_books_total': int(unique_books),
    'unique_purchase_ids_in_reviews': int(unique_reviews_books),
    'books_with_numeric_id_count': int(num_books_with_num),
    'reviews_with_numeric_purchase_count': int(num_reviews_with_num),
    'overlap_numeric_ids_count': int(overlap_count),
    'decade_counts_sample': {str(k): int(v) for k,v in sorted(decade_counts.items())},
    'top_purchase_nums_in_reviews_sample': {str(k): int(v) for k,v in top_purchase_nums.items()}
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ezqgJidiWrVV9KQClC1SYwJN': ['books_info'], 'var_call_9PtZvw5YFFNmXmEGDeU099yO': ['review'], 'var_call_TXclsw9steCSaXDXnCCBgdZY': 'file_storage/call_TXclsw9steCSaXDXnCCBgdZY.json', 'var_call_XzGZFNKIb7EjKaCc6zXQZPD5': 'file_storage/call_XzGZFNKIb7EjKaCc6zXQZPD5.json', 'var_call_FukkLQLQdaO9YopesUQhMLDr': 'file_storage/call_FukkLQLQdaO9YopesUQhMLDr.json', 'var_call_xohFAnEAGnqtlyeLL6V38yh9': {'decade': None, 'avg_rating': None, 'num_books': 0}}

exec(code, env_args)
