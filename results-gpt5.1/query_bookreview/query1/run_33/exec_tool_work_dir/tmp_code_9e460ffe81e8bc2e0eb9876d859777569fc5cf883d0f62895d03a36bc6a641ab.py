code = """import json, re, pandas as pd

# Load full results from JSON files
with open(var_call_qJ4F1Jo8Bq14y29orQRQkrqg, 'r') as f:
    books = json.load(f)
with open(var_call_1EiTdmJPTfEaWlGLXmAFNYD8, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Extract publication year from details text using regex for a 4-digit year between 1800-2099
year_pattern = re.compile(r'(18|19|20)\d{2}')

def extract_year(details):
    if not isinstance(details, str):
        return None
    matches = year_pattern.findall(details)
    # findall with this pattern returns list of full matches if no capturing groups are used; but we used groups, so fix:
    matches_full = re.findall(r'(?:18|19|20)\d{2}', details)
    years = [int(y) for y in matches_full]
    if not years:
        return None
    # heuristic: earliest year in text as publication year
    return min(years)

books_df['pub_year'] = books_df['details'].apply(extract_year)

# Drop rows without pub_year
books_df = books_df.dropna(subset=['pub_year'])
books_df['pub_year'] = books_df['pub_year'].astype(int)

# Derive decade label like '1980s'
books_df['decade'] = (books_df['pub_year'] // 10 * 10).astype(int).astype(str) + 's'

# Join reviews with books on purchase_id/book_id
merged = reviews_df.merge(books_df[['book_id', 'decade']], left_on='purchase_id', right_on='book_id', how='inner')

# Ensure rating is float
merged['rating'] = merged['rating'].astype(float)

# Compute stats per decade: number of distinct books and average rating
stats = merged.groupby('decade').agg(
    distinct_books=('book_id', 'nunique'),
    avg_rating=('rating', 'mean')
).reset_index()

# Filter decades with at least 10 distinct books
stats = stats[stats['distinct_books'] >= 10]

if stats.empty:
    result = None
else:
    # Get decade with highest average rating; in case of tie, choose earliest decade
    max_avg = stats['avg_rating'].max()
    top = stats[stats['avg_rating'] == max_avg]
    # choose earliest decade (by numeric prefix)
    top['dec_start'] = top['decade'].str.extract(r'(\d{4})').astype(int)
    top = top.sort_values('dec_start').iloc[0]
    result = top['decade']

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_qJ4F1Jo8Bq14y29orQRQkrqg': 'file_storage/call_qJ4F1Jo8Bq14y29orQRQkrqg.json', 'var_call_RLFj9UEJnUcn9qFYtMEQTzax': ['books_info'], 'var_call_59tfr1G4noKhzllw786wceGj': ['review'], 'var_call_1EiTdmJPTfEaWlGLXmAFNYD8': 'file_storage/call_1EiTdmJPTfEaWlGLXmAFNYD8.json'}

exec(code, env_args)
