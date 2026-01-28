code = """import json, re
import pandas as pd

# Load data from previous query results
with open(var_call_UNqE2IhNtPy3UfHydlayzsUs, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(var_call_FucGOrfXuqotZPjS25rulCNE, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

bdf = pd.DataFrame(books)
rdf = pd.DataFrame(reviews)

# Extract numeric id from book_id / purchase_id
def extract_num(x):
    if not isinstance(x, str):
        return None
    m = re.search(r"(\d+)", x)
    return int(m.group(1)) if m else None

bdf['num_id'] = bdf['book_id'].apply(extract_num)
rdf['num_id'] = rdf['purchase_id'].apply(extract_num)

# Extract publication year from details by finding 4-digit years between 1500 and 2023
def extract_year(s):
    if not isinstance(s, str):
        return None
    years = re.findall(r"\b(1[5-9]\d{2}|20\d{2})\b", s)
    # filter and convert
    yrs = []
    for y in years:
        try:
            yi = int(y)
            if 1500 <= yi <= 2023:
                yrs.append(yi)
        except:
            continue
    if len(yrs) == 0:
        return None
    # choose the first plausible year
    return yrs[0]

bdf['year'] = bdf['details'].apply(extract_year)

# Merge reviews with books on numeric id
merged = pd.merge(rdf, bdf, on='num_id', how='left', suffixes=('_rev','_book'))

# Keep entries where we have a book and a year
merged = merged[merged['book_id'].notna()]
merged = merged[merged['year'].notna()]

# Convert rating to numeric
merged['rating'] = pd.to_numeric(merged['rating'], errors='coerce')
merged = merged[merged['rating'].notna()]

# Compute per-book average rating
book_avg = merged.groupby('book_id').agg({'rating':'mean','year':'first'}).reset_index()
book_avg.rename(columns={'rating':'book_avg_rating'}, inplace=True)

# Compute decade
book_avg['decade_start'] = (book_avg['year'].astype(int) // 10) * 10
book_avg['decade'] = book_avg['decade_start'].astype(str) + 's'

# For each decade, compute number of distinct books and average of book_avg_rating
decade_stats = book_avg.groupby('decade').agg(
    book_count = ('book_id','nunique'),
    avg_rating = ('book_avg_rating','mean')
).reset_index()

# Filter decades with at least 10 distinct books
decade_stats_filtered = decade_stats[decade_stats['book_count'] >= 10]

result = None
if len(decade_stats_filtered) == 0:
    result = {'error':'No decade has at least 10 distinct rated books.'}
else:
    # choose decade with highest average rating
    best = decade_stats_filtered.sort_values(['avg_rating','book_count'], ascending=[False,False]).iloc[0]
    result = {
        'decade': best['decade'],
        'average_rating': round(float(best['avg_rating']), 4),
        'book_count': int(best['book_count'])
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_UNqE2IhNtPy3UfHydlayzsUs': 'file_storage/call_UNqE2IhNtPy3UfHydlayzsUs.json', 'var_call_PWYdjdvrG9HmjhbLe8j6vHRy': ['review'], 'var_call_FucGOrfXuqotZPjS25rulCNE': 'file_storage/call_FucGOrfXuqotZPjS25rulCNE.json'}

exec(code, env_args)
