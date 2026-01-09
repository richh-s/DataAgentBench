code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

books = load_records(var_call_puJwwaQmoN0raYq4d5TYz0RV)
reviews = load_records(var_call_LyhItPO07QGB7uY64QxaAPlq)

pat_year = re.compile(r'\b(19\d{2}|20\d{2})\b')
book_year = {}
for r in books:
    d = r.get('details') or ''
    m = pat_year.search(d)
    if m:
        book_year[r['book_id']] = int(m.group(1))

suf_pat = re.compile(r'(\d+)$')
num_to_book = {}
for bid in book_year:
    m = suf_pat.search(bid)
    if m:
        num_to_book[m.group(1)] = bid

rows=[]
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
    out={'error':'No joined records with publication year and ratings found','books_with_year':len(book_year),'reviews':len(reviews)}
else:
    df['decade_start']=(df['year']//10)*10
    grouped=df.groupby('decade_start').agg(avg_rating=('rating','mean'),distinct_books=('book_id','nunique')).reset_index()
    eligible=grouped[grouped['distinct_books']>=10].copy()
    if eligible.empty:
        out={'error':'No decades with at least 10 distinct rated books','grouped':grouped.sort_values('distinct_books',ascending=False).to_dict('records')}
    else:
        best=eligible.sort_values(['avg_rating','distinct_books'],ascending=[False,False]).iloc[0]
        decade=int(best['decade_start'])
        out={'decade':f"{decade}s"}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0tnYHcqM666zasgzs902l0xE': 'file_storage/call_0tnYHcqM666zasgzs902l0xE.json', 'var_call_DGITMZgJsNiHvyDssdLsE2D8': ['review'], 'var_call_LyhItPO07QGB7uY64QxaAPlq': 'file_storage/call_LyhItPO07QGB7uY64QxaAPlq.json', 'var_call_DLpRLGSbwxHVQUCw1D22C1tx': {'error': 'No joined records with publication year and ratings found'}, 'var_call_puJwwaQmoN0raYq4d5TYz0RV': 'file_storage/call_puJwwaQmoN0raYq4d5TYz0RV.json'}

exec(code, env_args)
