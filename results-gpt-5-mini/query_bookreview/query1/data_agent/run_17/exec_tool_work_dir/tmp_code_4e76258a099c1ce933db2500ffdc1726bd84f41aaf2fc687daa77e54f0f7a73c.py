code = """import json, re, pandas as pd

# Load data from storage files
with open(var_call_XTvE2u4u8fNfAT70SyBtj3lO, 'r') as f:
    reviews = json.load(f)
with open(var_call_WgirpVXkL6BEgT2yzTQt6Ktv, 'r') as f:
    books = json.load(f)

# Create DataFrames
df_rev = pd.DataFrame(reviews)
# Convert avg_rating to float
df_rev['avg_rating'] = df_rev['avg_rating'].astype(float)

# Map purchase_id -> book_id by extracting digits
def purchase_to_book(pid):
    m = re.search(r"(\d+)", pid)
    if m:
        return f"bookid_{m.group(1)}"
    return None

df_rev['book_id'] = df_rev['purchase_id'].apply(purchase_to_book)

# Load books dataframe
df_books = pd.DataFrame(books)

# Extract publication year from details field
def extract_year(details):
    if not isinstance(details, str):
        return None
    years = re.findall(r"\b(\d{4})\b", details)
    for y in years:
        try:
            yi = int(y)
            if 1500 <= yi <= 2025:
                return yi
        except:
            continue
    return None

# Apply extraction
if 'details' in df_books.columns:
    df_books['pub_year'] = df_books['details'].apply(extract_year)
else:
    df_books['pub_year'] = None

# Drop books without year
df_books = df_books.dropna(subset=['pub_year'])

# Create decade string
df_books['decade'] = df_books['pub_year'].apply(lambda y: f"{(int(y)//10)*10}s")

# Merge reviews (per-book avg) with books on book_id
df = pd.merge(df_rev, df_books[['book_id','decade']], on='book_id', how='inner')

# Group by decade, compute average of avg_rating across distinct books
group = df.groupby('decade').agg(n_books=('book_id','nunique'), avg_rating=('avg_rating','mean')).reset_index()

# Filter decades with at least 10 distinct books
group_filtered = group[group['n_books'] >= 10]

# If no decade meets criteria, prepare result accordingly
if group_filtered.empty:
    result = {'best_decade': None, 'avg_rating': None, 'n_books': 0, 'decades': []}
else:
    # Find decade with highest average rating
    best_row = group_filtered.sort_values(['avg_rating', 'n_books'], ascending=[False, False]).iloc[0]
    best_decade = best_row['decade']
    best_avg = float(best_row['avg_rating'])
    best_n = int(best_row['n_books'])
    # prepare list of decades
    decades_list = []
    for _, r in group_filtered.sort_values('decade').iterrows():
        decades_list.append({'decade': r['decade'], 'avg_rating': float(r['avg_rating']), 'n_books': int(r['n_books'])})
    result = {'best_decade': best_decade, 'avg_rating': round(best_avg,4), 'n_books': best_n, 'decades': decades_list}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HMpLhDV5JN6U08VwosCXQpgv': ['review'], 'var_call_tm06RGmquUHZ4WBzlNs8BZRv': ['books_info'], 'var_call_XTvE2u4u8fNfAT70SyBtj3lO': 'file_storage/call_XTvE2u4u8fNfAT70SyBtj3lO.json', 'var_call_WgirpVXkL6BEgT2yzTQt6Ktv': 'file_storage/call_WgirpVXkL6BEgT2yzTQt6Ktv.json'}

exec(code, env_args)
