code = """import json
import pandas as pd
import re

with open(var_call_caHGGXUt1VLNpELhqCC5y9AH, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(var_call_t0ZBVMIZsMYvShDIaE8Q4iCJ, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

books_df = books_df[['book_id', 'title', 'details']].copy()
books_df['purchase_id'] = books_df['book_id'].astype(str).str.replace('bookid_', 'purchaseid_')

# extract year
def extract_year(s):
    if not isinstance(s, str):
        return None
    m = re.search(r"\b(17|18|19|20)\d{2}\b", s)
    if m:
        return int(m.group(0))
    return None

books_df['year'] = books_df['details'].apply(extract_year)
books_df['decade'] = books_df['year'].dropna().astype(int).floordiv(10).mul(10).astype('Int64').astype(str) + 's'

reviews_df['avg_rating'] = pd.to_numeric(reviews_df['avg_rating'], errors='coerce')

merged = pd.merge(books_df, reviews_df, on='purchase_id', how='inner')

# compute overall stats
total_books_with_year = books_df['year'].notna().sum()
unique_books_with_year = books_df[books_df['year'].notna()]['book_id'].nunique()
merged_count = len(merged)
merged_unique_books = merged['purchase_id'].nunique()

grp = merged.groupby('decade').agg(book_count=('purchase_id','nunique'), avg_of_avg=('avg_rating','mean')).reset_index()

grp_sorted = grp.sort_values(by='avg_of_avg', ascending=False).to_dict(orient='records')

result = {
    'total_books_with_year': int(total_books_with_year),
    'unique_books_with_year': int(unique_books_with_year),
    'merged_rows': int(merged_count),
    'merged_unique_books': int(merged_unique_books),
    'decade_stats': grp_sorted[:50]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_l6tSoV2BcoOcQSiAS5CaRqL9': ['review'], 'var_call_nmmLgFKi9uB6QwSMDZ3nRC9k': ['books_info'], 'var_call_caHGGXUt1VLNpELhqCC5y9AH': 'file_storage/call_caHGGXUt1VLNpELhqCC5y9AH.json', 'var_call_t0ZBVMIZsMYvShDIaE8Q4iCJ': 'file_storage/call_t0ZBVMIZsMYvShDIaE8Q4iCJ.json', 'var_call_37aXB9KdPitRNKEQp4Yyw6V7': {'decade': None, 'average_rating': None, 'book_count': 0}}

exec(code, env_args)
