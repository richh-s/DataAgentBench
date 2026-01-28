code = """import json
import pandas as pd
import re

# load data from storage-provided file paths
books_path = var_call_gnZG8tVilNJ3jxZ1ZUWE6fh3
reviews_path = var_call_Q9jADMba7TegRFtObg2fbfPd

with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# normalize rating to numeric
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')

# map purchase_id to book_id by replacing prefix
def map_purchase_to_book(pid):
    if pid is None:
        return None
    if pid.startswith('bookid_'):
        return pid
    if pid.startswith('purchaseid_'):
        return 'bookid_' + pid.split('_',1)[1]
    # fallback: try to extract trailing number
    m = re.search(r'(\d+)$', pid)
    if m:
        return 'bookid_' + m.group(1)
    return pid

reviews_df['book_id'] = reviews_df['purchase_id'].apply(map_purchase_to_book)

# merge
merged = reviews_df.merge(books_df, on='book_id', how='left')

# extract year from details

def extract_year(details):
    if not isinstance(details, str):
        return None
    years = re.findall(r"\b(\d{4})\b", details)
    for y in years:
        try:
            yi = int(y)
        except:
            continue
        if 1000 <= yi <= 2023:
            return yi
    return None

merged['pub_year'] = merged['details'].apply(extract_year)

# drop rows without pub_year or rating or book_id
merged = merged[merged['pub_year'].notna() & merged['rating'].notna() & merged['book_id'].notna()]

# compute decade per book
merged['decade'] = (merged['pub_year'] // 10 * 10).astype(int).astype(str) + 's'

# compute per-book average rating and decade
book_avg = (merged.groupby(['book_id','decade'])['rating']
            .mean()
            .reset_index()
            .rename(columns={'rating':'book_avg_rating'}))

# compute per-decade stats
decade_stats = (book_avg.groupby('decade')
                .agg(book_count=('book_id','nunique'),
                     decade_avg_rating=('book_avg_rating','mean'))
                .reset_index())

# filter decades with at least 10 distinct books
eligible = decade_stats[decade_stats['book_count'] >= 10]

if eligible.empty:
    result = {'decade': None, 'avg_rating': None, 'book_count': 0}
else:
    # find decade with highest average rating
    best = eligible.sort_values(['decade_avg_rating','decade'], ascending=[False, True]).iloc[0]
    result = {
        'decade': best['decade'],
        'avg_rating': round(float(best['decade_avg_rating']), 4),
        'book_count': int(best['book_count'])
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_mmyodO94mooeIg74xVlPSzfb': ['review'], 'var_call_dSirAGmDPY0zvpJtil6kCoaj': ['books_info'], 'var_call_gnZG8tVilNJ3jxZ1ZUWE6fh3': 'file_storage/call_gnZG8tVilNJ3jxZ1ZUWE6fh3.json', 'var_call_Q9jADMba7TegRFtObg2fbfPd': 'file_storage/call_Q9jADMba7TegRFtObg2fbfPd.json'}

exec(code, env_args)
