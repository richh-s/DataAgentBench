code = """import json, re, pandas as pd

# Load full results
with open(var_call_ib2vgNVa3jD3GtuuRtMCBrBO, 'r') as f:
    books = json.load(f)
with open(var_call_Rs8hWo3JOqMPwu1RXHDWsKq2, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Extract publication year from details using regex
# Look for patterns like 'on January 1, 2004', 'on May 20, 1996', 'on March 20, 1995', or 'on January 1, 1945'
year_pattern = re.compile(r'on [A-Za-z]+\s+\d{1,2},\s*(\d{4})|on\s*(January|February|March|April|May|June|July|August|September|October|November|December)\s*\d{1,2},\s*(\d{4})|on\s*January 1,\s*(\d{4})|on\s*(\d{4})|January 1,\s*(\d{4})|released on\s*[A-Za-z]+\s+\d{1,2},\s*(\d{4})|released on\s*(\d{4})')

def extract_year(text):
    if not isinstance(text, str):
        return None
    m = year_pattern.search(text)
    if not m:
        return None
    for g in m.groups():
        if g and re.fullmatch(r"\d{4}", g):
            return int(g)
    return None

books_df['year'] = books_df['details'].apply(extract_year)
books_df = books_df.dropna(subset=['year'])

# Map purchase_id to year via book_id (they are aligned like 'purchaseid_123' <-> 'bookid_123')
# Extract numeric suffix and join
books_df['num'] = books_df['book_id'].str.extract(r'(\d+)$').astype(int)
reviews_df['num'] = reviews_df['purchase_id'].str.extract(r'(\d+)$').astype(int)

merged = pd.merge(reviews_df, books_df[['num','year']], on='num', how='inner')

# Ensure rating is float
merged['rating'] = merged['rating'].astype(float)

# Compute book-level average rating per year (distinct books by num)
book_year_rating = merged.groupby(['num','year'])['rating'].mean().reset_index()

# Map year to decade label like '1980s'
book_year_rating['decade'] = (book_year_rating['year'] // 10 * 10).astype(int).astype(str) + 's'

# Filter decades with at least 10 distinct books
decade_counts = book_year_rating.groupby('decade')['num'].nunique()
valid_decades = decade_counts[decade_counts >= 10].index
filtered = book_year_rating[book_year_rating['decade'].isin(valid_decades)]

# Compute average rating per decade (averaging book-level averages)
decade_avg = filtered.groupby('decade')['rating'].mean().reset_index()

if decade_avg.empty:
    result = None
else:
    top_row = decade_avg.sort_values('rating', ascending=False).iloc[0]
    result = top_row['decade']

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_ib2vgNVa3jD3GtuuRtMCBrBO': 'file_storage/call_ib2vgNVa3jD3GtuuRtMCBrBO.json', 'var_call_9Qq7APi6VReylL7g6eNNxp8Y': ['books_info'], 'var_call_KVpUfW1POVD9yFjU1rApOl9B': ['review'], 'var_call_Rs8hWo3JOqMPwu1RXHDWsKq2': 'file_storage/call_Rs8hWo3JOqMPwu1RXHDWsKq2.json'}

exec(code, env_args)
