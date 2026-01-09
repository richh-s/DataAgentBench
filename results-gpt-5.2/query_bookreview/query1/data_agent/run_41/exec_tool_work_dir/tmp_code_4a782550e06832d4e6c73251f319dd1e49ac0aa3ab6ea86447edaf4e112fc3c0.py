code = """import json, re, pandas as pd

# load books details rows
books_src = var_call_0tS2r4JVDXHlJylBJhCCjyf9
if isinstance(books_src, str):
    with open(books_src, 'r', encoding='utf-8') as f:
        books = json.load(f)
else:
    books = books_src

reviews_src = var_call_D8pN6fS2medp8zaVREnVbnwI
if isinstance(reviews_src, str):
    with open(reviews_src, 'r', encoding='utf-8') as f:
        reviews = json.load(f)
else:
    reviews = reviews_src

# parse publication year from details
pat = re.compile(r'\b(18\d{2}|19\d{2}|20\d{2})\b')

def extract_year(details: str):
    if not details:
        return None
    # prefer years near words published/edition/reprint
    s = details
    # find all years with context window
    years = []
    for m in pat.finditer(s):
        y = int(m.group(1))
        if 1800 <= y <= 2026:
            years.append((m.start(), y))
    if not years:
        return None
    # score by proximity to keywords
    kws = ['publish', 'published', 'publication', 'reprint', 'edition', 'released']
    kw_positions = []
    low = s.lower()
    for kw in kws:
        for mm in re.finditer(re.escape(kw), low):
            kw_positions.append(mm.start())
    if not kw_positions:
        # fallback: take earliest plausible year (often publication year)
        return min(y for _, y in years)
    best = None
    best_score = None
    for pos, y in years:
        dist = min(abs(pos-kp) for kp in kw_positions)
        score = dist
        if best_score is None or score < best_score:
            best_score = score
            best = y
    return best

book_year = {}
for r in books:
    bid = r.get('book_id')
    y = extract_year(r.get('details'))
    if bid and y:
        book_year[bid] = y

# map purchase_id -> book_id via numeric suffix
# e.g., purchaseid_186 -> bookid_186

def map_purchase_to_book(pid):
    if pid is None:
        return None
    m = re.search(r'_(\d+)$', str(pid))
    if not m:
        return None
    return f"bookid_{m.group(1)}"

rows = []
for rr in reviews:
    pid = rr.get('purchase_id')
    rating = rr.get('rating')
    try:
        rating_f = float(rating)
    except Exception:
        continue
    bid = map_purchase_to_book(pid)
    y = book_year.get(bid)
    if y is None:
        continue
    decade = (y//10)*10
    rows.append({'book_id': bid, 'decade': decade, 'rating': rating_f})

df = pd.DataFrame(rows)
if df.empty:
    out = {'decade': None}
else:
    # only decades with >=10 distinct books rated
    grp = df.groupby('decade').agg(
        avg_rating=('rating','mean'),
        distinct_books=('book_id', pd.Series.nunique)
    ).reset_index()
    grp = grp[grp['distinct_books']>=10]
    if grp.empty:
        out = {'decade': None}
    else:
        top = grp.sort_values(['avg_rating','distinct_books','decade'], ascending=[False, False, True]).iloc[0]
        out = {'decade': f"{int(top['decade'])}s"}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0tS2r4JVDXHlJylBJhCCjyf9': 'file_storage/call_0tS2r4JVDXHlJylBJhCCjyf9.json', 'var_call_9qCWxMuKTCvpe3ccNh8GgwXy': ['review'], 'var_call_D8pN6fS2medp8zaVREnVbnwI': 'file_storage/call_D8pN6fS2medp8zaVREnVbnwI.json'}

exec(code, env_args)
