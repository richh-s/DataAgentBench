code = """import json, pandas as pd

# Load full books data
with open(var_call_dLl9bLygkGmtZpFxrLa86e98, 'r') as f:
    books = json.load(f)
books_df = pd.DataFrame(books)

# Filter to Children's Books using substring match in categories string
childrens_books = books_df[books_df['categories'].str.contains("Children's Books", na=False)].copy()

# Load full review data
with open(var_call_XkEbeoGGz1i9SWreWG8yrmo1, 'r') as f:
    reviews = json.load(f)
reviews_df = pd.DataFrame(reviews)

# ratings to float
reviews_df['rating'] = reviews_df['rating'].astype(float)

# Fuzzy join: assume purchase_id and book_id share the numeric suffix
# Extract numeric part from IDs
def extract_num(s):
    return int(''.join(ch for ch in s if ch.isdigit())) if isinstance(s, str) else None

childrens_books['id_num'] = childrens_books['book_id'].apply(extract_num)
reviews_df['id_num'] = reviews_df['purchase_id'].apply(extract_num)

merged = pd.merge(reviews_df, childrens_books[['book_id','title','id_num']], on='id_num', how='inner')

# Compute average rating per book from 2020 onwards (reviews_df already filtered by time in SQL)
avg_ratings = merged.groupby(['book_id','title'])['rating'].mean().reset_index()

high_rated = avg_ratings[avg_ratings['rating'] >= 4.5].sort_values('rating', ascending=False)

result = high_rated.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_dLl9bLygkGmtZpFxrLa86e98': 'file_storage/call_dLl9bLygkGmtZpFxrLa86e98.json', 'var_call_oVtI0EbiFpzt3s1cwyufhH5I': ['review'], 'var_call_XkEbeoGGz1i9SWreWG8yrmo1': 'file_storage/call_XkEbeoGGz1i9SWreWG8yrmo1.json'}

exec(code, env_args)
