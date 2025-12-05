code = """import pandas as pd, json, re
from collections import defaultdict

# Load books_info details
with open(var_call_RvDWnmxHdDxllX3Ucqjcadfm, 'r') as f:
    books = json.load(f)

# Load reviews
with open(var_call_zWdnSESILH7eGmyEj0kFHIRf, 'r') as f:
    reviews = json.load(f)

# Extract publication year from details using regex
year_pattern = re.compile(r"(19|20)\d{2}")
book_year = {}
for row in books:
    details = row.get('details') or ''
    years = year_pattern.findall(details)
    # years is list of tuples because of groups; rebuild full years from matches
    full_years = re.findall(r"(19\d{2}|20\d{2})", details)
    year = None
    if full_years:
        # heuristic: earliest year mentioned as publication year
        year = min(int(y) for y in full_years)
    book_year[row['book_id']] = year

# Aggregate ratings per book
book_ratings = defaultdict(list)
for r in reviews:
    bid = r['purchase_id']
    rating = float(r['rating']) if r['rating'] is not None else None
    if rating is None:
        continue
    if bid in book_year and book_year[bid] is not None:
        book_ratings[bid].append(rating)

# Compute average rating per book and its decade
decade_ratings = defaultdict(list)
for bid, rs in book_ratings.items():
    if not rs:
        continue
    avg_book = sum(rs)/len(rs)
    year = book_year[bid]
    decade_start = (year // 10) * 10
    decade_label = f"{decade_start}s"
    decade_ratings[decade_label].append(avg_book)

# Filter decades with at least 10 distinct books
decade_avg = {}
for dec, ratings in decade_ratings.items():
    if len(ratings) >= 10:
        decade_avg[dec] = sum(ratings)/len(ratings)

if not decade_avg:
    result = None
else:
    best_decade = max(decade_avg.items(), key=lambda x: x[1])[0]
    result = best_decade

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_RvDWnmxHdDxllX3Ucqjcadfm': 'file_storage/call_RvDWnmxHdDxllX3Ucqjcadfm.json', 'var_call_G1eAvZNNz5fopvspBZ0sVTA0': ['books_info'], 'var_call_sNjs5srX810x5fJv0kjjvMFG': ['review'], 'var_call_zWdnSESILH7eGmyEj0kFHIRf': 'file_storage/call_zWdnSESILH7eGmyEj0kFHIRf.json'}

exec(code, env_args)
