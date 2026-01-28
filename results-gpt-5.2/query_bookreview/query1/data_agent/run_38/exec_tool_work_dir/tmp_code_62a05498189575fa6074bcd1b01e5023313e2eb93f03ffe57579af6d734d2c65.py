code = """import json, re, pandas as pd

# load reviews
path_reviews = var_call_fSh5H5u67w18dfcKKbEzc8z6
with open(path_reviews, 'r') as f:
    reviews = json.load(f)
df_r = pd.DataFrame(reviews)
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
df_r = df_r.dropna(subset=['purchase_id','rating'])

# load books (book_id, details)
path_books = var_call_SxSBChi2IUOF1s8xpXFzjHwe
with open(path_books, 'r') as f:
    books = json.load(f)
df_b = pd.DataFrame(books)
df_b = df_b.dropna(subset=['book_id','details'])

# extract year from details
year_re = re.compile(r'\b(18\d{2}|19\d{2}|20\d{2})\b')

def extract_year(s):
    if not isinstance(s, str):
        return None
    m = year_re.search(s)
    if not m:
        return None
    y = int(m.group(1))
    if 1800 <= y <= 2026:
        return y
    return None

df_b['year'] = df_b['details'].map(extract_year)
df_b = df_b.dropna(subset=['year'])
df_b['year'] = df_b['year'].astype(int)
df_b['decade_start'] = (df_b['year']//10)*10

# fuzzy join purchase_id like 'purchaseid_186' to book_id like 'bookid_186'
# extract numeric suffix
suf_re = re.compile(r'(\d+)$')

def suffix_num(x):
    if not isinstance(x, str):
        return None
    m = suf_re.search(x)
    return int(m.group(1)) if m else None

df_r['suf'] = df_r['purchase_id'].map(suffix_num)
df_b['suf'] = df_b['book_id'].map(suffix_num)

df_r = df_r.dropna(subset=['suf'])
df_b = df_b.dropna(subset=['suf'])

# merge on suffix
m = df_r.merge(df_b[['suf','decade_start','book_id']], on='suf', how='inner')

# decades with at least 10 distinct books that have been rated
agg = (m.groupby('decade_start')
         .agg(avg_rating=('rating','mean'), distinct_books=('book_id','nunique'))
         .reset_index())
agg = agg[agg['distinct_books']>=10]
if agg.empty:
    result = None
else:
    top = agg.sort_values(['avg_rating','distinct_books','decade_start'], ascending=[False,False,True]).iloc[0]
    decade_label = f"{int(top['decade_start'])}s"
    result = decade_label

print('__RESULT__:')
print(json.dumps({'decade': result}))"""

env_args = {'var_call_SxSBChi2IUOF1s8xpXFzjHwe': 'file_storage/call_SxSBChi2IUOF1s8xpXFzjHwe.json', 'var_call_enV3SLMGPObT8aOhjATPGq6v': ['review'], 'var_call_fSh5H5u67w18dfcKKbEzc8z6': 'file_storage/call_fSh5H5u67w18dfcKKbEzc8z6.json'}

exec(code, env_args)
