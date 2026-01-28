code = """import json
import pandas as pd

# Load data from storage file paths
reviews = json.load(open(var_call_bmQPnMYNRM14VNpgvl0bSD7f, 'r', encoding='utf-8'))
books = json.load(open(var_call_uvrZOsqYe3KAemqgu4ogGtUr, 'r', encoding='utf-8'))

# Create DataFrames
df_reviews = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

# Clean reviews
# Convert rating to numeric
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')
# Parse review_time
df_reviews['review_time'] = pd.to_datetime(df_reviews['review_time'], errors='coerce')
# Filter reviews from 2020-01-01 onwards
df_reviews = df_reviews[df_reviews['review_time'] >= pd.Timestamp('2020-01-01')].copy()
# Map purchase_id to book_id by replacing prefix
if 'purchase_id' in df_reviews.columns:
    df_reviews['book_id'] = df_reviews['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_')
else:
    df_reviews['book_id'] = None

# Aggregate average rating and count per book_id
agg = df_reviews.groupby('book_id').agg(avg_rating=('rating', 'mean'), review_count=('rating', 'count')).reset_index()

# Filter books categorized as "Children's Books"
# Ensure categories column exists
if 'categories' in df_books.columns:
    df_books['is_childrens'] = df_books['categories'].astype(str).str.contains("Children's Books", na=False)
else:
    df_books['is_childrens'] = False

child_books = df_books[df_books['is_childrens']].copy()

# Merge aggregated ratings with child books
merged = pd.merge(child_books, agg, on='book_id', how='inner')

# Filter average rating >= 4.5
result_df = merged[merged['avg_rating'] >= 4.5].copy()

# Prepare final results
result_df['avg_rating'] = result_df['avg_rating'].round(3)

results = []
for _, row in result_df.sort_values(['avg_rating', 'review_count'], ascending=[False, False]).iterrows():
    results.append({
        'book_id': row.get('book_id'),
        'title': row.get('title'),
        'avg_rating': float(row.get('avg_rating')) if pd.notna(row.get('avg_rating')) else None,
        'review_count_2020_onwards': int(row.get('review_count'))
    })

# Print in required format
print("__RESULT__:")
print(json.dumps(results, ensure_ascii=False))"""

env_args = {'var_call_tDCVxEuGVgbct0aGg2thxRiW': ['review'], 'var_call_bmQPnMYNRM14VNpgvl0bSD7f': 'file_storage/call_bmQPnMYNRM14VNpgvl0bSD7f.json', 'var_call_4ai7pTbW7urmmLZWAM9GpoxR': ['books_info'], 'var_call_uvrZOsqYe3KAemqgu4ogGtUr': 'file_storage/call_uvrZOsqYe3KAemqgu4ogGtUr.json'}

exec(code, env_args)
