code = """import json, re, pandas as pd

# Load data from storage
review_file = var_call_yTtjnKCY6kvbrpxLl53DvSXk
books_file = var_call_ci5lDKnx1tPGkSMoEVcJETip

with open(review_file, 'r') as f:
    reviews = json.load(f)
with open(books_file, 'r') as f:
    books = json.load(f)

# Convert to DataFrames
df_reviews = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

# Normalize IDs if needed (assuming purchase_id like 'purchaseid_1' and book_id like 'bookid_1')

def normalize_id(s):
    if pd.isna(s):
        return None
    m = re.search(r'(\d+)$', str(s))
    return m.group(1) if m else None

df_reviews['id_norm'] = df_reviews['purchase_id'].apply(normalize_id)
df_books['id_norm'] = df_books['book_id'].apply(normalize_id)

# Merge on normalized ID
merged = pd.merge(df_reviews, df_books[['book_id','details','id_norm']], on='id_norm', how='inner')

# Extract publication year from 'details' using regex for 4-digit year between 1900 and 2029

year_pattern = re.compile(r'(19\d{2}|20[0-2]\d)')

def extract_year(text):
    if pd.isna(text):
        return None
    years = year_pattern.findall(str(text))
    if not years:
        return None
    # Heuristic: choose earliest year as publication year
    years_int = sorted(int(y) for y in years)
    return years_int[0]

merged['pub_year'] = merged['details'].apply(extract_year)

# Filter rows with valid publication year
merged = merged.dropna(subset=['pub_year'])
merged['pub_year'] = merged['pub_year'].astype(int)

# Convert rating to float
merged['rating'] = merged['rating'].astype(float)

# Compute decade
merged['decade'] = (merged['pub_year'] // 10) * 10

# For each book (book_id), compute its average rating
book_avg = merged.groupby(['book_id','decade'])['rating'].mean().reset_index(name='book_avg_rating')

# For each decade, consider only decades with at least 10 distinct books having ratings
decade_stats = book_avg.groupby('decade').agg(
    num_books=('book_id','nunique'),
    avg_rating=('book_avg_rating','mean')
).reset_index()

eligible = decade_stats[decade_stats['num_books'] >= 10]

if eligible.empty:
    result = None
else:
    best_row = eligible.sort_values('avg_rating', ascending=False).iloc[0]
    decade = int(best_row['decade'])
    result = f"{decade}s"

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_g3g675vYq6cJSGEeT9qnU8GM': ['books_info'], 'var_call_IWk7mTvOrkZtkVZxrMb6w7Yc': ['review'], 'var_call_yTtjnKCY6kvbrpxLl53DvSXk': 'file_storage/call_yTtjnKCY6kvbrpxLl53DvSXk.json', 'var_call_ci5lDKnx1tPGkSMoEVcJETip': 'file_storage/call_ci5lDKnx1tPGkSMoEVcJETip.json'}

exec(code, env_args)
