code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

books = load_records(var_call_0tnYHcqM666zasgzs902l0xE)
reviews = load_records(var_call_LyhItPO07QGB7uY64QxaAPlq)

# Extract publication year from details text
pat_year = re.compile(r'\b(19\d{2}|20\d{2})\b')
book_year = {}
for r in books:
    d = r.get('details') or ''
    # Prefer year near 'Published'/'released' etc by taking first found year
    m = pat_year.search(d)
    if m:
        book_year[r['book_id']] = int(m.group(1))

# Fuzzy join purchase_id -> book_id by numeric suffix
suf_pat = re.compile(r'(\d+)$')

# Map book numeric suffix to book_id (if duplicates, keep first)
num_to_book = {}
for bid in book_year.keys():
    m = suf_pat.search(bid)
    if m:
        num_to_book.setdefault(m.group(1), bid)

rows = []
for rv in reviews:
    pid = rv.get('purchase_id')
    m = suf_pat.search(pid or '')
    if not m:
        continue
    num = m.group(1)
    bid = num_to_book.get(num)
    if not bid:
        continue
    yr = book_year.get(bid)
    if not yr:
        continue
    try:
        rating = float(rv.get('rating'))
    except Exception:
        continue
    rows.append((bid, yr, rating))

df = pd.DataFrame(rows, columns=['book_id','year','rating'])
if df.empty:
    out = {'error':'No joined records with publication year and ratings found'}
else:
    df['decade_start'] = (df['year']//10)*10
    # distinct books rated per decade
    grouped = df.groupby('decade_start').agg(
        avg_rating=('rating','mean'),
        distinct_books=('book_id', pd.Series.nunique)
    ).reset_index()
    eligible = grouped[grouped['distinct_books']>=10].copy()
    if eligible.empty:
        out = {'error':'No decades with at least 10 distinct rated books'}
    else:
        best = eligible.sort_values(['avg_rating','distinct_books'], ascending=[False,False]).iloc[0]
        decade = int(best['decade_start'])
        out = {'decade': f"{decade}s", 'avg_rating': float(best['avg_rating']), 'distinct_books': int(best['distinct_books'])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0tnYHcqM666zasgzs902l0xE': 'file_storage/call_0tnYHcqM666zasgzs902l0xE.json', 'var_call_DGITMZgJsNiHvyDssdLsE2D8': ['review'], 'var_call_LyhItPO07QGB7uY64QxaAPlq': 'file_storage/call_LyhItPO07QGB7uY64QxaAPlq.json'}

exec(code, env_args)
