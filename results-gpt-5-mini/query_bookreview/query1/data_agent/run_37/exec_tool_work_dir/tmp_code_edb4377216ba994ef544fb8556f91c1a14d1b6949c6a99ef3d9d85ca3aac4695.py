code = """import json, re, math

# Load data from storage files (paths are stored in variables provided by previous tool calls)
books_path = var_call_VFwaiakiaOs5o8a86Y0tuuLZ
reviews_path = var_call_yqr9lFD3rfR1pzWwKMIjVdUL

with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Helper to extract numeric id suffix
def extract_num_id(s):
    if not s or not isinstance(s, str):
        return None
    m = re.search(r"(\d+)$", s)
    return m.group(1) if m else None

# Extract publication year from details field
def extract_year(details):
    if not details or not isinstance(details, str):
        return None
    # find all 4-digit numbers
    years = re.findall(r"(\d{4})", details)
    if not years:
        return None
    # choose the first plausible year between 1500 and 2025 (inclusive)
    for y in years:
        yi = int(y)
        if 1500 <= yi <= 2025:
            return yi
    # otherwise return the first 4-digit number
    return int(years[0])

# Build book map by numeric id
book_info_by_num = {}
for b in books:
    book_id = b.get('book_id')
    num = extract_num_id(book_id)
    if not num:
        continue
    year = extract_year(b.get('details','') or '')
    if year is None:
        # try to also look in title for year (rare)
        year = extract_year(b.get('title','') or '')
    if year is None:
        continue
    decade = (year // 10) * 10
    decade_label = f"{decade}s"
    book_info_by_num[num] = {
        'book_id': book_id,
        'num': num,
        'year': year,
        'decade': decade_label
    }

# Process reviews: attach to books by numeric id
joined = []
for r in reviews:
    pid = r.get('purchase_id')
    num = extract_num_id(pid)
    if not num:
        continue
    if num not in book_info_by_num:
        continue
    # parse rating
    rating_raw = r.get('rating')
    try:
        rating = float(rating_raw)
    except:
        try:
            rating = float(str(rating_raw).strip())
        except:
            continue
    rec = {
        'purchase_id': pid,
        'book_num': num,
        'rating': rating,
        'decade': book_info_by_num[num]['decade']
    }
    joined.append(rec)

# If no joined records, return empty
if not joined:
    result = {'best_decade': None, 'avg_rating': None, 'distinct_books': 0}
else:
    # Aggregate by decade
    from collections import defaultdict
    decade_ratings = defaultdict(list)
    decade_books = defaultdict(set)
    for j in joined:
        decade = j['decade']
        decade_ratings[decade].append(j['rating'])
        decade_books[decade].add(j['book_num'])

    # compute stats
    stats = []
    for dec in decade_ratings:
        ratings = decade_ratings[dec]
        avg = sum(ratings)/len(ratings) if ratings else None
        distinct_books = len(decade_books[dec])
        stats.append({'decade': dec, 'avg_rating': avg, 'distinct_books': distinct_books, 'num_ratings': len(ratings)})

    # filter decades with at least 10 distinct books
    valid = [s for s in stats if s['distinct_books'] >= 10]
    if not valid:
        result = {'best_decade': None, 'avg_rating': None, 'distinct_books': 0}
    else:
        # find max avg_rating; in case of tie choose decade with more distinct books then lexicographically smallest
        valid.sort(key=lambda x: (x['avg_rating'], x['distinct_books'], x['decade']), reverse=True)
        best = valid[0]
        # round avg to 4 decimals
        best['avg_rating'] = round(best['avg_rating'], 4) if best['avg_rating'] is not None else None
        result = {'best_decade': best['decade'], 'avg_rating': best['avg_rating'], 'distinct_books': best['distinct_books']}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jXkwomUT3RqFnIQAGsavMsd6': ['review'], 'var_call_VFwaiakiaOs5o8a86Y0tuuLZ': 'file_storage/call_VFwaiakiaOs5o8a86Y0tuuLZ.json', 'var_call_yqr9lFD3rfR1pzWwKMIjVdUL': 'file_storage/call_yqr9lFD3rfR1pzWwKMIjVdUL.json'}

exec(code, env_args)
