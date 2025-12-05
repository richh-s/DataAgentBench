code = """import json, re, pandas as pd

# Load review averages
path_reviews = var_call_TIOVREL6hyzBGuw7leXemiE6
with open(path_reviews, 'r') as f:
    reviews = json.load(f)

# Load book details
path_books = var_call_elemP1lhUsJEk9QH54wzblUe
with open(path_books, 'r') as f:
    books = json.load(f)

# Build mapping from index number to decade based on book_id pattern 'bookid_<n>'
book_decade = {}
for b in books:
    bid = b['book_id']
    m = re.match(r'bookid_(\d+)$', bid)
    if not m:
        continue
    idx = int(m.group(1))
    details = b.get('details') or ''
    mdate = re.search(r'on ([A-Za-z]+ \d{1,2}, (\d{4}))', details)
    if not mdate:
        mdate = re.search(r'on ([A-Za-z]+,? (\d{4}))', details)
    if not mdate:
        mdate = re.search(r'released on (January 1, (\d{4}))', details)
    year = None
    if mdate:
        year = int(mdate.group(2))
    else:
        myear = re.search(r' on (January 1, )?(\d{4})', details)
        if myear:
            year = int(myear.group(2))
    if year is None:
        continue
    decade = (year // 10) * 10
    book_decade[idx] = decade

# Now map purchase_id pattern 'purchaseid_<n>' to same index n and decade
records = []
for r in reviews:
    pid = r['purchase_id']
    m = re.match(r'purchaseid_(\d+)$', pid)
    if not m:
        continue
    idx = int(m.group(1))
    decade = book_decade.get(idx)
    if decade is None:
        continue
    try:
        avg_rating = float(r['avg_rating'])
    except:
        continue
    records.append({'decade': decade, 'avg_rating': avg_rating, 'book_idx': idx})

if not records:
    result = json.dumps({'error': 'No records with mapped decades'})
else:
    df = pd.DataFrame(records)
    # Count distinct books per decade
    grp = df.groupby('decade').agg(avg_decade_rating=('avg_rating','mean'), book_count=('book_idx','nunique')).reset_index()
    grp = grp[grp['book_count'] >= 10]
    if grp.empty:
        result = json.dumps({'error': 'No decade with at least 10 distinct books'})
    else:
        best = grp.sort_values('avg_decade_rating', ascending=False).iloc[0]
        decade_str = f"{int(best['decade'])}s"
        result = json.dumps({'decade': decade_str, 'average_rating': round(float(best['avg_decade_rating']), 3), 'distinct_books': int(best['book_count'])})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_DV2jaXdeb1blBm3WRqTK4eg4': ['review'], 'var_call_TIOVREL6hyzBGuw7leXemiE6': 'file_storage/call_TIOVREL6hyzBGuw7leXemiE6.json', 'var_call_a54U8vXkkcEH8ZjlrHZttQtL': ['books_info'], 'var_call_elemP1lhUsJEk9QH54wzblUe': 'file_storage/call_elemP1lhUsJEk9QH54wzblUe.json'}

exec(code, env_args)
