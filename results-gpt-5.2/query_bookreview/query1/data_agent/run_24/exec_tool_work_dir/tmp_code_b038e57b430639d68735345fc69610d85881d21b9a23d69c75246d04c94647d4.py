code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

books = load_records(var_call_lJEvhsZqnCcXEYKqRoYY6Vqm)  # book_id, details
reviews = load_records(var_call_yey3FZBwhBjLiXO4JwO4REWg)  # purchase_id, rating

# Parse year from details
year_re = re.compile(r'(?:\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\b\s+\d{1,2},\s+)?(\d{4})')

def extract_year(details):
    if not details:
        return None
    # prioritize patterns around "Published"/"Publication"
    m = re.search(r'(?i)published[^\d]{0,40}(\d{4})', details)
    if m:
        y = int(m.group(1))
        if 1500 <= y <= 2026:
            return y
    # else take first plausible year
    for m in year_re.finditer(details):
        y = int(m.group(1))
        if 1500 <= y <= 2026:
            return y
    return None

book_year = {}
for r in books:
    y = extract_year(r.get('details'))
    if y is not None:
        book_year[r['book_id']] = y

# map purchaseid_x -> bookid_x (fuzzy join via numeric suffix)

def pid_to_bid(pid):
    if pid is None:
        return None
    m = re.search(r'(\d+)$', str(pid))
    if not m:
        return None
    return f"bookid_{int(m.group(1))}"

rows = []
for rr in reviews:
    bid = pid_to_bid(rr.get('purchase_id'))
    if bid in book_year:
        try:
            rating = float(rr.get('rating'))
        except Exception:
            continue
        rows.append((bid, book_year[bid], rating))

df = pd.DataFrame(rows, columns=['book_id','year','rating'])
if df.empty:
    out = {"error":"No joined review/book-year records found"}
else:
    df['decade_start'] = (df['year']//10)*10
    # per-decade stats: average of all ratings; require >=10 distinct books rated
    g = df.groupby('decade_start').agg(
        avg_rating=('rating','mean'),
        distinct_books=('book_id','nunique'),
        n_ratings=('rating','size')
    ).reset_index()
    g = g[g['distinct_books']>=10].copy()
    if g.empty:
        out = {"error":"No decade has at least 10 distinct rated books"}
    else:
        top = g.sort_values(['avg_rating','distinct_books','n_ratings'], ascending=[False,False,False]).iloc[0]
        decade_label = f"{int(top['decade_start'])}s"
        out = {"decade": decade_label, "avg_rating": float(top['avg_rating']), "distinct_books": int(top['distinct_books']), "n_ratings": int(top['n_ratings'])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ko75vxM2z2wq2bKSK022Fj7I': 'file_storage/call_ko75vxM2z2wq2bKSK022Fj7I.json', 'var_call_lJEvhsZqnCcXEYKqRoYY6Vqm': 'file_storage/call_lJEvhsZqnCcXEYKqRoYY6Vqm.json', 'var_call_TgKWG0jQHEQnwqZERq2MxYYB': 'file_storage/call_TgKWG0jQHEQnwqZERq2MxYYB.json', 'var_call_uApDMq5byIES6bkhVWWGE0e9': ['books_info'], 'var_call_h1NtfeyL9z2QmQCb7DpcPe83': ['review'], 'var_call_yey3FZBwhBjLiXO4JwO4REWg': 'file_storage/call_yey3FZBwhBjLiXO4JwO4REWg.json'}

exec(code, env_args)
