code = """import json, re, pandas as pd

# Load full books info from file
with open(var_call_Ghtwot2wGOEjEplye6Q5GJrs, 'r') as f:
    books = json.load(f)

reviews = var_call_wMZoLXf3ePBdnoqImulheE3o

# Ensure reviews is a list of dicts
if isinstance(reviews, str):
    reviews = json.loads(reviews)

# Extract publication year from details using regex
book_years = {}
for row in books:
    details = row.get('details') or ''
    match_year = None
    for m in re.finditer(r'(18|19|20)(\d{2})', details):
        year = int(m.group(1)+m.group(2))
        if 1800 <= year <= 2029:
            match_year = year
            break
    if match_year is not None:
        book_years[row['book_id']] = match_year

books_df = pd.DataFrame([
    {'book_id': bid, 'year': yr} for bid, yr in book_years.items()
])

rev_df = pd.DataFrame(reviews)
rev_df['rating'] = rev_df['rating'].astype(float)

rev_df['num'] = rev_df['purchase_id'].str.extract(r'(\d+)$').astype(float)
books_df['num'] = books_df['book_id'].str.extract(r'(\d+)$').astype(float)

merged = pd.merge(rev_df, books_df, on='num', how='inner')

merged['decade'] = (merged['year']//10)*10

group = merged.groupby('decade').agg(distinct_books=('book_id','nunique'), avg_rating=('rating','mean'))
filtered = group[group['distinct_books']>=10]

if filtered.empty:
    result = None
else:
    filtered_sorted = filtered.sort_values(['avg_rating','decade'], ascending=[False, True])
    best_decade = int(filtered_sorted.index[0])
    result = f"{best_decade}s"

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Ghtwot2wGOEjEplye6Q5GJrs': 'file_storage/call_Ghtwot2wGOEjEplye6Q5GJrs.json', 'var_call_LEF99fEglSETIXrE8i6CRA1z': ['books_info'], 'var_call_wpiacZs8byiTsx3e8wpK6Zm8': ['review'], 'var_call_wMZoLXf3ePBdnoqImulheE3o': 'file_storage/call_wMZoLXf3ePBdnoqImulheE3o.json'}

exec(code, env_args)
