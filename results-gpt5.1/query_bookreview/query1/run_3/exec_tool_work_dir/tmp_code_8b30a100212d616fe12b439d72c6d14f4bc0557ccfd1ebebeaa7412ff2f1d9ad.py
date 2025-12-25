code = """import json, re, pandas as pd

# Load full books info from file
with open(var_call_Ghtwot2wGOEjEplye6Q5GJrs, 'r') as f:
    books = json.load(f)

reviews = var_call_wMZoLXf3ePBdnoqImulheE3o

# Extract publication year from details using regex for 4-digit year 1800-2029
year_pattern = re.compile(r'(18|19|20)\d{2}')

book_years = {}
for row in books:
    details = row.get('details') or ''
    years = year_pattern.findall(details)
    # findall with groups returns tuples for prefix, so instead search differently

# Better: use finditer
book_years = {}
for row in books:
    details = row.get('details') or ''
    match = None
    for m in re.finditer(r'(18|19|20)(\d{2})', details):
        year = int(m.group(1)+m.group(2))
        if 1800 <= year <= 2029:
            match = year
            break
    if match is not None:
        book_years[row['book_id']] = match

# Build DataFrames
books_df = pd.DataFrame(list(book_years.items()), columns=['book_id','year'])
rev_df = pd.DataFrame(reviews)
rev_df['rating'] = rev_df['rating'].astype(float)

# Fuzzy join: here purchase_id like 'purchaseid_123' vs bookid_123
# Extract numeric suffix
rev_df['num'] = rev_df['purchase_id'].str.extract(r'(\d+)$').astype(float)
books_df['num'] = books_df['book_id'].str.extract(r'(\d+)$').astype(float)

merged = pd.merge(rev_df, books_df, on='num', how='inner')

# Compute decade
merged['decade'] = (merged['year']//10)*10

# Need at least 10 distinct books (book_id) with ratings in that decade
group = merged.groupby('decade').agg(distinct_books=('book_id','nunique'), avg_rating=('rating','mean'))
filtered = group[group['distinct_books']>=10]

if filtered.empty:
    result = None
else:
    # Get decade with highest avg_rating; in tie, earliest decade
    best = filtered.sort_values(['avg_rating','decade'], ascending=[False, True]).iloc[0]
    decade = int(filtered.sort_values(['avg_rating','decade'], ascending=[False, True]).index[0])
    result = f"{decade}s"

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Ghtwot2wGOEjEplye6Q5GJrs': 'file_storage/call_Ghtwot2wGOEjEplye6Q5GJrs.json', 'var_call_LEF99fEglSETIXrE8i6CRA1z': ['books_info'], 'var_call_wpiacZs8byiTsx3e8wpK6Zm8': ['review'], 'var_call_wMZoLXf3ePBdnoqImulheE3o': 'file_storage/call_wMZoLXf3ePBdnoqImulheE3o.json'}

exec(code, env_args)
