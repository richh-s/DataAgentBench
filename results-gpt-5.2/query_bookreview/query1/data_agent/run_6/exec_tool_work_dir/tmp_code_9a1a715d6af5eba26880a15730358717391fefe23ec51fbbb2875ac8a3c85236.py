code = """import json, re, pandas as pd

# load reviews
path_reviews = var_call_GE06GXCKrhDJAsH2kKoh2juB
with open(path_reviews, 'r') as f:
    reviews = json.load(f)
df_r = pd.DataFrame(reviews)
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
df_r = df_r.dropna(subset=['purchase_id','rating'])

# load book details
path_books = var_call_JBhMxeNYcHMITB8I6SW6Yd9l
with open(path_books, 'r') as f:
    books = json.load(f)
df_b = pd.DataFrame(books)

# extract publication year from details
pat = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_year(s):
    if not isinstance(s, str):
        return None
    m = pat.search(s)
    if not m:
        return None
    y = int(m.group(1))
    if 1500 <= y <= 2026:
        return y
    return None

df_b['pub_year'] = df_b['details'].map(extract_year)
df_b = df_b.dropna(subset=['book_id','pub_year'])
df_b['pub_year'] = df_b['pub_year'].astype(int)

# fuzzy join purchaseid_X to bookid_X by shared numeric suffix
# extract suffix numbers
suffix_pat = re.compile(r'(\d+)$')

def suffix_num(x):
    if not isinstance(x, str):
        return None
    m = suffix_pat.search(x)
    return int(m.group(1)) if m else None

df_r['sid'] = df_r['purchase_id'].map(suffix_num)
df_b['sid'] = df_b['book_id'].map(suffix_num)

joined = pd.merge(df_r, df_b[['sid','pub_year']], on='sid', how='inner')

# compute decade, require at least 10 distinct books rated (distinct sid)
joined['decade_start'] = (joined['pub_year']//10)*10

g = joined.groupby('decade_start').agg(
    avg_rating=('rating','mean'),
    distinct_books=('sid','nunique')
).reset_index()

g = g[g['distinct_books']>=10]

if g.empty:
    ans = None
else:
    top = g.sort_values(['avg_rating','distinct_books','decade_start'], ascending=[False,False,True]).iloc[0]
    decade = f"{int(top['decade_start'])}s"
    ans = decade

print('__RESULT__:')
print(json.dumps({'decade': ans}))"""

env_args = {'var_call_JBhMxeNYcHMITB8I6SW6Yd9l': 'file_storage/call_JBhMxeNYcHMITB8I6SW6Yd9l.json', 'var_call_PqKpGbUw9nwoo3NcVVJDtvHg': ['review'], 'var_call_GE06GXCKrhDJAsH2kKoh2juB': 'file_storage/call_GE06GXCKrhDJAsH2kKoh2juB.json'}

exec(code, env_args)
