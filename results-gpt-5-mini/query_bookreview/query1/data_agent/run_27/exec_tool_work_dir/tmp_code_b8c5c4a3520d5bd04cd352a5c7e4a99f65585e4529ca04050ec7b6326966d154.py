code = """import json
import pandas as pd
import re

# load results from parallel queries
with open(var_call_TUvJXKQeqJ37mMHR2spm3ift, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(var_call_Nx0j5IGC14Xr8U35jHcX9nVS, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# basic counts
books_count = len(books_df)
reviews_count = len(reviews_df)

# normalize ratings
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')

# id extraction
def extract_num_id(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'_(\d+)$', s)
    if m:
        return m.group(1)
    m2 = re.search(r'(\d+)', s)
    return m2.group(1) if m2 else None

books_df['num_id'] = books_df['book_id'].apply(extract_num_id)
reviews_df['num_id'] = reviews_df['purchase_id'].apply(extract_num_id)
reviews_df['book_id'] = reviews_df['num_id'].apply(lambda x: f'bookid_{x}' if pd.notnull(x) else None)

# merge
merged = reviews_df.merge(books_df[['book_id', 'details']], on='book_id', how='left')

# presence counts
merged_rows = len(merged)
rows_with_details = merged['details'].notnull().sum()
rows_without_details = merged['details'].isnull().sum()

# extract years
def extract_year(details):
    if not isinstance(details, str):
        return None
    years = re.findall(r'\b(1[5-9]\d{2}|20\d{2})\b', details)
    if not years:
        return None
    for y in years:
        ys = y if isinstance(y, str) else (y[0] if isinstance(y, (list, tuple)) else str(y))
        try:
            yi = int(ys)
            if 1500 <= yi <= 2023:
                return yi
        except:
            continue
    return None

merged['year'] = merged['details'].apply(extract_year)
rows_with_year = merged['year'].notnull().sum()
unique_books_with_year = merged[merged['year'].notnull()]['book_id'].nunique()

# decades
merged_valid = merged[merged['year'].notnull() & merged['rating'].notnull()].copy()
if not merged_valid.empty:
    merged_valid['year'] = merged_valid['year'].astype(int)
    merged_valid['decade_start'] = (merged_valid['year'] // 10) * 10
    merged_valid['decade'] = merged_valid['decade_start'].astype(str) + 's'
    decade_book_counts = merged_valid.groupby('decade')['book_id'].nunique().reset_index().rename(columns={'book_id':'distinct_books'})
    decade_avg = merged_valid.groupby('decade')['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})
    decade_stats = pd.merge(decade_avg, decade_book_counts, on='decade')
    decade_stats_list = decade_stats.sort_values('decade', ascending=True).to_dict(orient='records')
    valid_decades = [d for d in decade_stats_list if d['distinct_books'] >= 10]
    best_decade = None
    if valid_decades:
        # choose highest avg_rating, tie-breaker by decade string
        best = sorted(valid_decades, key=lambda x: (-x['avg_rating'], x['decade']))[0]
        best_decade = best['decade']
else:
    decade_stats_list = []
    valid_decades = []
    best_decade = None

out = {
    'books_count': books_count,
    'reviews_count': reviews_count,
    'merged_rows': merged_rows,
    'rows_with_details': int(rows_with_details),
    'rows_without_details': int(rows_without_details),
    'rows_with_year': int(rows_with_year),
    'unique_books_with_year': int(unique_books_with_year),
    'decade_stats': decade_stats_list,
    'valid_decades': valid_decades,
    'best_decade': best_decade
}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_25XrTT1v8MA76LlhO9Ah0Qpu': ['review'], 'var_call_CaaMHIphba5mhsgrjOW70AAl': ['books_info'], 'var_call_ahSeu74lplrW2uWVFYFbYKof': 'file_storage/call_ahSeu74lplrW2uWVFYFbYKof.json', 'var_call_t8s9j3CLGS3oQRddFrBguw0a': 'file_storage/call_t8s9j3CLGS3oQRddFrBguw0a.json', 'var_call_AnPCoO6KSaGRcg5jGKCGL4Nx': None, 'var_call_o2VX8jZXpeJ7U4MZ3xWm2fnA': [], 'var_call_TUvJXKQeqJ37mMHR2spm3ift': 'file_storage/call_TUvJXKQeqJ37mMHR2spm3ift.json', 'var_call_Nx0j5IGC14Xr8U35jHcX9nVS': 'file_storage/call_Nx0j5IGC14Xr8U35jHcX9nVS.json'}

exec(code, env_args)
