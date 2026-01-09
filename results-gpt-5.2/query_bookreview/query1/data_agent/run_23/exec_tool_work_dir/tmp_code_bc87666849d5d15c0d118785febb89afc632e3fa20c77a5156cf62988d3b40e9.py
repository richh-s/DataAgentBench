code = """import json, re
import pandas as pd

# load reviews
path_reviews = var_call_aHniMSxgFEcKVulXB0amBzwY
with open(path_reviews, 'r') as f:
    reviews = json.load(f)
df_r = pd.DataFrame(reviews)
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
df_r = df_r.dropna(subset=['purchase_id','rating'])

# load books details
path_books = var_call_0TZRbGdXubIhjpsNAVg8zNMj
with open(path_books, 'r') as f:
    books = json.load(f)
df_b = pd.DataFrame(books)

def extract_year(details):
    if details is None:
        return None
    s = str(details)
    m = re.search(r'\b(19\d{2}|20\d{2})\b', s)
    if not m:
        return None
    y = int(m.group(1))
    if 1800 <= y <= 2026:
        return y
    return None

df_b['year'] = df_b['details'].apply(extract_year)

def num_suffix_to_id(x, prefix):
    m = re.search(r'(\d+)$', str(x))
    if not m:
        return None
    return f"{prefix}_{int(m.group(1))}"

df_r['book_id'] = df_r['purchase_id'].apply(lambda x: num_suffix_to_id(x,'bookid'))

# join reviews to books
j = df_r.merge(df_b[['book_id','year']], on='book_id', how='inner')
j = j.dropna(subset=['year'])
j['year'] = j['year'].astype(int)

# decade label
def decade_label(y):
    d = (y//10)*10
    return f"{d}s"

j['decade'] = j['year'].apply(decade_label)

# compute per book avg rating, then per decade average across distinct books
book_avg = j.groupby(['decade','book_id'], as_index=False)['rating'].mean()
dec = book_avg.groupby('decade').agg(distinct_books=('book_id','nunique'), avg_rating=('rating','mean')).reset_index()
dec = dec[dec['distinct_books']>=10]
if dec.empty:
    out = {"decade": None}
else:
    best = dec.sort_values(['avg_rating','distinct_books','decade'], ascending=[False,False,True]).iloc[0]
    out = {"decade": best['decade'], "avg_rating": float(best['avg_rating']), "distinct_books": int(best['distinct_books'])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0TZRbGdXubIhjpsNAVg8zNMj': 'file_storage/call_0TZRbGdXubIhjpsNAVg8zNMj.json', 'var_call_lKMsyIe3G1WM2Njg8NEgSMFZ': ['review'], 'var_call_18DN12ok8m2O3w3aHqoiHwlg': ['books_info'], 'var_call_aHniMSxgFEcKVulXB0amBzwY': 'file_storage/call_aHniMSxgFEcKVulXB0amBzwY.json'}

exec(code, env_args)
