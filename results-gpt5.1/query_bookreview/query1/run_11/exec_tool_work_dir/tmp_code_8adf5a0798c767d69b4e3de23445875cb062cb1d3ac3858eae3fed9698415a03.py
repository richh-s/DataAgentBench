code = """import json, re, pandas as pd

# Load full data from JSON files
with open(var_call_p7jfXNa0JXXWruGIwnv4gvI0, 'r') as f:
    books = json.load(f)
with open(var_call_R3RwRVIaPYWXlOEYB5rKK5sF, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Extract year of publication from 'details' using regex patterns
# Look for patterns like 'on January 1, 2004', 'on May 20, 1996', 'released on November 15, 2000',
# or 'on January 1, 1945', etc.

patterns = [
    r'on [A-Za-z]+ \d{1,2}, (\d{4})',
    r'on [A-Za-z]+ \d{4}',
    r'on January 1, (\d{4})',
    r'on [A-Za-z]+ \d{1,2}, (\d{4})',
    r'released on [A-Za-z]+ \d{1,2}, (\d{4})',
    r'released on (\w+ \d{1,2}, (\d{4}))',
    r'edition on [A-Za-z]+ \d{1,2}, (\d{4})',
    r' on (January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, (\d{4})',
    r'on (January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, (\d{4})',
    r'on [A-Za-z]+ \d{1,2}, (\d{4})',
    r' on (\d{4})',
]

def extract_year(text):
    if not isinstance(text, str):
        return None
    # First try common explicit date patterns
    m = re.search(r'on [A-Za-z]+ \d{1,2}, (\d{4})', text)
    if m:
        return int(m.group(1))
    # Then look for 'on January 1, 1993' etc.
    m = re.search(r'on (January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, (\d{4})', text)
    if m:
        return int(m.group(2))
    # Try 'in 2013', 'in 1998'
    m = re.search(r'\b(19\d{2}|20\d{2})\b', text)
    if m:
        return int(m.group(1))
    return None

books_df['year'] = books_df['details'].apply(extract_year)
books_df = books_df.dropna(subset=['year'])
books_df['year'] = books_df['year'].astype(int)

# Compute decade string like '1980s'
books_df['decade'] = (books_df['year'] // 10 * 10).astype(int).astype(str) + 's'

# Join reviews with books on purchase_id/book_id exact match (IDs appear aligned in sample)
merged = reviews_df.merge(books_df[['book_id', 'decade']], left_on='purchase_id', right_on='book_id', how='inner')

# Ensure rating is float
merged['rating'] = merged['rating'].astype(float)

# For each book, compute its average rating
book_avg = merged.groupby(['book_id', 'decade'])['rating'].mean().reset_index(name='book_avg_rating')

# For each decade, consider books with at least one rating (implicitly) and require at least 10 distinct books
decade_stats = book_avg.groupby('decade').agg(
    avg_rating=('book_avg_rating', 'mean'),
    n_books=('book_id', 'nunique')
).reset_index()

eligible = decade_stats[decade_stats['n_books'] >= 10]

if eligible.empty:
    result = None
else:
    best_row = eligible.sort_values('avg_rating', ascending=False).iloc[0]
    result = best_row['decade']

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_p7jfXNa0JXXWruGIwnv4gvI0': 'file_storage/call_p7jfXNa0JXXWruGIwnv4gvI0.json', 'var_call_C3NsYMI82w1RaTL9CeyTXN0g': ['books_info'], 'var_call_FQyKM6uR6376Ax25gBomyEPO': ['review'], 'var_call_R3RwRVIaPYWXlOEYB5rKK5sF': 'file_storage/call_R3RwRVIaPYWXlOEYB5rKK5sF.json'}

exec(code, env_args)
