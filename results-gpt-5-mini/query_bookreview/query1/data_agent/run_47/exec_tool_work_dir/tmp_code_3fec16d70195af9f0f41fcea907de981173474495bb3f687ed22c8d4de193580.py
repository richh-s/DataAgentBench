code = """import json
import pandas as pd
import re

# Load the query results from storage files
books_path = var_call_eByCs9ZBoVAOkuMRUiFZ6WZK
reviews_path = var_call_DZWGzH2v2GOEBxmcafXJ0k69

with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Normalize review ratings
reviews_df = reviews_df.dropna(subset=['purchase_id', 'rating'])
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')
reviews_df = reviews_df.dropna(subset=['rating'])

# Convert purchase_id to book_id by replacing prefix
reviews_df['book_id'] = reviews_df['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)

# Extract publication year from books.details using regex (years between 1500 and 2029)
def extract_year(text):
    if not isinstance(text, str):
        return None
    m = re.search(r"\b(1[5-9]\d{2}|20[0-2]\d)\b", text)
    if m:
        try:
            return int(m.group(0))
        except:
            return None
    return None

books_df['pub_year'] = books_df['details'].apply(extract_year)
books_df = books_df.dropna(subset=['book_id', 'pub_year'])
books_df['pub_year'] = books_df['pub_year'].astype(int)

# Compute per-book average rating from reviews
book_avg = reviews_df.groupby('book_id', as_index=False)['rating'].mean()
book_avg.rename(columns={'rating':'avg_rating'}, inplace=True)

# Merge with books to get publication year
merged = pd.merge(book_avg, books_df[['book_id','title','pub_year']], on='book_id', how='inner')

# Compute decade string
merged['decade_start'] = (merged['pub_year'] // 10) * 10
merged['decade'] = merged['decade_start'].astype(int).astype(str) + 's'

# For each decade compute number of distinct books and average of book average ratings
decade_stats = merged.groupby('decade').agg(
    n_books = ('book_id', 'nunique'),
    decade_avg_rating = ('avg_rating', 'mean')
).reset_index()

# Filter decades with at least 10 distinct books
eligible = decade_stats[decade_stats['n_books'] >= 10]

if eligible.empty:
    result = None
else:
    # Find decade with highest average rating; if tie pick the earliest decade alphabetically
    top = eligible.sort_values(['decade_avg_rating', 'decade'], ascending=[False, True]).iloc[0]
    result = top['decade']

# Print result in required format as JSON-serializable string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_0H9hgh0vh6CpBm1euN2YtOoL': ['review'], 'var_call_lPOSNXzvwspBPy271TohxtDp': ['books_info'], 'var_call_eByCs9ZBoVAOkuMRUiFZ6WZK': 'file_storage/call_eByCs9ZBoVAOkuMRUiFZ6WZK.json', 'var_call_DZWGzH2v2GOEBxmcafXJ0k69': 'file_storage/call_DZWGzH2v2GOEBxmcafXJ0k69.json'}

exec(code, env_args)
