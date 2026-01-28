code = """import json
import ast
import pandas as pd

# Load tool results from storage (file paths)
with open(var_call_YhZX8vRAtavpsKOuUjyEtv9n, 'r', encoding='utf-8') as f:
    reviews = json.load(f)
with open(var_call_fllTWoAjDGJfuej0oHuUvvA7, 'r', encoding='utf-8') as f:
    books = json.load(f)

# Create DataFrames
rev_df = pd.DataFrame(reviews)
books_df = pd.DataFrame(books)

# Clean and convert ratings
rev_df = rev_df.dropna(subset=['purchase_id', 'rating'])
rev_df['rating'] = rev_df['rating'].astype(float)

# Map purchase_id to book_id (fuzzy mapping: purchaseid_N -> bookid_N)
rev_df['book_id'] = rev_df['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_')

# Aggregate ratings from 2020 onwards (reviews already filtered in SQL)
agg = rev_df.groupby('book_id').agg(average_rating=('rating', 'mean'), review_count=('rating', 'count')).reset_index()

# Parse categories in books_df and filter for Children's Books
def parse_categories(cat_str):
    try:
        parsed = ast.literal_eval(cat_str) if isinstance(cat_str, str) else []
        if isinstance(parsed, (list, tuple)):
            return parsed
        return []
    except Exception:
        return []

books_df['categories_parsed'] = books_df['categories'].apply(parse_categories)
books_children = books_df[books_df['categories_parsed'].apply(lambda x: "Children's Books" in x)].copy()

# Merge aggregated ratings with children's books
merged = pd.merge(books_children, agg, on='book_id', how='inner')

# Filter for average rating >= 4.5
result_df = merged[merged['average_rating'] >= 4.5].copy()

# Prepare output
result_df['average_rating'] = result_df['average_rating'].round(3)
result_df = result_df.sort_values(by=['average_rating', 'review_count'], ascending=[False, False])

results = []
for _, row in result_df.iterrows():
    results.append({
        'book_id': row['book_id'],
        'title': row.get('title', None),
        'average_rating': float(row['average_rating']),
        'review_count': int(row['review_count'])
    })

# Print according to required format
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_9YUP3mhXEBryg2bHIGnAMBZz': ['review'], 'var_call_YhZX8vRAtavpsKOuUjyEtv9n': 'file_storage/call_YhZX8vRAtavpsKOuUjyEtv9n.json', 'var_call_f3JBRT4A0WtkFlle3hu2QOzb': ['books_info'], 'var_call_fllTWoAjDGJfuej0oHuUvvA7': 'file_storage/call_fllTWoAjDGJfuej0oHuUvvA7.json'}

exec(code, env_args)
