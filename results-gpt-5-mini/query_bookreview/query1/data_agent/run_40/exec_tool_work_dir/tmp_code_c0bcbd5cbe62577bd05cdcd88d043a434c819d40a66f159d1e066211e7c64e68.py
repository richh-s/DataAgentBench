code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_caHGGXUt1VLNpELhqCC5y9AH, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(var_call_t0ZBVMIZsMYvShDIaE8Q4iCJ, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Keep necessary columns
if 'book_id' not in books_df.columns:
    books_df['book_id'] = None
if 'details' not in books_df.columns:
    books_df['details'] = None

books_df = books_df[['book_id', 'details']].copy()

# Map book_id to purchase_id by replacing prefix
books_df['purchase_id'] = books_df['book_id'].astype(str).str.replace('bookid_', 'purchaseid_')

# Extract publication year from details using regex
def extract_year(s):
    if not isinstance(s, str):
        return None
    # look for years 1700-2099
    m = re.search(r"\b(17|18|19|20)\d{2}\b", s)
    if m:
        return int(m.group(0))
    return None

books_df['year'] = books_df['details'].apply(extract_year)
books_df = books_df.dropna(subset=['year'])
books_df['year'] = books_df['year'].astype(int)
books_df['decade'] = (books_df['year'] // 10 * 10).astype(int).astype(str) + 's'

# Prepare reviews dataframe: ensure numeric avg_rating
reviews_df = reviews_df[['purchase_id', 'avg_rating']].copy()
reviews_df['avg_rating'] = pd.to_numeric(reviews_df['avg_rating'], errors='coerce')

# Merge on purchase_id
merged = pd.merge(books_df, reviews_df, on='purchase_id', how='inner')

# Group by decade: count distinct books and compute average of per-book avg_rating
grp = merged.groupby('decade').agg(book_count=('purchase_id', 'nunique'), avg_of_avg=('avg_rating', 'mean')).reset_index()

# Filter decades with at least 10 distinct books
grp = grp[grp['book_count'] >= 10]

if grp.empty:
    result = {'decade': None, 'average_rating': None, 'book_count': 0}
else:
    best = grp.loc[grp['avg_of_avg'].idxmax()]
    result = {'decade': best['decade'], 'average_rating': round(float(best['avg_of_avg']), 4), 'book_count': int(best['book_count'])}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_l6tSoV2BcoOcQSiAS5CaRqL9': ['review'], 'var_call_nmmLgFKi9uB6QwSMDZ3nRC9k': ['books_info'], 'var_call_caHGGXUt1VLNpELhqCC5y9AH': 'file_storage/call_caHGGXUt1VLNpELhqCC5y9AH.json', 'var_call_t0ZBVMIZsMYvShDIaE8Q4iCJ': 'file_storage/call_t0ZBVMIZsMYvShDIaE8Q4iCJ.json'}

exec(code, env_args)
