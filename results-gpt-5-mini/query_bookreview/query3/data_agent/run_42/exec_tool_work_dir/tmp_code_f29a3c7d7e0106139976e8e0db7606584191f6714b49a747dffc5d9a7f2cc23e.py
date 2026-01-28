code = """import json
import pandas as pd
import re

with open(var_call_bmIgUAXKjX8yjxSfPgATyeTy, 'r') as f:
    reviews = json.load(f)
with open(var_call_PqDutk8xXQUKu7IuHjYHFlrN, 'r') as f:
    books = json.load(f)

df_r = pd.DataFrame(reviews)
df_b = pd.DataFrame(books)

# Clean ratings and times
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
df_r['review_time'] = pd.to_datetime(df_r['review_time'], errors='coerce')

# Filter reviews from 2020 onwards
df_r = df_r[df_r['review_time'] >= pd.Timestamp('2020-01-01')].copy()

# Map purchase_id to book_id using digits

def to_bookid(pid):
    if pd.isna(pid):
        return None
    m = re.search(r"(\d+)", str(pid))
    if m:
        return 'bookid_' + m.group(1)
    return None

if 'purchase_id' in df_r.columns:
    df_r['book_id'] = df_r['purchase_id'].apply(to_bookid)
else:
    df_r['book_id'] = None

# Identify children's books
if 'categories' in df_b.columns:
    df_b['is_children'] = df_b['categories'].astype(str).str.contains("Children's Books", na=False)
else:
    df_b['is_children'] = False

children = df_b[df_b['is_children']].copy()

# Merge
merged = pd.merge(df_r, children[['book_id', 'title']], on='book_id', how='inner')

# Compute averages
result = []
if not merged.empty:
    grp = merged.groupby(['book_id', 'title']).agg(avg_rating=('rating', 'mean'), review_count=('rating', 'count')).reset_index()
    grp['avg_rating'] = grp['avg_rating'].round(3)
    res = grp[grp['avg_rating'] >= 4.5].sort_values(['avg_rating', 'review_count'], ascending=[False, False])
    result = res.to_dict(orient='records')

for r in result:
    r['avg_rating'] = float(r['avg_rating'])
    r['review_count'] = int(r['review_count'])

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_V4Ay7XT6DZjxMcFI1xYIrbr3': ['review'], 'var_call_xjSOnwYTFge2cGaFGNaZqfAm': ['books_info'], 'var_call_bmIgUAXKjX8yjxSfPgATyeTy': 'file_storage/call_bmIgUAXKjX8yjxSfPgATyeTy.json', 'var_call_PqDutk8xXQUKu7IuHjYHFlrN': 'file_storage/call_PqDutk8xXQUKu7IuHjYHFlrN.json', 'var_call_1xNuphlCke72czMqZ5Vtt7iF': {'review_columns': ['purchase_id', 'rating', 'review_time', 'title'], 'books_columns': ['book_id', 'title', 'categories', 'details'], 'review_len': 100, 'books_len': 200, 'review_head': [{'purchase_id': 'purchaseid_186', 'rating': '4', 'review_time': '2012-11-24 18:52:00', 'title': 'Ha! On me!  I thought this was a cookbook!'}, {'purchase_id': 'purchaseid_191', 'rating': '4', 'review_time': '2015-12-31 13:35:00', 'title': 'Four Stars'}, {'purchase_id': 'purchaseid_190', 'rating': '4', 'review_time': '2013-05-05 10:47:00', 'title': 'A wonderful adventure in France'}], 'books_head': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'categories': '["Books", "Reference", "Words, Language & Grammar"]', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}]}}

exec(code, env_args)
