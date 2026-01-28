code = """import json
import pandas as pd
import re
from datetime import datetime

# Load data
with open(var_call_1FcBgCKDIm7pwEtxeM28e23N, 'r') as f:
    reviews = json.load(f)
with open(var_call_17MEPLWTrGD9QV5OvoSDLmmZ, 'r') as f:
    books = json.load(f)

rev_df = pd.DataFrame(reviews)
books_df = pd.DataFrame(books)

# Normalize review_time and filter from 2020-01-01
rev_df['review_time'] = pd.to_datetime(rev_df['review_time'], errors='coerce')
rev_df = rev_df[rev_df['review_time'] >= pd.to_datetime('2020-01-01')]
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
rev_df = rev_df.dropna(subset=['rating','purchase_id'])

# Map purchase_id to book_id using numeric suffix
def purchase_to_bookid(p):
    if not isinstance(p, str):
        return None
    m = re.search(r'(\d+)$', p)
    if m:
        return f"bookid_{m.group(1)}"
    return None

rev_df['book_id'] = rev_df['purchase_id'].apply(purchase_to_bookid)
rev_df = rev_df.dropna(subset=['book_id'])

# Merge on book_id
merged = rev_df.merge(books_df[['book_id','title','categories']], on='book_id', how='left', suffixes=('_rev','_book'))

# Determine book title: prefer books table title, else use review title
if 'title_book' in merged.columns:
    merged['book_title'] = merged['title_book'].fillna(merged.get('title_rev'))
else:
    # fallback if suffixes not applied
    merged['book_title'] = merged['title'] if 'title' in merged.columns else merged.get('title_rev')

# Drop rows without categories or book_title
merged = merged.dropna(subset=['categories','book_title'])

# Filter categories containing "Children's Books"
merged_children = merged[merged['categories'].str.contains("Children's Books", na=False)]

# Group by book_id and book_title
grouped = merged_children.groupby(['book_id','book_title']).agg(average_rating=('rating','mean'), review_count=('rating','count')).reset_index()

# Filter average_rating >= 4.5
result_df = grouped[grouped['average_rating'] >= 4.5].sort_values(by=['average_rating','review_count'], ascending=[False, False])

# Build result list
result = []
for _, row in result_df.iterrows():
    result.append({'book_id': row['book_id'], 'title': row['book_title'], 'average_rating': round(float(row['average_rating']),3), 'review_count': int(row['review_count'])})

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_mVVpJoNT9uzr2PlzsQWzbkqG': ['review'], 'var_call_tRrgSzlaazg8qOSlICKzoF4A': ['books_info'], 'var_call_1FcBgCKDIm7pwEtxeM28e23N': 'file_storage/call_1FcBgCKDIm7pwEtxeM28e23N.json', 'var_call_17MEPLWTrGD9QV5OvoSDLmmZ': 'file_storage/call_17MEPLWTrGD9QV5OvoSDLmmZ.json', 'var_call_NrwmV37GeuUyHgWofcpQTJXY': {'rev_columns': ['purchase_id', 'title', 'rating', 'review_time'], 'books_columns': ['book_id', 'title', 'categories', 'details'], 'rev_sample_first_row': {'purchase_id': 'purchaseid_186', 'title': 'Ha! On me!  I thought this was a cookbook!', 'rating': '4', 'review_time': '2012-11-24 18:52:00'}, 'books_sample_first_row': {'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}}}

exec(code, env_args)
