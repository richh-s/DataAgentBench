code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

books = load_records(var_call_KSikr6z8B6WVZxS05OGjgOvT)
reviews = load_records(var_call_aJMM7HvGzZQ3HCBqTfU29tfo)

# Extract 4-digit publication year from details
year_pat = re.compile(r'\b(18\d{2}|19\d{2}|20\d{2})\b')

def extract_year(s):
    if not s:
        return None
    m = year_pat.search(s)
    if not m:
        return None
    y = int(m.group(1))
    if 1800 <= y <= 2026:
        return y
    return None

book_year = {}
for r in books:
    y = extract_year(r.get('details',''))
    if y is not None:
        book_year[r['book_id']] = y

# Fuzzy join purchase_id -> book_id by numeric suffix
suffix_pat = re.compile(r'(\d+)$')

def suffix(s):
    m = suffix_pat.search(s or '')
    return m.group(1) if m else None

book_by_suffix = {}
for bid in book_year.keys():
    suf = suffix(bid)
    if suf:
        book_by_suffix.setdefault(suf, bid)

rows = []
for rr in reviews:
    pid = rr.get('purchase_id')
    rat = rr.get('rating')
    try:
        ratf = float(rat)
    except Exception:
        continue
    suf = suffix(pid)
    if not suf:
        continue
    bid = book_by_suffix.get(suf)
    if not bid:
        continue
    y = book_year.get(bid)
    if y is None:
        continue
    decade = (y//10)*10
    rows.append((bid, decade, ratf))

df = pd.DataFrame(rows, columns=['book_id','decade','rating'])

# Distinct books rated per decade
if df.empty:
    out = {"decade": None, "avg_rating": None, "distinct_books": 0}
else:
    grp = df.groupby('decade').agg(avg_rating=('rating','mean'), distinct_books=('book_id', pd.Series.nunique))
    grp = grp[grp['distinct_books']>=10]
    if grp.empty:
        out = {"decade": None, "avg_rating": None, "distinct_books": 0}
    else:
        best_decade = grp['avg_rating'].idxmax()
        out = {"decade": f"{int(best_decade)}s", "avg_rating": float(grp.loc[best_decade,'avg_rating']), "distinct_books": int(grp.loc[best_decade,'distinct_books'])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_KSikr6z8B6WVZxS05OGjgOvT': 'file_storage/call_KSikr6z8B6WVZxS05OGjgOvT.json', 'var_call_Sr37Qat5tyCqg3xP39bQQUSG': ['review'], 'var_call_aJMM7HvGzZQ3HCBqTfU29tfo': 'file_storage/call_aJMM7HvGzZQ3HCBqTfU29tfo.json'}

exec(code, env_args)
