code = """import json, re, pandas as pd
from collections import defaultdict

# Load full books details
with open(var_call_UsTMQ8QzJI4FwXD5wch76qVy, 'r') as f:
    books = json.load(f)

# Load full reviews
with open(var_call_wIgaIWOKenXhlVLHeghtj6Zp, 'r') as f:
    reviews = json.load(f)

# Extract publication year from details
year_pattern = re.compile(r"(19|20)\d{2}")
book_year = {}
for row in books:
    details = row.get('details') or ''
    years = year_pattern.findall(details)
    # findall with groups returns tuples; instead use finditer

book_year = {}
for row in books:
    details = row.get('details') or ''
    match = re.search(r"(19|20)\d{2}", details)
    if match:
        year = int(match.group(0))
        book_year[row['book_id']] = year

# Map purchase_id to ratings list
ratings_by_book = defaultdict(list)
for r in reviews:
    bid = r['purchase_id']
    try:
        rating = float(r['rating'])
    except:
        continue
    ratings_by_book[bid].append(rating)

# Compute average rating per book
avg_rating_book = {bid: sum(vals)/len(vals) for bid, vals in ratings_by_book.items() if bid in book_year}

# Aggregate by decade, considering distinct books
decade_ratings = defaultdict(list)
for bid, avg_r in avg_rating_book.items():
    year = book_year[bid]
    decade = (year // 10) * 10
    decade_ratings[decade].append(avg_r)

# Filter decades with at least 10 distinct books
decade_avg = {}
for decade, ratings in decade_ratings.items():
    if len(ratings) >= 10:
        decade_avg[decade] = sum(ratings)/len(ratings)

if not decade_avg:
    result = None
else:
    best_decade = max(decade_avg.items(), key=lambda x: x[1])[0]
    result = f"{best_decade}s"

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_UsTMQ8QzJI4FwXD5wch76qVy': 'file_storage/call_UsTMQ8QzJI4FwXD5wch76qVy.json', 'var_call_cFseZdhlDdqlyA8ybuTLyMNg': ['books_info'], 'var_call_5T8qFd2oN7a4FNeRO3vcqIAv': ['review'], 'var_call_wIgaIWOKenXhlVLHeghtj6Zp': 'file_storage/call_wIgaIWOKenXhlVLHeghtj6Zp.json'}

exec(code, env_args)
