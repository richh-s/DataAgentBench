code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-8048486413748627374'], 'r') as f:
    reviews = json.load(f)
with open(locals()['var_function-call-10305899063336439880'], 'r') as f:
    books = json.load(f)

# Convert to DataFrame
df_reviews = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

# Function to extract year
def extract_year(text):
    if not isinstance(text, str):
        return None
    # Pattern: Month Day, Year (e.g., January 1, 2004)
    match = re.search(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})', text)
    if match:
        return int(match.group(1))
    return None

# Apply extraction
# Try details first, then subtitle
df_books['year'] = df_books['details'].apply(extract_year)
# Fill NaN with year from subtitle
df_books['year'] = df_books['year'].fillna(df_books['subtitle'].apply(extract_year))

# Filter out books with no year
df_books = df_books.dropna(subset=['year'])

# Convert year to decade
df_books['decade'] = (df_books['year'] // 10) * 10
df_books['decade'] = df_books['decade'].astype(int).astype(str) + "s"

# Merge reviews with books
# reviews: purchase_id, books: book_id
df_merged = pd.merge(df_reviews, df_books, left_on='purchase_id', right_on='book_id', how='inner')

# Convert rating to float
df_merged['rating'] = df_merged['rating'].astype(float)

# Group by decade
decade_stats = df_merged.groupby('decade').agg(
    avg_rating=('rating', 'mean'),
    distinct_books=('book_id', 'nunique')
).reset_index()

# Filter decades with at least 10 distinct books
decade_stats_filtered = decade_stats[decade_stats['distinct_books'] >= 10]

# Find the decade with the highest average rating
if not decade_stats_filtered.empty:
    best_decade = decade_stats_filtered.sort_values(by='avg_rating', ascending=False).iloc[0]
    result = {
        "decade": best_decade['decade'],
        "average_rating": best_decade['avg_rating'],
        "distinct_books": int(best_decade['distinct_books'])
    }
else:
    result = "No decade meets the criteria."

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-11980478109906576321': ['books_info'], 'var_function-call-9741073344249609642': 'file_storage/function-call-9741073344249609642.json', 'var_function-call-15691835330281128782': ['review'], 'var_function-call-10425051511888995697': [{'COUNT(*)': '1833'}], 'var_function-call-2377527336151131583': [{'count': '200'}], 'var_function-call-8048486413748627374': 'file_storage/function-call-8048486413748627374.json', 'var_function-call-10305899063336439880': 'file_storage/function-call-10305899063336439880.json'}

exec(code, env_args)
