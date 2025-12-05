code = """import json, re, pandas as pd

with open(var_call_KshLFUwbCSbeplb9ScB0maeo, 'r') as f:
    books = json.load(f)
with open(var_call_BHk2IHcgCXhb9vX856qgcPrF, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Extract publication year from details: look for phrases like 'on Month DD, YYYY' or 'on January 1, 2004' etc.
year_pattern = re.compile(r'(18|19|20)\d{2}')

def get_year(text):
    if not isinstance(text, str):
        return None
    # find all 4-digit years
    years = re.findall(r'(18\d{2}|19\d{2}|20\d{2})', text)
    if not years:
        return None
    # heuristic: choose earliest year as publication year
    years_int = sorted(set(int(y) for y in years))
    return years_int[0]

books_df['year'] = books_df['details'].apply(get_year)
books_df = books_df.dropna(subset=['year'])
books_df['year'] = books_df['year'].astype(int)
books_df['decade'] = (books_df['year'] // 10) * 10

# Map purchase_id to book_id via fuzzy join: assume they correspond exactly
reviews_df = reviews_df.dropna(subset=['purchase_id', 'rating'])

# Ensure rating is float
reviews_df['rating'] = reviews_df['rating'].astype(float)

# Join on purchase_id == book_id
merged = pd.merge(reviews_df, books_df[['book_id', 'decade']], left_on='purchase_id', right_on='book_id', how='inner')

# Compute per-book average rating
book_avg = merged.groupby(['book_id', 'decade'])['rating'].mean().reset_index(name='book_avg_rating')

# Filter decades with at least 10 distinct books that have been rated
decade_counts = book_avg.groupby('decade')['book_id'].nunique().reset_index(name='book_count')
valid_decades = decade_counts[decade_counts['book_count'] >= 10]['decade']

valid_book_avg = book_avg[book_avg['decade'].isin(valid_decades)]

# Compute decade average rating as mean of book average ratings
decade_avg = valid_book_avg.groupby('decade')['book_avg_rating'].mean().reset_index()

if decade_avg.empty:
    result = None
else:
    best_row = decade_avg.sort_values('book_avg_rating', ascending=False).iloc[0]
    decade_str = f"{int(best_row['decade'])}s"
    result = decade_str

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_KshLFUwbCSbeplb9ScB0maeo': 'file_storage/call_KshLFUwbCSbeplb9ScB0maeo.json', 'var_call_LHUzTIG8UR2Wakp1c2fEiOKD': ['books_info'], 'var_call_q1aorycwM6QTrlIDzitq7Ga3': ['review'], 'var_call_BHk2IHcgCXhb9vX856qgcPrF': 'file_storage/call_BHk2IHcgCXhb9vX856qgcPrF.json', 'var_call_PTT6x3baj1byQsyv3B2UZA8K': 'error'}

exec(code, env_args)
