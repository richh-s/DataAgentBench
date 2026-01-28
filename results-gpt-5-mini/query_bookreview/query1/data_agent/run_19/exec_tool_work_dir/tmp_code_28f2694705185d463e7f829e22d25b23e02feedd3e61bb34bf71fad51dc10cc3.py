code = """import json
import pandas as pd
import re

with open(var_call_Wv01vezERIxQWQNp3uhDCQDy, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(var_call_4RvMVzQw6ae3RUi3uTmH3BkO, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

def to_float(x):
    try:
        return float(x)
    except:
        return None

if 'rating' in df_reviews.columns:
    df_reviews['rating'] = df_reviews['rating'].apply(to_float)

# Map purchase_id to book_id
if 'purchase_id' in df_reviews.columns:
    df_reviews['book_id'] = df_reviews['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)

# Per-book avg
df_reviews_valid = df_reviews[df_reviews['rating'].notnull()]
book_avg = df_reviews_valid.groupby('book_id', dropna=False)['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})

merged = pd.merge(book_avg, df_books[['book_id','details']], on='book_id', how='left')

# extract year

def extract_year(text):
    if not isinstance(text, str):
        return None
    years = re.findall(r'\b(1[0-9]{3}|20[0-2][0-9])\b', text)
    if years:
        for y in years:
            try:
                yi = int(y)
                if 1000 <= yi <= 2023:
                    return yi
            except:
                continue
    years_all = re.findall(r'\b(\d{4})\b', text)
    for y in years_all:
        try:
            yi = int(y)
            if 1000 <= yi <= 2023:
                return yi
        except:
            continue
    return None

merged['year'] = merged['details'].apply(extract_year)
merged_with_year = merged[merged['year'].notnull()].copy()
merged_with_year['year'] = merged_with_year['year'].astype(int)
merged_with_year['decade'] = merged_with_year['year'].floordiv(10).mul(10).astype(int).astype(str) + 's'

decade_stats = merged_with_year.groupby('decade').agg(
    book_count = ('book_id', 'nunique'),
    decade_avg_rating = ('avg_rating', 'mean')
).reset_index()

eligible = decade_stats[decade_stats['book_count'] >= 10].copy()

best_decade = None
if not eligible.empty:
    best = eligible.loc[eligible['decade_avg_rating'].idxmax()]
    best_decade = best['decade']

# prepare serializable output
out = {
    'total_books_with_avg_rating': int(book_avg['book_id'].nunique()),
    'books_with_year_extracted': int(merged_with_year['book_id'].nunique()),
    'decade_stats': decade_stats.sort_values('decade').to_dict(orient='records'),
    'eligible_decades': eligible.sort_values('decade').to_dict(orient='records'),
    'best_decade': best_decade
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1sQwuGiVh9Xaqbw0U8PvXHJS': ['review'], 'var_call_s2vic9F4hCbhlVidy06HXrHS': ['books_info'], 'var_call_Wv01vezERIxQWQNp3uhDCQDy': 'file_storage/call_Wv01vezERIxQWQNp3uhDCQDy.json', 'var_call_4RvMVzQw6ae3RUi3uTmH3BkO': 'file_storage/call_4RvMVzQw6ae3RUi3uTmH3BkO.json', 'var_call_Yqn2bofCUxicIDA0CWwjQpmI': None}

exec(code, env_args)
