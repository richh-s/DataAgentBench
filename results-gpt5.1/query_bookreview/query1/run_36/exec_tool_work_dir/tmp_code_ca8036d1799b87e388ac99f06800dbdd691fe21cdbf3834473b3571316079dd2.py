code = """import pandas as pd, json, re
from collections import defaultdict

# load full books and reviews
import pathlib, os, math
books_path = var_call_wYMZws1pW3sksAt9ajYHX7V8
reviews_path = var_call_fL7klIj9F6YawgduvXP166N3

books = pd.read_json(books_path)
reviews = pd.read_json(reviews_path)

# extract publication year from details using regex on year patterns like 1987, 2004 etc, prefer explicit 'Published' or 'released on <Month> <d>, <year>' or 'on <Month> <d>, <year>'
year_pattern = re.compile(r"(19|20)\d{2}")

def extract_year(text):
    if not isinstance(text,str):
        return None
    # look for 'on <Month ... <year>' first
    m = re.search(r"on [A-Za-z]+ \d{1,2}, ((19|20)\d{2})", text)
    if m:
        return int(m.group(1))
    # look for 'Published by' or 'published by' followed by anything then year
    m = re.search(r"[Pp]ublished[^0-9]*((19|20)\d{2})", text)
    if m:
        return int(m.group(1))
    # fallback first 19xx/20xx
    m = year_pattern.search(text)
    if m:
        return int(m.group(0))
    return None

books['year'] = books['details'].apply(extract_year)
books = books.dropna(subset=['year'])
books['year'] = books['year'].astype(int)
books['decade'] = (books['year'] // 10) * 10

# join reviews to books on purchase_id == book_id
reviews['rating'] = reviews['rating'].astype(float)
merged = reviews.merge(books[['book_id','decade']], left_on='purchase_id', right_on='book_id', how='inner')

# compute per book average rating
book_avg = merged.groupby(['book_id','decade'])['rating'].mean().reset_index(name='book_avg_rating')

# filter decades with at least 10 distinct books that have been rated
decade_counts = book_avg.groupby('decade')['book_id'].nunique().reset_index(name='n_books')
valid_decades = decade_counts[decade_counts['n_books']>=10]

if valid_decades.empty:
    result = None
else:
    # compute decade average of book averages
    decade_avg = book_avg[book_avg['decade'].isin(valid_decades['decade'])].groupby('decade')['book_avg_rating'].mean().reset_index()
    best_row = decade_avg.sort_values('book_avg_rating', ascending=False).iloc[0]
    decade_str = f"{int(best_row['decade'])}s"
    result = decade_str

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_wYMZws1pW3sksAt9ajYHX7V8': 'file_storage/call_wYMZws1pW3sksAt9ajYHX7V8.json', 'var_call_5OzAlMEnBCHf10TS70znluEw': ['books_info'], 'var_call_XouuLpUdoAk50DJPOukblQHx': ['review'], 'var_call_fL7klIj9F6YawgduvXP166N3': 'file_storage/call_fL7klIj9F6YawgduvXP166N3.json'}

exec(code, env_args)
