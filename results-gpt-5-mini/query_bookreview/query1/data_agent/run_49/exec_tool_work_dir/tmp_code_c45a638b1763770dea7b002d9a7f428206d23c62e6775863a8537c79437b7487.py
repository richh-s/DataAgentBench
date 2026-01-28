code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
books_path = var_call_6tcfcXA6GTqzqez1IsHycyNJ
reviews_path = var_call_XnYzyYg7VsZwY5KH84rsdemb

with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Extract numeric id from book_id and purchase_id
books_df['book_num'] = books_df['book_id'].astype(str).str.extract(r'(\d+)$').astype(float)
reviews_df['book_num'] = reviews_df['purchase_id'].astype(str).str.extract(r'(\d+)$').astype(float)

# Extract year from details using regex for years between 1000 and 2099
def extract_year(detail):
    if not isinstance(detail, str):
        return None
    m = re.search(r'\b(1[0-9]{3}|20[0-9]{2})\b', detail)
    return int(m.group(0)) if m else None

books_df['year'] = books_df['details'].apply(extract_year)
# Drop books without year or without numeric id
books_df = books_df.dropna(subset=['book_num','year'])
books_df['book_num'] = books_df['book_num'].astype(int)
books_df['year'] = books_df['year'].astype(int)

# Compute decade string
books_df['decade'] = (books_df['year'] // 10 * 10).astype(int).astype(str) + 's'

# Prepare reviews: convert rating to numeric and drop rows without book_num
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')
reviews_df = reviews_df.dropna(subset=['book_num','rating'])
reviews_df['book_num'] = reviews_df['book_num'].astype(int)

# Merge reviews with books on book_num
merged = pd.merge(reviews_df, books_df[['book_num','year','decade','book_id','title']], on='book_num', how='inner')

# Compute book-level average rating
book_avg = merged.groupby(['book_num','decade','book_id','title'], as_index=False)['rating'].mean().rename(columns={'rating':'book_avg_rating'})

# For each decade, consider only books that have been rated (book_avg already ensures that)
decade_stats = book_avg.groupby('decade').agg(num_books=pd.NamedAgg(column='book_num', aggfunc='nunique'), avg_of_book_avgs=pd.NamedAgg(column='book_avg_rating', aggfunc='mean')).reset_index()

# Filter decades with at least 10 distinct books
eligible = decade_stats[decade_stats['num_books'] >= 10]

if eligible.empty:
    result = None
else:
    # Find decade with highest average (if tie, take the one with highest avg then largest num_books, then earliest decade)
    eligible = eligible.sort_values(by=['avg_of_book_avgs','num_books','decade'], ascending=[False, False, True])
    top = eligible.iloc[0]
    result = {
        'decade': top['decade'],
        'average_rating': round(float(top['avg_of_book_avgs']), 4),
        'num_books': int(top['num_books'])
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_RZV1vaaVuQpJiM3cElj9TGQx': ['review'], 'var_call_LgY0bMOn0KqnwsQRapoLec6N': ['books_info'], 'var_call_6tcfcXA6GTqzqez1IsHycyNJ': 'file_storage/call_6tcfcXA6GTqzqez1IsHycyNJ.json', 'var_call_XnYzyYg7VsZwY5KH84rsdemb': 'file_storage/call_XnYzyYg7VsZwY5KH84rsdemb.json'}

exec(code, env_args)
