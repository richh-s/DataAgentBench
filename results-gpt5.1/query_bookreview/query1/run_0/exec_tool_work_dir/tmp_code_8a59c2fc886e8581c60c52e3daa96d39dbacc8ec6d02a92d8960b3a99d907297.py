code = """import json, pandas as pd
from pathlib import Path

books_path = Path(var_call_Qzwc5YMGXTagO2l6900Gf7Jg)
reviews_path = Path(var_call_8HRMZPeWWUUdVZVOpVi3SHt1)

books = pd.read_json(books_path)
reviews = pd.read_json(reviews_path)

# extract publication year from details
import re

def extract_year(text):
    if not isinstance(text, str):
        return None
    m = re.search(r"(19|20)\d{2}", text)
    return int(m.group(0)) if m else None

books['pub_year'] = books['details'].apply(extract_year)

# map purchase_id -> pub_year by joining on id suffix (number) assuming purchaseid_X <-> bookid_X
books['num_id'] = books['book_id'].str.extract(r"(\d+)").astype(float)
reviews['num_id'] = reviews['purchase_id'].str.extract(r"(\d+)").astype(float)

merged = pd.merge(reviews, books[['num_id','pub_year']], on='num_id', how='left')

merged = merged.dropna(subset=['pub_year'])

# compute average rating per book (distinct books by purchase/book id numeric)
merged['rating'] = merged['rating'].astype(float)
book_avg = merged.groupby('num_id')['rating'].mean().reset_index()

# join back to year
book_avg = book_avg.merge(books[['num_id','pub_year']].drop_duplicates(), on='num_id', how='left')

book_avg = book_avg.dropna(subset=['pub_year'])
book_avg['decade'] = (book_avg['pub_year']//10)*10

# require at least 10 distinct books in decade
decade_stats = book_avg.groupby('decade').agg(avg_rating=('rating','mean'), book_count=('num_id','nunique')).reset_index()
eligible = decade_stats[decade_stats['book_count']>=10]

if eligible.empty:
    result = None
else:
    top = eligible.sort_values('avg_rating', ascending=False).iloc[0]
    result = {"decade": int(top['decade']), "average_rating": float(top['avg_rating']), "book_count": int(top['book_count'])}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Qzwc5YMGXTagO2l6900Gf7Jg': 'file_storage/call_Qzwc5YMGXTagO2l6900Gf7Jg.json', 'var_call_8Qzpj5HDBSSJOhesHMgI1lri': ['books_info'], 'var_call_RPcYiAQJPdKwnQg3i38vMiGv': ['review'], 'var_call_8HRMZPeWWUUdVZVOpVi3SHt1': 'file_storage/call_8HRMZPeWWUUdVZVOpVi3SHt1.json'}

exec(code, env_args)
