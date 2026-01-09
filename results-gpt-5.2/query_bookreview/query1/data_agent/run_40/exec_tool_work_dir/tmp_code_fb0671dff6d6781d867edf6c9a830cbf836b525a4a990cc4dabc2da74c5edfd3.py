code = """import json, re, pandas as pd

# load reviews
path_reviews = var_call_ebD8iC2hfJA7mzRauHHPOcrl
with open(path_reviews, 'r') as f:
    reviews = json.load(f)

# load books
path_books = var_call_4f3VLEiMReCAvoGPqF8VznwE
with open(path_books, 'r') as f:
    books = json.load(f)

# parse year from details
year_re = re.compile(r'\b(18\d{2}|19\d{2}|20\d{2})\b')

def extract_year(details):
    if not details:
        return None
    m = year_re.search(details)
    if not m:
        return None
    y = int(m.group(1))
    if 1800 <= y <= 2026:
        return y
    return None

book_year = {}
for b in books:
    bid = b.get('book_id')
    y = extract_year(b.get('details'))
    if bid and y:
        book_year[bid] = y

# map purchaseid_x -> bookid_x
pid_re = re.compile(r'purchaseid_(\d+)$')
bid_template = 'bookid_{}'

rows = []
for r in reviews:
    pid = r.get('purchase_id')
    rat = r.get('rating')
    if pid is None or rat is None:
        continue
    m = pid_re.search(str(pid))
    if not m:
        continue
    bid = bid_template.format(m.group(1))
    y = book_year.get(bid)
    if y is None:
        continue
    try:
        rating = float(rat)
    except Exception:
        continue
    decade = (y // 10) * 10
    rows.append((bid, decade, rating))

df = pd.DataFrame(rows, columns=['book_id','decade','rating'])
if df.empty:
    out = None
else:
    # keep only books that have been rated (already ensured) and compute decade stats
    g_book = df.groupby(['decade','book_id'], as_index=False)['rating'].mean()  # average rating per book within decade
    g_dec = g_book.groupby('decade').agg(distinct_books=('book_id','nunique'), avg_rating=('rating','mean')).reset_index()
    g_dec = g_dec[g_dec['distinct_books']>=10]
    if g_dec.empty:
        out = None
    else:
        best = g_dec.sort_values(['avg_rating','distinct_books','decade'], ascending=[False,False,True]).iloc[0]
        out = f"{int(best['decade'])}s"

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_4f3VLEiMReCAvoGPqF8VznwE': 'file_storage/call_4f3VLEiMReCAvoGPqF8VznwE.json', 'var_call_pwmDTJEVVxh8jXcBfkMxOdX0': ['review'], 'var_call_ebD8iC2hfJA7mzRauHHPOcrl': 'file_storage/call_ebD8iC2hfJA7mzRauHHPOcrl.json'}

exec(code, env_args)
