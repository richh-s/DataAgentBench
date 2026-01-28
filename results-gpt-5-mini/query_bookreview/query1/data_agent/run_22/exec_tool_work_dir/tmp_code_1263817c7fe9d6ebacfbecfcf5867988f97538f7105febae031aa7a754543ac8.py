code = """import json
import re
import pandas as pd

# Load data from storage file paths
books_path = var_call_y772XmPnzuFBSUzIrQ0ieuwP
reviews_path = var_call_f2wELhABQt7xcqD8LhhZCPF6

with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Create DataFrames
df_books = pd.DataFrame(books)
# keep only needed columns
if 'book_id' not in df_books.columns:
    print('__RESULT__:')
    print(json.dumps('no_book_id_in_books'))
else:
    df_reviews = pd.DataFrame(reviews)

    # normalize ratings
    df_reviews = df_reviews[df_reviews['rating'].notnull()].copy()
    df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')
    df_reviews = df_reviews[df_reviews['rating'].notnull()]

    # map purchaseid to bookid by replacing prefix
    def purchase_to_book(pid):
        if not isinstance(pid, str):
            return None
        return pid.replace('purchaseid_', 'bookid_')

    df_reviews['book_id'] = df_reviews['purchase_id'].apply(purchase_to_book)

    # compute per-book average rating
    book_avg = df_reviews.groupby('book_id')['rating'].mean().reset_index().rename(columns={'rating':'book_avg_rating'})

    # extract year from books.details
    def extract_year(details):
        if not isinstance(details, str):
            return None
        # find first 4-digit year between 1000 and 2099
        m = re.search(r"\b(1[0-9]{3}|20[0-9]{2})\b", details)
        if m:
            try:
                return int(m.group(0))
            except:
                return None
        return None

    df_books['pub_year'] = df_books['details'].apply(extract_year)
    # merge with book_avg
    df_merged = pd.merge(book_avg, df_books[['book_id','pub_year']], on='book_id', how='left')

    # drop rows without pub_year
    df_merged = df_merged[df_merged['pub_year'].notnull()].copy()
    df_merged['pub_year'] = df_merged['pub_year'].astype(int)
    df_merged['decade'] = (df_merged['pub_year']//10*10).astype(int).astype(str) + 's'

    # group by decade: count distinct books and average of book averages
    grp = df_merged.groupby('decade').agg(n_books=('book_id','nunique'), decade_avg_rating=('book_avg_rating','mean')).reset_index()

    # filter decades with at least 10 distinct books
    grp_filtered = grp[grp['n_books']>=10]

    if grp_filtered.empty:
        result = None
    else:
        # find decade with highest average rating; in case of ties take the one with highest avg and then smallest decade? we'll pick the first
        best = grp_filtered.sort_values(['decade_avg_rating','decade'], ascending=[False, True]).iloc[0]
        result = {
            'decade': best['decade'],
            'average_rating': round(float(best['decade_avg_rating']), 4),
            'n_books': int(best['n_books'])
        }

    # print result as JSON string
    print('__RESULT__:')
    print(json.dumps(result))"""

env_args = {'var_call_sGNWgtrDyRD48heiY52PNDie': ['review'], 'var_call_yHZ0hQvdPocQKH2pLJ9e5pNm': ['books_info'], 'var_call_y772XmPnzuFBSUzIrQ0ieuwP': 'file_storage/call_y772XmPnzuFBSUzIrQ0ieuwP.json', 'var_call_ACiSEhncOtES40qdbWPc8joC': ['review'], 'var_call_f2wELhABQt7xcqD8LhhZCPF6': 'file_storage/call_f2wELhABQt7xcqD8LhhZCPF6.json'}

exec(code, env_args)
