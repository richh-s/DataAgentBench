code = """import json, re, pandas as pd

# Load full reviews aggregate
path = var_call_4mjXIte44JFy7OTYBfsTWqXO
with open(path, 'r') as f:
    reviews = json.load(f)

# Load all books_info rows (already in memory as list)
books = var_call_QDiVZxiZKWxVgQgADDZHX6lE

# Build DataFrames
reviews_df = pd.DataFrame(reviews)
books_df = pd.DataFrame(books)

# Extract publication year from details text using regex for 4-digit year between 1900-2099
year_pattern = re.compile(r"(19\d{2}|20\d{2})")

def extract_year(details):
    if not isinstance(details, str):
        return None
    # Common patterns like 'on January 1, 2004', 'in 2004', '2004 edition', etc.
    years = year_pattern.findall(details)
    if not years:
        return None
    # Heuristic: use the earliest year mentioned as publication year
    years_int = sorted(int(y) for y in years)
    return years_int[0]

books_df['pub_year'] = books_df['details'].apply(extract_year)
books_df['decade'] = books_df['pub_year'].apply(lambda y: None if pd.isna(y) else int(y//10*10))

# Fuzzy join purchase_id <-> book_id: they share the same suffix after an underscore (e.g., purchaseid_123, bookid_123)

def id_to_num(x):
    if not isinstance(x, str):
        return None
    m = re.search(r"(\d+)$", x)
    return m.group(1) if m else None

reviews_df['id_num'] = reviews_df['purchase_id'].apply(id_to_num)
books_df['id_num'] = books_df['book_id'].apply(id_to_num)

merged = pd.merge(reviews_df, books_df[['book_id','id_num','decade']], on='id_num', how='inner')

# Filter rows with valid decade
merged = merged[merged['decade'].notna()]

# Convert avg_rating to float
merged['avg_rating'] = merged['avg_rating'].astype(float)

# Now we have per-book avg_rating linked to a decade. Ensure distinct books by book_id.
# For safety, if a book_id appears multiple times (shouldn't), average its ratings first.
book_avg = merged.groupby(['book_id','decade'], as_index=False)['avg_rating'].mean()

# Count distinct books per decade
decade_stats = book_avg.groupby('decade').agg(num_books=('book_id','nunique'), decade_avg_rating=('avg_rating','mean')).reset_index()

# Filter decades with at least 10 distinct books
decade_stats = decade_stats[decade_stats['num_books'] >= 10]

if decade_stats.empty:
    result = None
else:
    # Pick decade with highest average rating; tie-breaker: latest decade
    max_avg = decade_stats['decade_avg_rating'].max()
    candidates = decade_stats[decade_stats['decade_avg_rating'] == max_avg]
    best_decade = candidates['decade'].max()
    # format like '1980s'
    result = f"{int(best_decade)}s"

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_QDiVZxiZKWxVgQgADDZHX6lE': 'file_storage/call_QDiVZxiZKWxVgQgADDZHX6lE.json', 'var_call_sWfKwU8tczFxO5s7otXkXhKn': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}], 'var_call_a3kBBHuYBKbOE0VxP5IICctn': ['review'], 'var_call_4mjXIte44JFy7OTYBfsTWqXO': 'file_storage/call_4mjXIte44JFy7OTYBfsTWqXO.json'}

exec(code, env_args)
