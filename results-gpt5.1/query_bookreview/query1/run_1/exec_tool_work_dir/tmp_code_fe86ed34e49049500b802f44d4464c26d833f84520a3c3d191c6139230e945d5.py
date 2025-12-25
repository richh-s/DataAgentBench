code = """import json, re, pandas as pd

# Load full results from JSON files
with open(var_call_Xh6RAFYMGCmD484p3je8SpuK, 'r') as f:
    reviews = json.load(f)
with open(var_call_MRTXIgAuwIoBfcFSNBMrZdH3, 'r') as f:
    books = json.load(f)

# Convert to DataFrames
df_reviews = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

# Ensure rating is float
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

# Extract publication year from details using regex for four-digit years between 1900 and 2099
year_pattern = re.compile(r'(19|20)\d{2}')

def extract_year(text):
    if not isinstance(text, str):
        return None
    years = [int(y) for y in year_pattern.findall(text.replace("'", ""))]  # incorrect; adjust

# Fix extraction properly

def extract_year(text):
    if not isinstance(text, str):
        return None
    matches = re.findall(r'(?:19|20)\d{2}', text)
    if not matches:
        return None
    # Heuristic: use the earliest year mentioned as publication year
    years = [int(m) for m in matches]
    return min(years)


df_books['pub_year'] = df_books['details'].apply(extract_year)

# Drop rows without publication year
df_books = df_books.dropna(subset=['pub_year'])

# Compute decade string, e.g., 1980s
df_books['decade'] = (df_books['pub_year'].astype(int) // 10 * 10).astype(int).astype(str) + 's'

# Join reviews to books on purchase_id == book_id
merged = pd.merge(df_reviews, df_books[['book_id', 'decade']], left_on='purchase_id', right_on='book_id', how='inner')

# For each book_id, compute its average rating
book_avg = merged.groupby(['book_id', 'decade'])['rating'].mean().reset_index(name='book_avg_rating')

# For each decade, consider decades with at least 10 distinct books that have been rated
decade_stats = book_avg.groupby('decade').agg(distinct_books=('book_id', 'nunique'), avg_rating=('book_avg_rating', 'mean')).reset_index()

eligible = decade_stats[decade_stats['distinct_books'] >= 10]

if eligible.empty:
    result = None
else:
    # Get decade with highest average rating; tie-breaker: earliest decade
    max_avg = eligible['avg_rating'].max()
    top = eligible[eligible['avg_rating'] == max_avg].sort_values('decade').iloc[0]
    result = {'decade': top['decade'], 'average_rating': float(round(top['avg_rating'], 4)), 'distinct_books': int(top['distinct_books'])}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_gquDcIB2oNhm0bnneUTjLur7': 'file_storage/call_gquDcIB2oNhm0bnneUTjLur7.json', 'var_call_CmZMA4SwO9IHufNyoCFGpXH0': ['review'], 'var_call_Xh6RAFYMGCmD484p3je8SpuK': 'file_storage/call_Xh6RAFYMGCmD484p3je8SpuK.json', 'var_call_MRTXIgAuwIoBfcFSNBMrZdH3': 'file_storage/call_MRTXIgAuwIoBfcFSNBMrZdH3.json'}

exec(code, env_args)
