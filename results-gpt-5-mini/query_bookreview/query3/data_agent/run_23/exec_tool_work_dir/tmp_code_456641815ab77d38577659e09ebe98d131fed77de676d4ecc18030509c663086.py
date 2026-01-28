code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_ViKRoIfLCXMQuKgzH6XJ6AiQ, 'r') as f:
    reviews = json.load(f)
with open(var_call_qXpRCZpwHnepLRx1nKXDykj0, 'r') as f:
    books = json.load(f)

# Create DataFrames
df_reviews = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

# Normalize ratings to float
if 'rating' in df_reviews.columns:
    df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

# Extract numeric id from purchase_id and book_id for fuzzy join
def extract_num(x):
    if pd.isna(x):
        return None
    m = re.search(r"(\d+)", str(x))
    return int(m.group(1)) if m else None

df_reviews['num_id'] = df_reviews['purchase_id'].apply(extract_num)
df_books['num_id'] = df_books['book_id'].apply(extract_num)

# Filter reviews from 2020 onwards just in case
df_reviews['review_time'] = pd.to_datetime(df_reviews['review_time'], errors='coerce')
df_reviews = df_reviews[df_reviews['review_time'] >= pd.to_datetime('2020-01-01')]

# Aggregate reviews by num_id
agg = df_reviews.groupby('num_id').agg(average_rating=('rating', 'mean'), review_count=('rating', 'count')).reset_index()

# Filter books in Children's Books category
# categories column is a string representation of a list; check substring
df_books['is_children'] = df_books['categories'].astype(str).str.contains("Children's Books", na=False)
children_books = df_books[df_books['is_children'] == True]

# Merge aggregated ratings with children books on num_id
merged = pd.merge(children_books, agg, on='num_id', how='left')

# Keep only those with average_rating >= 4.5
result_df = merged[merged['average_rating'] >= 4.5].copy()

# Prepare final result list
result_df['average_rating'] = result_df['average_rating'].round(3)
result_df['review_count'] = result_df['review_count'].fillna(0).astype(int)

# If review_count is 0, it shouldn't meet >=4.5, but keep logic
final = result_df.sort_values(['average_rating', 'review_count'], ascending=[False, False])

results = []
for _, row in final.iterrows():
    results.append({
        'book_id': row['book_id'],
        'title': row.get('title', None),
        'average_rating': None if pd.isna(row['average_rating']) else float(row['average_rating']),
        'review_count': int(row['review_count'])
    })

# Print in required format
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_5CddxGPFQboc7HUCk8KE4EmP': ['review'], 'var_call_I3eZ2nevVyDP2zuxCJ353lNL': ['books_info'], 'var_call_ViKRoIfLCXMQuKgzH6XJ6AiQ': 'file_storage/call_ViKRoIfLCXMQuKgzH6XJ6AiQ.json', 'var_call_qXpRCZpwHnepLRx1nKXDykj0': 'file_storage/call_qXpRCZpwHnepLRx1nKXDykj0.json'}

exec(code, env_args)
