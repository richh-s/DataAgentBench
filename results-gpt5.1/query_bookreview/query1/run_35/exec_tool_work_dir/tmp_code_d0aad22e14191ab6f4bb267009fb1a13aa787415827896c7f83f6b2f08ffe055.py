code = """import json, re, pandas as pd
from collections import defaultdict

# load full data
with open(var_call_iZcRYxxcaNehiKpENqLNDFbS, 'r') as f:
    reviews = json.load(f)
with open(var_call_d5FxMkQv5OJflqGfTYKAdlGI, 'r') as f:
    books = json.load(f)

# build mapping from purchase_id to book_id via numeric suffix
bookid_by_num = {}
for b in books:
    m = re.search(r"(\d+)$", b['book_id'])
    if m:
        bookid_by_num[m.group(1)] = b

records = []
for r in reviews:
    m = re.search(r"(\d+)$", r['purchase_id'])
    if not m:
        continue
    num = m.group(1)
    b = bookid_by_num.get(num)
    if not b:
        continue
    details = b.get('details','') or ''
    # find year patterns 19xx or 20xx
    years = re.findall(r"(19\d{2}|20\d{2})", details)
    year = None
    if years:
        year = int(years[0])
    if not year:
        continue
    decade = (year // 10) * 10
    records.append({'decade': decade, 'book_id': b['book_id'], 'rating': float(r['rating'])})

if not records:
    result = None
else:
    df = pd.DataFrame(records)
    # keep distinct books with at least one rating per decade and average rating per book first
    book_avg = df.groupby(['decade','book_id'])['rating'].mean().reset_index()
    # filter decades with at least 10 distinct books
    counts = book_avg.groupby('decade')['book_id'].nunique().reset_index(name='n_books')
    valid_decades = counts[counts['n_books']>=10]['decade']
    if valid_decades.empty:
        result = None
    else:
        valid = book_avg[book_avg['decade'].isin(valid_decades)]
        decade_avg = valid.groupby('decade')['rating'].mean().reset_index()
        top = decade_avg.sort_values(['rating','decade'], ascending=[False, True]).iloc[0]
        result = f"{int(top['decade'])}s"

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_r1vTa1o6oyPRHzujHpq9sGo6': ['books_info'], 'var_call_J792xpCf9Q6ozlvWxxJh2628': ['review'], 'var_call_iZcRYxxcaNehiKpENqLNDFbS': 'file_storage/call_iZcRYxxcaNehiKpENqLNDFbS.json', 'var_call_d5FxMkQv5OJflqGfTYKAdlGI': 'file_storage/call_d5FxMkQv5OJflqGfTYKAdlGI.json'}

exec(code, env_args)
