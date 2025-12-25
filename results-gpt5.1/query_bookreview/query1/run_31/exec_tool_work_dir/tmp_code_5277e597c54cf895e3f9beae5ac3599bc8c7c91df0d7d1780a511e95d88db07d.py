code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_uhVZ2gsQhslCGqgyAB3ZksGl, 'r') as f:
    books = json.load(f)
with open(var_call_iFtNvlSP4aFsfb9v0QaVbjGv, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Extract year from details text where possible
pattern = re.compile(r'(19|20)\d{2}')

def extract_year(details):
    if not isinstance(details, str):
        return None
    # look for phrases like 'on January 1, 2004' or 'in 2004' or 'in a 1998 edition'
    years = pattern.findall(details)
    # pattern finds ('19','20') groups; easier to search differently

execute_year_pattern = re.compile(r'(19|20)\d{2}')

def get_year(text):
    if not isinstance(text, str):
        return None
    m = execute_year_pattern.search(text)
    if m:
        return int(m.group(0))
    return None

books_df['year'] = books_df['details'].apply(get_year)

# Derive decade label like '1980s'
books_df['decade'] = books_df['year'].apply(lambda y: f"{int(y//10*10)}s" if pd.notnull(y) else None)

# Join reviews with books on purchase_id == book_id
merged = reviews_df.merge(books_df[['book_id','decade']], left_on='purchase_id', right_on='book_id', how='left')

# Drop rows without a decade
merged = merged.dropna(subset=['decade'])

# Ensure rating is float
merged['rating'] = merged['rating'].astype(float)

# Compute per-book average rating and decade
book_avg = merged.groupby(['book_id','decade'])['rating'].mean().reset_index(name='book_avg_rating')

# Count distinct books per decade
decade_counts = book_avg.groupby('decade').agg(distinct_books=('book_id','nunique'), avg_rating=('book_avg_rating','mean')).reset_index()

# Filter decades with at least 10 distinct books
valid_decades = decade_counts[decade_counts['distinct_books'] >= 10]

if valid_decades.empty:
    result = None
else:
    best_row = valid_decades.sort_values('avg_rating', ascending=False).iloc[0]
    result = best_row['decade']

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_uhVZ2gsQhslCGqgyAB3ZksGl': 'file_storage/call_uhVZ2gsQhslCGqgyAB3ZksGl.json', 'var_call_IRoFJYShGY0oRS6NFaf876pi': ['books_info'], 'var_call_oLcibJJ9PdtK6eB7SBPu8TC0': ['review'], 'var_call_iFtNvlSP4aFsfb9v0QaVbjGv': 'file_storage/call_iFtNvlSP4aFsfb9v0QaVbjGv.json'}

exec(code, env_args)
