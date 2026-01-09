code = """import json, re, pandas as pd

def load_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

books = load_result(var_call_Dc3zTbmWR4YMgpsQBImfwMZY)
reviews = load_result(var_call_XEN1CuQS36JlEXsFOQHQ3LXs)

# Parse publication year from details text
pat = re.compile(r'\b(?:released on|on)\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b')
pat2 = re.compile(r'\b(?:Published by|published by)\b.*?\b(?:on\s+)?(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b')
pat3 = re.compile(r'\b(?:publication date|Publication date)\s*[:\-]?\s*(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b')

def extract_year(details):
    if not details:
        return None
    s = str(details)
    for p in (pat3, pat2, pat):
        m = p.search(s)
        if m:
            y = int(m.group(1))
            if 1000 <= y <= 2026:
                return y
    # fallback: first 4-digit year
    m = re.search(r'\b(1[5-9]\d{2}|20\d{2})\b', s)
    if m:
        y = int(m.group(1))
        if 1000 <= y <= 2026:
            return y
    return None

book_year = {}
for r in books:
    bid = r.get('book_id')
    y = extract_year(r.get('details'))
    if bid and y:
        book_year[bid] = y

# Map purchaseid_x -> bookid_x
purchase_to_book = {}
for pr in set([rv.get('purchase_id') for rv in reviews]):
    if not pr:
        continue
    m = re.match(r'purchaseid_(\d+)$', str(pr))
    if m:
        purchase_to_book[pr] = f"bookid_{m.group(1)}"

# Aggregate ratings per decade with at least 10 distinct rated books
# Consider a book 'rated' if it has >=1 review with rating
from collections import defaultdict

decade_book_ratings = defaultdict(list)  # (decade, book)-> list ratings
for rv in reviews:
    pid = rv.get('purchase_id')
    if pid not in purchase_to_book:
        continue
    bid = purchase_to_book[pid]
    y = book_year.get(bid)
    if not y:
        continue
    try:
        rating = float(rv.get('rating'))
    except:
        continue
    decade = (y // 10) * 10
    decade_book_ratings[(decade, bid)].append(rating)

# Compute per-decade average across all reviews, but only decades with >=10 distinct books rated
per_decade = defaultdict(lambda: {'ratings': [], 'books': set()})
for (decade, bid), rs in decade_book_ratings.items():
    per_decade[decade]['books'].add(bid)
    per_decade[decade]['ratings'].extend(rs)

rows = []
for decade, d in per_decade.items():
    n_books = len(d['books'])
    if n_books >= 10 and len(d['ratings'])>0:
        avg = sum(d['ratings'])/len(d['ratings'])
        rows.append((decade, n_books, avg, len(d['ratings'])))

rows.sort(key=lambda x: (x[2], x[1], x[3]), reverse=True)
result = None
if rows:
    best = rows[0][0]
    result = f"{best}s"

print('__RESULT__:')
print(json.dumps({'decade': result, 'candidates': rows[:10]}))"""

env_args = {'var_call_Dc3zTbmWR4YMgpsQBImfwMZY': 'file_storage/call_Dc3zTbmWR4YMgpsQBImfwMZY.json', 'var_call_xrGzuXDbwAy2w5hHpbRjzYuY': ['review'], 'var_call_XEN1CuQS36JlEXsFOQHQ3LXs': 'file_storage/call_XEN1CuQS36JlEXsFOQHQ3LXs.json'}

exec(code, env_args)
