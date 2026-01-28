code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
reviews_path = var_call_HZyfVibvDqgCXwdhDEJl6Srg
books_path = var_call_2xKoHvIpNF3IsCSnTt0Z72Ge

with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)
with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)

# Create DataFrames
df_rev = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

# Normalize ratings
# Some ratings may be strings; convert to numeric
df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')

# Extract numeric id from purchase_id and book_id
extract_num = lambda s: (re.search(r"(\d+)", s) and re.search(r"(\d+)", s).group(1)) or None

df_rev['num_id'] = df_rev['purchase_id'].astype(str).apply(lambda x: extract_num(x))
df_books['num_id'] = df_books['book_id'].astype(str).apply(lambda x: extract_num(x))

# Compute average rating per purchase_id (num_id)
avg_by_purchase = df_rev.groupby('num_id', dropna=True)['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})

# Merge with books on num_id
merged = pd.merge(df_books, avg_by_purchase, on='num_id', how='left')

# Filter for Literature & Fiction in categories and English language in details
# categories is a string representation of a list; check substring
mask_category = merged['categories'].str.contains('Literature & Fiction', case=False, na=False)
mask_english = merged['details'].str.lower().str.contains('english', na=False)

filtered = merged[mask_category & mask_english].copy()

# Filter for perfect average rating of 5.0 (allow tiny floating tolerance)
filtered['avg_rating'] = filtered['avg_rating'].astype(float)
filtered_perfect = filtered[filtered['avg_rating'].notnull() & (filtered['avg_rating'] >= 4.9999999) & (filtered['avg_rating'] <= 5.0000001)].copy()

# Prepare results
results = []
for _, row in filtered_perfect.iterrows():
    results.append({
        'book_id': row['book_id'],
        'title': row.get('title', None),
        'avg_rating': round(float(row['avg_rating']), 6),
        'categories': row.get('categories', None),
        'details': row.get('details', None)
    })

# Output as JSON string
output = json.dumps(results)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_VpJTmjijYwxWY0RIxCAxNeD2': ['review'], 'var_call_HnHOr197G3ukYW8Xx4pcJEjm': ['books_info'], 'var_call_HZyfVibvDqgCXwdhDEJl6Srg': 'file_storage/call_HZyfVibvDqgCXwdhDEJl6Srg.json', 'var_call_2xKoHvIpNF3IsCSnTt0Z72Ge': 'file_storage/call_2xKoHvIpNF3IsCSnTt0Z72Ge.json'}

exec(code, env_args)
