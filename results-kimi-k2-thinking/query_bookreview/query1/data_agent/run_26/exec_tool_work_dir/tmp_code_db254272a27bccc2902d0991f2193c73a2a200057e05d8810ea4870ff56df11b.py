code = """import json, re, pandas as pd, os

books_path = var_functions.query_db:22
reviews_path = var_functions.query_db:5

# Load data from files
if 'json' in str(books_path):
    with open(books_path) as f:
        books_df = pd.DataFrame(json.load(f))
else:
    books_df = pd.DataFrame(books_path)

if 'json' in str(reviews_path):
    with open(reviews_path) as f:
        reviews_df = pd.DataFrame(json.load(f))
else:
    reviews_df = pd.DataFrame(reviews_path)

print('Shape books:', books_df.shape, 'Shape reviews:', reviews_df.shape)

# Extract year
def extract_year(details):
    if not details or pd.isna(details):
        return None
    patterns = [
        r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})',
        r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b',
    ]
    for pat in patterns:
        m = re.search(pat, str(details))
        if m:
            year = int(m.groups()[-1])
            if 1900 <= year <= 2025:
                return year
    return None

# Add decade column
books_df['publication_year'] = books_df['details'].apply(extract_year)
books_df['decade'] = books_df['publication_year'].apply(lambda x: f'{x//10*10}s' if pd.notna(x) else None)

print('Books with year:', books_df['decade'].notna().sum())

# Merge with reviews
merged = reviews_df.merge(books_df[['book_id', 'decade', 'publication_year']], left_on='purchase_id', right_on='book_id', how='inner')

print('Merged reviews with pub date:', merged.shape[0])

# Filter decades with >= 10 distinct books
decade_stats = merged.groupby('decade').agg({'purchase_id': ['nunique'], 'rating': ['count', 'mean']}).reset_index()
decade_stats.columns = ['decade', 'distinct_books', 'total_reviews', 'avg_rating']
decade_stats['avg_rating'] = decade_stats['avg_rating'].astype(float)

valid_decades = decade_stats[decade_stats['distinct_books'] >= 10].sort_values('avg_rating', ascending=False)

print('Valid decades:', valid_decades.shape[0])
if not valid_decades.empty:
    top = valid_decades.iloc[0]
    result = {'decade': top['decade'], 'avg_rating': round(top['avg_rating'], 3), 'books': int(top['distinct_books'])}
    print('Top decade:', result)
else:
    result = None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None}

exec(code, env_args)
