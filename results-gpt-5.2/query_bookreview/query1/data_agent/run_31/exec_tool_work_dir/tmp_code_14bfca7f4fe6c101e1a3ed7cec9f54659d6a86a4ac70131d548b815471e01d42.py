code = """import json, re, pandas as pd

# load reviews
path_reviews = var_call_wLoratoiHeLMbkxuw5jhJxRj
with open(path_reviews, 'r') as f:
    reviews = json.load(f)

# load books details
path_books = var_call_NWdBiWYXC5Kur54ZoMeb1QPD
with open(path_books, 'r') as f:
    books = json.load(f)

# map purchaseid_N -> bookid_N via numeric suffix
re_pid = re.compile(r'(?:purchaseid_|bookid_)(\d+)$')

def get_num(s):
    if s is None:
        return None
    m = re_pid.search(str(s))
    return int(m.group(1)) if m else None

# extract publication year from details text
re_year = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_year(details):
    if not details:
        return None
    # prefer patterns around 'released on' or 'published'
    txt = str(details)
    # find all years
    years = [int(y) for y in re_year.findall(txt)]
    if not years:
        return None
    # heuristic: choose earliest year mentioned (often publication date vs later reprint)
    return min(years)

book_num_to_year = {}
for b in books:
    n = get_num(b.get('book_id'))
    if n is None:
        continue
    y = extract_year(b.get('details'))
    if y is not None:
        book_num_to_year[n] = y

# join reviews to years
rows = []
for r in reviews:
    n = get_num(r.get('purchase_id'))
    if n is None:
        continue
    y = book_num_to_year.get(n)
    if y is None:
        continue
    try:
        rating = float(r.get('rating'))
    except Exception:
        continue
    decade = (y // 10) * 10
    rows.append((decade, n, rating))

df = pd.DataFrame(rows, columns=['decade','book_num','rating'])

# compute per-decade: average rating across all reviews, but only for decades with >=10 distinct books rated
agg = df.groupby('decade').agg(avg_rating=('rating','mean'), distinct_books=('book_num','nunique'))
agg = agg[agg['distinct_books'] >= 10]
if agg.empty:
    result = None
else:
    top_decade = agg.sort_values(['avg_rating','distinct_books'], ascending=[False, False]).index[0]
    result = f"{top_decade}s"

print('__RESULT__:')
print(json.dumps({'decade': result}))"""

env_args = {'var_call_NWdBiWYXC5Kur54ZoMeb1QPD': 'file_storage/call_NWdBiWYXC5Kur54ZoMeb1QPD.json', 'var_call_8jthKBJQbooXzMpAmP1JVCdW': ['review'], 'var_call_wLoratoiHeLMbkxuw5jhJxRj': 'file_storage/call_wLoratoiHeLMbkxuw5jhJxRj.json'}

exec(code, env_args)
