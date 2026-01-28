code = """import json
import re
from statistics import mean

# Load data from the stored JSON files
books_path = var_call_LxlXbDydMUn7vMI1fN9eFQip
reviews_path = var_call_0JydO0Ga4JlEFBMl8dsOzpqH

with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)

with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Helper to extract numeric id suffix
def extract_num_id(s):
    if not s:
        return None
    m = re.search(r"(\d+)$", s)
    return int(m.group(1)) if m else None

# Helper to extract year from details
def extract_year(details):
    if not details:
        return None
    # Look for 4-digit year between 1000 and 2023
    years = re.findall(r"(\d{4})", details)
    for y in years:
        yi = int(y)
        if 1000 <= yi <= 2023:
            return yi
    return None

# Build mapping book_num -> year
book_year = {}
for b in books:
    bid = b.get('book_id')
    num = extract_num_id(bid)
    if num is None:
        continue
    year = None
    # try details first
    year = extract_year(b.get('details','') or '')
    # fallback: try description and categories
    if year is None:
        year = extract_year(b.get('description','') or '')
    if year is None:
        year = extract_year(b.get('categories','') or '')
    if year is not None:
        book_year[num] = year

# Aggregate ratings per book number from reviews
ratings_by_book = {}
for r in reviews:
    pid = r.get('purchase_id')
    rating = r.get('rating')
    if pid is None or rating is None:
        continue
    num = extract_num_id(pid)
    if num is None:
        continue
    try:
        rt = float(rating)
    except:
        continue
    ratings_by_book.setdefault(num, []).append(rt)

# For each book that has both a year and ratings, compute book average
book_avg = {}
for num, rlist in ratings_by_book.items():
    if num in book_year and len(rlist) > 0:
        book_avg[num] = mean(rlist)

# Group by decade and compute per-decade average of book means
decade_groups = {}
for num, avg in book_avg.items():
    year = book_year[num]
    decade_start = (year // 10) * 10
    decade_label = f"{decade_start}s"
    decade_groups.setdefault(decade_label, []).append((num, avg))

# Filter decades with at least 10 distinct books and compute decade average
decade_stats = {}
for dec, items in decade_groups.items():
    distinct_books = {num for num, _ in items}
    if len(distinct_books) >= 10:
        # average of book averages
        vals = [avg for _, avg in items]
        decade_stats[dec] = {
            'book_count': len(distinct_books),
            'avg_rating': mean(vals)
        }

# Determine decade with highest average rating
if not decade_stats:
    result = {"decade": None, "avg_rating": None, "book_count": 0}
else:
    best_decade = max(decade_stats.items(), key=lambda x: (x[1]['avg_rating'], x[0]))
    dec_label = best_decade[0]
    dec_info = best_decade[1]
    result = {"decade": dec_label, "avg_rating": round(dec_info['avg_rating'], 4), "book_count": dec_info['book_count']}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_YmXOVvuKHqUuKghuFyYZqToK': ['review'], 'var_call_uZru3CPmP8emsDhCO1MHIWBW': ['books_info'], 'var_call_LxlXbDydMUn7vMI1fN9eFQip': 'file_storage/call_LxlXbDydMUn7vMI1fN9eFQip.json', 'var_call_0JydO0Ga4JlEFBMl8dsOzpqH': 'file_storage/call_0JydO0Ga4JlEFBMl8dsOzpqH.json'}

exec(code, env_args)
