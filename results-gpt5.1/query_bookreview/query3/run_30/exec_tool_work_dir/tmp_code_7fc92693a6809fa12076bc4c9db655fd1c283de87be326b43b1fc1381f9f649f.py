code = """import json, pandas as pd

# Load full books_info and review data from files
books_path = var_call_NCkO8iYaBJaskPB43JTKaTyR
reviews_path = var_call_XcrZt0AsTjDaa7xAbwh9oOz8

with open(books_path, 'r') as f:
    books = json.load(f)
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Filter Children's Books in categories string
child_books = books_df[books_df['categories'].str.contains("Children's Books", na=False)].copy()

# Fuzzy join: purchase_id like 'purchaseid_XX' vs book_id 'bookid_XX' -> match on numeric suffix
child_books['suffix'] = child_books['book_id'].str.extract(r'(\d+)$')[0]
reviews_df['suffix'] = reviews_df['purchase_id'].str.extract(r'(\d+)$')[0]

# Compute average rating per suffix from 2020 onwards (already filtered in SQL)
reviews_df['rating'] = reviews_df['rating'].astype(float)
avg_ratings = reviews_df.groupby('suffix', as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating_2020plus'})

merged = pd.merge(child_books, avg_ratings, on='suffix', how='inner')

# Filter avg rating >= 4.5
result_df = merged[merged['avg_rating_2020plus'] >= 4.5][['book_id','title','avg_rating_2020plus']].sort_values('avg_rating_2020plus', ascending=False)

result = result_df.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_NCkO8iYaBJaskPB43JTKaTyR': 'file_storage/call_NCkO8iYaBJaskPB43JTKaTyR.json', 'var_call_EbS3eHqq1q3DSALvAdaIotLl': ['review'], 'var_call_XcrZt0AsTjDaa7xAbwh9oOz8': 'file_storage/call_XcrZt0AsTjDaa7xAbwh9oOz8.json'}

exec(code, env_args)
