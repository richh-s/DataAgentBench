code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_NWNS8quNZTf4JDaHeRNsDIXf, 'r') as f:
    books = json.load(f)
with open(var_call_w1jh55KooexdJVLcoNiRj1OU, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Extract publication year from details text
year_pattern = re.compile(r'(19|20)\d{2}')

def extract_year(text):
    if not isinstance(text, str):
        return None
    # Look for phrases like '2004', often near 'published' or 'released'
    years = year_pattern.findall(text)
    # year_pattern with groups returns tuples; adjust
    matches = re.findall(r'(19|20)\d{2}', text)
    # Use full regex to get full years
    matches_full = re.findall(r'(?:19|20)\d{2}', text)
    if matches_full:
        # Heuristic: choose the first year in text
        return int(matches_full[0])
    return None

books_df['pub_year'] = books_df['details'].apply(extract_year)
books_df = books_df.dropna(subset=['pub_year'])
books_df['pub_year'] = books_df['pub_year'].astype(int)
books_df['decade'] = (books_df['pub_year'] // 10) * 10

# Map purchase_id to book_id via simple normalization (here they seem like 'purchaseid_123' vs 'bookid_123')

def purchase_to_book(pid):
    if not isinstance(pid, str):
        return None
    m = re.match(r'purchaseid_(\d+)', pid)
    if m:
        return 'bookid_' + m.group(1)
    return None

reviews_df['book_id'] = reviews_df['purchase_id'].apply(purchase_to_book)
reviews_df = reviews_df.dropna(subset=['book_id'])

# Ensure rating is float
reviews_df['rating'] = reviews_df['rating'].astype(float)

# Join reviews with books on book_id
merged = pd.merge(reviews_df, books_df[['book_id', 'decade']], on='book_id', how='inner')

# For each decade, compute number of distinct books and average rating (across all reviews)
book_counts = merged.groupby('decade')['book_id'].nunique().rename('distinct_books')
avg_ratings = merged.groupby('decade')['rating'].mean().rename('avg_rating')
summary = pd.concat([book_counts, avg_ratings], axis=1).reset_index()

# Filter decades with at least 10 distinct books
summary_filtered = summary[summary['distinct_books'] >= 10]

if summary_filtered.empty:
    result = None
else:
    best_row = summary_filtered.sort_values('avg_rating', ascending=False).iloc[0]
    decade = int(best_row['decade'])
    # Format like '1980s'
    result = f"{decade}s"

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_NWNS8quNZTf4JDaHeRNsDIXf': 'file_storage/call_NWNS8quNZTf4JDaHeRNsDIXf.json', 'var_call_LeYsrShIcmkYDadVgWZJiN5Z': ['review'], 'var_call_w1jh55KooexdJVLcoNiRj1OU': 'file_storage/call_w1jh55KooexdJVLcoNiRj1OU.json'}

exec(code, env_args)
