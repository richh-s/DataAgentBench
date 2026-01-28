code = """import json, re
from collections import defaultdict

# Load data from previous tool results (file paths are stored in these variables)
with open(var_call_VJs8oJcr0FYbyZdrmhBxxWLn, 'r') as f:
    reviews = json.load(f)
with open(var_call_twTvANXNNRZug8YgYwIZ7WIb, 'r') as f:
    books = json.load(f)

# Extract publication year from books 'details' (or description if needed)
book_year = {}
year_re = re.compile(r"\b(1[0-9]{3}|20[0-9]{2})\b")
for b in books:
    bid = b.get('book_id')
    det = b.get('details') or ''
    m = year_re.search(det)
    if not m:
        descr = b.get('description') or ''
        m = year_re.search(descr)
    if m:
        try:
            year = int(m.group(0))
            book_year[bid] = year
        except:
            continue

# Map reviews to books; convert purchase_id to book_id by replacing prefix
book_ratings = defaultdict(list)
for r in reviews:
    pid = r.get('purchase_id')
    if not pid:
        continue
    bid = pid.replace('purchaseid_', 'bookid_')
    if bid not in book_year:
        continue
    try:
        rating = float(r.get('rating'))
    except:
        continue
    book_ratings[bid].append(rating)

# Compute per-book average ratings
book_avg = {}
for bid, rats in book_ratings.items():
    if len(rats) == 0:
        continue
    book_avg[bid] = sum(rats) / len(rats)

# Group books by decade and compute decade averages (of per-book averages)
decade_map = defaultdict(list)
for bid, avg in book_avg.items():
    year = book_year.get(bid)
    if not year:
        continue
    decade_start = (year // 10) * 10
    decade_str = f"{decade_start}s"
    decade_map[decade_str].append(avg)

# Filter decades with at least 10 distinct books and compute average
decade_stats = []
for dec, avgs in decade_map.items():
    count = len(avgs)
    if count >= 10:
        avg_dec = sum(avgs) / count
        decade_stats.append({'decade': dec, 'average_rating': avg_dec, 'book_count': count})

# Determine best decade
if not decade_stats:
    result = {'decade': None, 'average_rating': None, 'book_count': 0}
else:
    best = max(decade_stats, key=lambda x: (x['average_rating'], x['book_count']))
    # round average_rating to 4 decimals for readability
    best['average_rating'] = round(best['average_rating'], 4)
    result = best

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_naxH9QhY6FOr8IophD5cuPLC': ['review'], 'var_call_lR6PM4jXo5xU99GhtK7Hiokx': ['books_info'], 'var_call_VJs8oJcr0FYbyZdrmhBxxWLn': 'file_storage/call_VJs8oJcr0FYbyZdrmhBxxWLn.json', 'var_call_twTvANXNNRZug8YgYwIZ7WIb': 'file_storage/call_twTvANXNNRZug8YgYwIZ7WIb.json'}

exec(code, env_args)
