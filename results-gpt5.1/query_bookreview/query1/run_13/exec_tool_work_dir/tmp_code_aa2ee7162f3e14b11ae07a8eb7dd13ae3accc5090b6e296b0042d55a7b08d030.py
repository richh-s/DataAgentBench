code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_oThluguydmWSqvteWZRd1UsG, 'r') as f:
    books = json.load(f)
with open(var_call_HDVG3cnMZV0HBr6OXN04XrfX, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Extract publication year from details
year_pattern = re.compile(r'(19|20)\d{2}')

def extract_year(text):
    if not isinstance(text, str):
        return None
    # Look for phrases like 'on January 1, 2004' or 'in 2004' etc.
    m = year_pattern.search(text)
    if m:
        return int(m.group(0))
    return None

books_df['year'] = books_df['details'].apply(extract_year)
books_df = books_df.dropna(subset=['year'])
books_df['year'] = books_df['year'].astype(int)
books_df['decade'] = (books_df['year'] // 10) * 10

# Join reviews to books by purchase_id/book_id (they appear to match exactly in sample)
merged = reviews_df.merge(books_df[['book_id','decade']], left_on='purchase_id', right_on='book_id', how='inner')

# Clean ratings to float
merged['rating'] = merged['rating'].astype(float)

# Compute distinct books per decade
book_counts = merged.groupby('decade')['book_id'].nunique().rename('distinct_books')

# Filter decades with at least 10 distinct books
valid_decades = book_counts[book_counts >= 10].index

valid = merged[merged['decade'].isin(valid_decades)]

avg_ratings = valid.groupby('decade')['rating'].mean()

if avg_ratings.empty:
    result = None
else:
    best_decade = int(avg_ratings.sort_values(ascending=False).index[0])
    result = f"{best_decade}s"

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_oThluguydmWSqvteWZRd1UsG': 'file_storage/call_oThluguydmWSqvteWZRd1UsG.json', 'var_call_TbTldeV1QrbVXRktigdSs9S2': ['books_info'], 'var_call_zdLqQSjo2UKM0n3fKULc43kR': ['review'], 'var_call_HDVG3cnMZV0HBr6OXN04XrfX': 'file_storage/call_HDVG3cnMZV0HBr6OXN04XrfX.json'}

exec(code, env_args)
