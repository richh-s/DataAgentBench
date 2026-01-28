code = """import json
import pandas as pd
import re
with open(var_call_clwW1HpxqxlCKDXJvn9Iim9W, 'r') as f:
    reviews_data = json.load(f)
with open(var_call_mC9eh9kdqR7TFrzmoKhf7oa0, 'r') as f:
    books_data = json.load(f)
rv = pd.DataFrame(reviews_data)
bk = pd.DataFrame(books_data)
rv['purchase_id'] = rv['purchase_id'].astype(str)
rv_ids = set(rv['purchase_id'].unique())
bk_ids = set(bk['book_id'].unique())
# Map purchase to book ids
mapped_ids = set([pid.replace('purchaseid_','bookid_') for pid in rv_ids])

intersection = sorted(list(mapped_ids & bk_ids))

# Extract years from books
year_re = re.compile(r"\b(1[0-9]{3}|20[0-9]{2})\b")
def extract_year(text):
    if not isinstance(text, str):
        return None
    matches = year_re.findall(text)
    for m in matches:
        try:
            y = int(m)
            if 1000 <= y <= 2023:
                return y
        except:
            continue
    return None

bk['year'] = bk['details'].apply(extract_year)

# How many books have years
num_books_with_year = int(bk['year'].notna().sum())
num_total_books = int(len(bk))
num_review_purchase_ids = int(len(rv_ids))
num_mapped_ids_present_in_books = int(len(intersection))

# After merging with avg ratings per purchase
rv_avg = pd.DataFrame(reviews_data)[['purchase_id','avg_rating']].copy()
rv_avg['avg_rating'] = pd.to_numeric(rv_avg['avg_rating'], errors='coerce')
rv_avg['book_id'] = rv_avg['purchase_id'].str.replace('purchaseid_','bookid_', regex=False)
merged = pd.merge(bk, rv_avg[['book_id','avg_rating']], on='book_id', how='inner')
merged['year'] = merged['details'].apply(extract_year)
merged = merged[merged['year'].notna() & merged['avg_rating'].notna()].copy()
num_merged = int(len(merged))
num_unique_merged_books = int(merged['book_id'].nunique())

books_unique = merged.drop_duplicates(subset=['book_id'])[['book_id','title','year','avg_rating']].copy()
books_unique['decade'] = ((books_unique['year']//10)*10).astype(int).astype(str)+ 's'
decade_stats = books_unique.groupby('decade').agg(book_count=('book_id','nunique'), avg_rating_by_book=('avg_rating','mean')).reset_index()
decade_stats_sorted = decade_stats.sort_values('book_count', ascending=False).to_dict(orient='records')

out = {
    'num_total_books': num_total_books,
    'num_books_with_year': num_books_with_year,
    'num_review_purchase_ids': num_review_purchase_ids,
    'num_mapped_ids_present_in_books': num_mapped_ids_present_in_books,
    'num_merged_rows': num_merged,
    'num_unique_merged_books': num_unique_merged_books,
    'decade_stats': decade_stats_sorted
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_L3tZ220n99FgcRPeZvbhSpxY': ['review'], 'var_call_xqroN816bvY3rq0PLmDfvm3h': ['books_info'], 'var_call_clwW1HpxqxlCKDXJvn9Iim9W': 'file_storage/call_clwW1HpxqxlCKDXJvn9Iim9W.json', 'var_call_mC9eh9kdqR7TFrzmoKhf7oa0': 'file_storage/call_mC9eh9kdqR7TFrzmoKhf7oa0.json', 'var_call_PzRGmZTiF7A8yiwjsrG9INcb': None}

exec(code, env_args)
