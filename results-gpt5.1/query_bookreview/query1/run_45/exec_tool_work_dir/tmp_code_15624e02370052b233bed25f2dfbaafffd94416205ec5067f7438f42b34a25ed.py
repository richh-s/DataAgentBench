code = """import json, re, pandas as pd

# Load full results from JSON files
with open(var_call_G9sQqq1cufyeVkOCXWJScTE6, 'r') as f:
    books = json.load(f)
with open(var_call_A6a5INsg5wGFUoiyMZHWGWMH, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)[['book_id', 'details']]
reviews_df = pd.DataFrame(reviews)[['purchase_id', 'rating']]

# Extract publication year from details using regex
# Look for patterns like 'on January 1, 2004', 'on May 18, 2014', 'released on March 20, 1995', etc.

year_pattern = re.compile(r'(19|20)\d{2}')

def extract_year(text):
    if not isinstance(text, str):
        return None
    matches = year_pattern.findall(text)
    # year_pattern returns tuples for (19|20), we instead search with another regex
    years = re.findall(r'(19|20)\d{2}', text)
    # Above returns list of strings like '2004', '1995'
    if not years:
        return None
    # Heuristic: choose the earliest 4-digit year as publication year
    years_int = sorted({int(y) for y in years})
    return years_int[0]

books_df['pub_year'] = books_df['details'].apply(extract_year)
books_df = books_df.dropna(subset=['pub_year'])
books_df['pub_year'] = books_df['pub_year'].astype(int)

# Map purchase_id to book_id via simple normalization (assuming they correspond like 'bookid_1' <-> 'purchaseid_1')
# If names follow that pattern, extract trailing integer and join on it.

def id_to_num(x):
    if not isinstance(x, str):
        return None
    m = re.search(r"(\d+)$", x)
    return int(m.group(1)) if m else None

books_df['id_num'] = books_df['book_id'].apply(id_to_num)
reviews_df['id_num'] = reviews_df['purchase_id'].apply(id_to_num)

books_df = books_df.dropna(subset=['id_num'])
reviews_df = reviews_df.dropna(subset=['id_num'])

books_df['id_num'] = books_df['id_num'].astype(int)
reviews_df['id_num'] = reviews_df['id_num'].astype(int)

# Merge reviews with books on the numeric id
merged = pd.merge(reviews_df, books_df[['id_num', 'pub_year']], on='id_num', how='inner')

# Ensure rating is float
merged['rating'] = merged['rating'].astype(float)

# Compute decade
merged['decade'] = (merged['pub_year'] // 10) * 10

# Count distinct books per decade (by id_num)
book_counts = merged.groupby('decade')['id_num'].nunique().reset_index(name='distinct_books')

# Filter decades with at least 10 distinct books
valid_decades = book_counts[book_counts['distinct_books'] >= 10]['decade']

valid_merged = merged[merged['decade'].isin(valid_decades)]

if valid_merged.empty:
    result = None
else:
    decade_avg = valid_merged.groupby('decade')['rating'].mean().reset_index()
    # Get decade with highest average rating
    best_row = decade_avg.sort_values('rating', ascending=False).iloc[0]
    best_decade = int(best_row['decade'])
    result = f"{best_decade}s"

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_G9sQqq1cufyeVkOCXWJScTE6': 'file_storage/call_G9sQqq1cufyeVkOCXWJScTE6.json', 'var_call_OpjUUrAdY5fC5fQIqL7YTRk3': ['books_info'], 'var_call_fkqGRkTBfdO0fpu93bDX5PGh': ['review'], 'var_call_A6a5INsg5wGFUoiyMZHWGWMH': 'file_storage/call_A6a5INsg5wGFUoiyMZHWGWMH.json'}

exec(code, env_args)
