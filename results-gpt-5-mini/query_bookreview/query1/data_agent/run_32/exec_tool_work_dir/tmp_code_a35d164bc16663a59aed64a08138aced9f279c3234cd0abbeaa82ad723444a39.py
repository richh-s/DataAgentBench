code = """import json
import re
import pandas as pd

# Load data from storage files
with open(var_call_uoQBgM6xZLvCULtDUAjY1i45, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(var_call_3TFu4u2EsLD3NZx9UVOjCJLb, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Create DataFrames
df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# Normalize ratings to numeric
if 'rating' in df_reviews.columns:
    df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

# Map purchase_id -> book_id by replacing prefix
if 'purchase_id' in df_reviews.columns:
    df_reviews['book_id'] = df_reviews['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)

# Extract year from details in books
def extract_year(detail):
    if not isinstance(detail, str):
        return None
    # look for 4-digit year between 1000 and 2099
    m = re.search(r"\b(1[0-9]{3}|20[0-9]{2})\b", detail)
    if m:
        try:
            y = int(m.group(0))
            return y
        except:
            return None
    return None

if 'details' in df_books.columns:
    df_books['year'] = df_books['details'].apply(extract_year)
else:
    df_books['year'] = None

# Merge reviews with books on book_id
df = pd.merge(df_reviews, df_books[['book_id','year']], on='book_id', how='inner')

# Drop rows with no year or no rating
df = df[df['year'].notna() & df['rating'].notna()].copy()

# Compute decade label
df['decade_start'] = (df['year'].astype(int) // 10) * 10
df['decade'] = df['decade_start'].astype(int).astype(str) + 's'

# For each decade compute distinct book count and average rating (across reviews)
group = df.groupby('decade').agg(distinct_books=('book_id', lambda x: x.nunique()), avg_rating=('rating', 'mean')).reset_index()

# Filter decades with at least 10 distinct books
group_filtered = group[group['distinct_books'] >= 10]

result_decade = None
result_avg = None
if not group_filtered.empty:
    # select decade with highest average rating; if ties, take the one with more books, then lexicographically
    group_filtered = group_filtered.sort_values(by=['avg_rating','distinct_books','decade'], ascending=[False, False, True])
    top = group_filtered.iloc[0]
    result_decade = top['decade']
    result_avg = float(top['avg_rating'])

# Prepare output
out = {
    'decade': result_decade,
    'average_rating': None if result_avg is None else round(result_avg, 4),
    'distinct_books_in_decade_with_ratings': None if result_decade is None else int(group_filtered.iloc[0]['distinct_books'])
}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_TmxbjPq0NdaugFpHVwIbt13H': ['books_info'], 'var_call_qtfordLX0oPiqP3bTJAZLsTQ': ['review'], 'var_call_uoQBgM6xZLvCULtDUAjY1i45': 'file_storage/call_uoQBgM6xZLvCULtDUAjY1i45.json', 'var_call_3TFu4u2EsLD3NZx9UVOjCJLb': 'file_storage/call_3TFu4u2EsLD3NZx9UVOjCJLb.json'}

exec(code, env_args)
