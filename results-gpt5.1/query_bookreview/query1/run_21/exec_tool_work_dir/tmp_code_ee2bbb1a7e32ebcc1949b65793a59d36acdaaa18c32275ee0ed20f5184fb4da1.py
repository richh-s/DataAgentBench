code = """import json, re, pandas as pd

# Load full books and reviews data
with open(var_call_29gDCo82jXgBUDV5tcUnYXs8, 'r') as f:
    books = json.load(f)
with open(var_call_FLq1XjYdMBb6bVcHbvUoEkMV, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Extract publication year from details text
year_pattern = re.compile(r"(19|20)\d{2}")

def extract_year(text):
    if not isinstance(text, str):
        return None
    # prefer phrases like 'on Month D, YYYY' or direct year near 'published' or 'edition'
    candidates = year_pattern.findall(text)
    # findall with groups returns tuples for pattern with groups; adjust
    years = []
    for m in year_pattern.finditer(text):
        years.append(int(m.group(0)))
    if not years:
        return None
    # heuristic: choose earliest plausible publication year
    return min(y for y in years if 1800 <= y <= 2025) if any(1800 <= y <= 2025 for y in years) else None

books_df['pub_year'] = books_df['details'].apply(extract_year)
books_df = books_df.dropna(subset=['pub_year'])
books_df['pub_year'] = books_df['pub_year'].astype(int)
books_df['decade'] = (books_df['pub_year'] // 10) * 10

# Join reviews to books on id (purchase_id ~ book_id)
merged = reviews_df.merge(books_df[['book_id','decade']], left_on='purchase_id', right_on='book_id', how='inner')

# ratings to float
merged['rating'] = merged['rating'].astype(float)

# Compute per-book average rating
book_avg = merged.groupby(['book_id','decade'])['rating'].mean().reset_index(name='book_avg_rating')

# Filter decades with at least 10 distinct books
decade_counts = book_avg.groupby('decade')['book_id'].nunique().reset_index(name='n_books')
valid_decades = decade_counts[decade_counts['n_books'] >= 10]['decade']

filtered = book_avg[book_avg['decade'].isin(valid_decades)]

# Compute decade-level average of book averages
decade_avg = filtered.groupby('decade')['book_avg_rating'].mean().reset_index()

if decade_avg.empty:
    result = None
else:
    top_row = decade_avg.sort_values('book_avg_rating', ascending=False).iloc[0]
    decade = int(top_row['decade'])
    result = f"{decade}s"

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_29gDCo82jXgBUDV5tcUnYXs8': 'file_storage/call_29gDCo82jXgBUDV5tcUnYXs8.json', 'var_call_H3rgZ2Gt9ziyLne2dgU8UZU2': ['books_info'], 'var_call_bjzOZATU0hylNQ8NWKclaa8E': ['review'], 'var_call_FLq1XjYdMBb6bVcHbvUoEkMV': 'file_storage/call_FLq1XjYdMBb6bVcHbvUoEkMV.json'}

exec(code, env_args)
