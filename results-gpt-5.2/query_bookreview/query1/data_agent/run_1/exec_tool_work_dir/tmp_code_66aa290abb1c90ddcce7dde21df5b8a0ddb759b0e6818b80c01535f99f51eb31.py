code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

books = load_records(var_call_MNQgzA13DEbi6aQCwQBcWpKc)
reviews = load_records(var_call_QfZG6itGWLtFbRQlCLEfnmpY)

# Parse publication year from details
pat = re.compile(r'\b(19\d{2}|20\d{2})\b')
book_year = {}
for r in books:
    det = r.get('details') or ''
    years = [int(y) for y in pat.findall(det)]
    if years:
        # choose earliest plausible year as publication year
        year = min(years)
        book_year[r['book_id']] = year

# map purchaseid_x -> bookid_x when possible
pid_to_bid = {}
for pid in {rr.get('purchase_id') for rr in reviews if rr.get('purchase_id') is not None}:
    m = re.match(r'purchaseid_(\d+)$', str(pid))
    if m:
        pid_to_bid[pid] = f"bookid_{m.group(1)}"

rows = []
for rr in reviews:
    pid = rr.get('purchase_id')
    bid = pid_to_bid.get(pid)
    if not bid:
        continue
    year = book_year.get(bid)
    if not year:
        continue
    try:
        rating = float(rr.get('rating'))
    except Exception:
        continue
    decade = (year // 10) * 10
    rows.append((bid, decade, rating))

df = pd.DataFrame(rows, columns=['book_id','decade','rating'])
# Need decades with at least 10 distinct books that have been rated
if df.empty:
    out = None
else:
    grp = df.groupby('decade').agg(avg_rating=('rating','mean'), distinct_books=('book_id','nunique'))
    grp = grp[grp['distinct_books']>=10]
    if grp.empty:
        out = None
    else:
        best_decade = grp.sort_values(['avg_rating','distinct_books'], ascending=[False,False]).index[0]
        out = f"{best_decade}s"

print('__RESULT__:')
print(json.dumps({'decade': out}))"""

env_args = {'var_call_MNQgzA13DEbi6aQCwQBcWpKc': 'file_storage/call_MNQgzA13DEbi6aQCwQBcWpKc.json', 'var_call_lhFopJlGz2BY1YMfdBaoVVf0': ['review'], 'var_call_QfZG6itGWLtFbRQlCLEfnmpY': 'file_storage/call_QfZG6itGWLtFbRQlCLEfnmpY.json'}

exec(code, env_args)
