code = """import json, re, pandas as pd

# load reviews
path_reviews = var_call_Y5ETerWl3Dd5iKzUzRqNJ0Hq
with open(path_reviews, 'r') as f:
    reviews = json.load(f)

df_rev = pd.DataFrame(reviews)
df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')
df_rev = df_rev.dropna(subset=['purchase_id','rating'])

# books details
path_books = var_call_MZLTPHH2aePnOD8FKUcRwYLr
with open(path_books, 'r') as f:
    books = json.load(f)

df_books = pd.DataFrame(books)

def extract_year(details):
    if details is None:
        return None
    s = str(details)
    # prioritize patterns like 'on Month d, YYYY' or 'on January 1, 2004'
    m = re.search(r'\b(?:on|released on)\s+[A-Za-z]+\s+\d{1,2},\s*(\d{4})\b', s)
    if m:
        return int(m.group(1))
    # then any standalone year 1500-2099
    m = re.search(r'\b(1[5-9]\d{2}|20\d{2})\b', s)
    if m:
        return int(m.group(1))
    return None

df_books['year'] = df_books['details'].apply(extract_year)
df_books = df_books.dropna(subset=['book_id','year'])
df_books['year'] = df_books['year'].astype(int)

# join purchaseid_x to bookid_x via numeric suffix
# extract numeric id
for col in ['purchase_id']:
    df_rev['num'] = df_rev['purchase_id'].astype(str).str.extract(r'(\d+)$')[0]
df_books['num'] = df_books['book_id'].astype(str).str.extract(r'(\d+)$')[0]

df_join = df_rev.merge(df_books[['book_id','year','num']], on='num', how='inner')

# only decades with at least 10 distinct books that have been rated (at least 1 review after join)
df_join['decade_start'] = (df_join['year']//10)*10

g = df_join.groupby('decade_start').agg(
    avg_rating=('rating','mean'),
    distinct_books=('book_id', pd.Series.nunique)
).reset_index()

g = g[g['distinct_books']>=10]

if g.empty:
    result = None
else:
    top = g.sort_values(['avg_rating','distinct_books','decade_start'], ascending=[False,False,True]).iloc[0]
    decade_label = f"{int(top['decade_start'])}s"
    result = decade_label

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_MZLTPHH2aePnOD8FKUcRwYLr': 'file_storage/call_MZLTPHH2aePnOD8FKUcRwYLr.json', 'var_call_JYV2YEpLzHLgir67OOPpDot1': ['review'], 'var_call_Y5ETerWl3Dd5iKzUzRqNJ0Hq': 'file_storage/call_Y5ETerWl3Dd5iKzUzRqNJ0Hq.json'}

exec(code, env_args)
