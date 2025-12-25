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

# Normalize IDs
# Extract numbers from the IDs
df_reviews['id_num'] = df_reviews['purchase_id'].str.extract(r'(\d+)')
df_books['id_num'] = df_books['book_id'].str.extract(r'(\d+)')

# Function to extract year
def extract_year(text):
    if not isinstance(text, str):
        return None
    # Pattern: Month Day, Year (e.g., January 1, 2004)
    # Also handle simpler years if needed, but let's stick to full date first as it's safer
    # Added abbreviated months just in case
    match = re.search(r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2},\s+(\d{4})', text)
    if match:
        return int(match.group(1))
    return None

# Apply extraction
df_books['year'] = df_books['details'].apply(extract_year)
df_books['year'] = df_books['year'].fillna(df_books['subtitle'].apply(extract_year))

# Check how many books have years
books_with_year = df_books['year'].notnull().sum()
total_books = len(df_books)

# Convert year to decade
df_books['decade'] = (df_books['year'] // 10) * 10
df_books['decade'] = df_books['decade'].fillna(-1).astype(int).astype(str) + "s"

# Merge
df_merged = pd.merge(df_reviews, df_books, on='id_num', how='inner')

# Convert rating to float
df_merged['rating'] = df_merged['rating'].astype(float)

# Group by decade
decade_stats = df_merged.groupby('decade').agg(
    avg_rating=('rating', 'mean'),
    distinct_books=('book_id', 'nunique')
).reset_index()

# Filter decades with at least 10 distinct books
# Filter out the "-1s" decade (missing year)
decade_stats_filtered = decade_stats[(decade_stats['distinct_books'] >= 10) & (decade_stats['decade'] != '-1s')]

# Find the decade with the highest average rating
if not decade_stats_filtered.empty:
    best_decade = decade_stats_filtered.sort_values(by='avg_rating', ascending=False).iloc[0]
    result = {
        "decade": best_decade['decade'],
        "average_rating": best_decade['avg_rating'],
        "distinct_books": int(best_decade['distinct_books']),
        "all_stats": decade_stats.to_dict(orient='records') # Debug info
    }
else:
    result = {
        "msg": "No decade meets the criteria.",
        "debug_stats": decade_stats.to_dict(orient='records'),
        "books_with_year": int(books_with_year),
        "total_books": int(total_books),
        "merged_rows": len(df_merged)
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-11980478109906576321': ['books_info'], 'var_function-call-9741073344249609642': 'file_storage/function-call-9741073344249609642.json', 'var_function-call-15691835330281128782': ['review'], 'var_function-call-10425051511888995697': [{'COUNT(*)': '1833'}], 'var_function-call-2377527336151131583': [{'count': '200'}], 'var_function-call-8048486413748627374': 'file_storage/function-call-8048486413748627374.json', 'var_function-call-10305899063336439880': 'file_storage/function-call-10305899063336439880.json', 'var_function-call-5379179217560364536': 'No decade meets the criteria.'}

exec(code, env_args)
