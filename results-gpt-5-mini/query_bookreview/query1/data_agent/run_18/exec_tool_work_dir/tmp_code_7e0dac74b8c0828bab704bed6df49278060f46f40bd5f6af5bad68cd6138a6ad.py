code = """import json, re
import pandas as pd

# Load full books and reviews from storage
with open(var_call_V2Ub7kWMd06b7DMRBz5xaSBj, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(var_call_7WJPf7muozLZut10OuOdjvFo, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# helper to extract numeric id
def extract_num(s):
    if pd.isna(s):
        return None
    m = re.search(r"(\d+)", str(s))
    return int(m.group(1)) if m else None

# extract year
def extract_year(s):
    if pd.isna(s):
        return None
    m = re.search(r"\b(1[0-9]{3}|20[0-2][0-9])\b", str(s))
    return int(m.group(0)) if m else None

# apply
if 'book_id' in df_books.columns:
    df_books['num_id'] = df_books['book_id'].apply(extract_num)
else:
    df_books['num_id'] = None

if 'purchase_id' in df_reviews.columns:
    df_reviews['num_id'] = df_reviews['purchase_id'].apply(extract_num)
else:
    df_reviews['num_id'] = None

# ratings numeric
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

# year
if 'details' in df_books.columns:
    df_books['year'] = df_books['details'].apply(extract_year)
else:
    df_books['year'] = None

# stats
books_total = len(df_books)
books_with_num = df_books['num_id'].notna().sum()
books_with_year = df_books['year'].notna().sum()
reviews_total = len(df_reviews)
reviews_with_num = df_reviews['num_id'].notna().sum()

# intersection
book_ids_set = set(df_books['num_id'].dropna().astype(int).unique())
review_ids_set = set(df_reviews['num_id'].dropna().astype(int).unique())
intersect = sorted(book_ids_set & review_ids_set)
intersect_count = len(intersect)

# distribution of years among intersecting books
books_intersect = df_books[df_books['num_id'].isin(intersect)].copy()
year_counts = books_intersect['year'].value_counts(dropna=False).to_dict()

# For debugging, show sample of book entries where year is missing
sample_missing_year = books_intersect[books_intersect['year'].isna()].head(10).to_dict(orient='records')

# compute merged dataset and aggregation same as before
reviews_clean = df_reviews.dropna(subset=['num_id']).copy()
books_clean = df_books.dropna(subset=['num_id']).copy()
merged = pd.merge(reviews_clean, books_clean, on='num_id', how='inner', suffixes=('_rev','_book'))
merged = merged.dropna(subset=['rating'])
merged['year'] = merged['year'].astype('Int64')
merged = merged[merged['year'].notna()]
merged['decade_start'] = (merged['year']//10)*10
merged['decade'] = merged['decade_start'].astype(int).astype(str) + 's'

agg = merged.groupby('decade').agg(book_count = ('book_id', lambda x: x.nunique()), avg_rating = ('rating', 'mean')).reset_index()
agg_filtered = agg[agg['book_count'] >= 10]

best = None
if not agg_filtered.empty:
    best_row = agg_filtered.sort_values(['avg_rating','book_count'], ascending=[False, False]).iloc[0]
    best = { 'decade': best_row['decade'], 'average_rating': round(float(best_row['avg_rating']),4), 'book_count': int(best_row['book_count']) }

out = {
    'books_total': books_total,
    'books_with_num': int(books_with_num),
    'books_with_year': int(books_with_year),
    'reviews_total': reviews_total,
    'reviews_with_num': int(reviews_with_num),
    'intersect_count': int(intersect_count),
    'year_counts_in_intersect_sample': {str(k): int(v) for k,v in list(year_counts.items())[:10]},
    'sample_missing_year_in_intersect': sample_missing_year,
    'agg_top_decades_all': agg.sort_values('avg_rating', ascending=False).head(10).to_dict(orient='records'),
    'agg_filtered': agg_filtered.to_dict(orient='records'),
    'best': best
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_y1Tx7d5jbxthUjoKbarSZn6t': 'file_storage/call_y1Tx7d5jbxthUjoKbarSZn6t.json', 'var_call_AoGVRqzQ10M2wVo911ReA77F': ['review'], 'var_call_7WJPf7muozLZut10OuOdjvFo': 'file_storage/call_7WJPf7muozLZut10OuOdjvFo.json', 'var_call_YMgkOmecrFWpmUbJ3KAaY39G': {'decade': None, 'average_rating': None, 'book_count': 0}, 'var_call_V2Ub7kWMd06b7DMRBz5xaSBj': 'file_storage/call_V2Ub7kWMd06b7DMRBz5xaSBj.json'}

exec(code, env_args)
