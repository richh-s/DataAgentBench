code = """import json, re, pandas as pd

# Load full books info
with open(var_call_o2vVUSxGbqcuJGQfA143BB6Z, 'r') as f:
    books = json.load(f)

# Extract year from details using regex and compute decade
years = []
for row in books:
    details = row.get('details') or ''
    # look for 4-digit years between 1500 and 2100
    found = re.findall(r'(1[5-9]\d{2}|20\d{2}|2100)', details)
    year = None
    if found:
        # heuristic: take the first year mentioned
        year = int(found[0])
    years.append({'book_id': row['book_id'], 'year': year})

books_df = pd.DataFrame(years)
books_df = books_df.dropna(subset=['year'])
books_df['year'] = books_df['year'].astype(int)
books_df['decade'] = (books_df['year'] // 10) * 10

# Load reviews
with open(var_call_Lmv5aAvECFqxjHwqJDyVOU4q, 'r') as f:
    reviews = json.load(f)
rev_df = pd.DataFrame(reviews)
rev_df['rating'] = rev_df['rating'].astype(float)

# Fuzzy join: purchase_id in reviews == book_id in books
merged = pd.merge(rev_df, books_df, left_on='purchase_id', right_on='book_id', how='inner')

# Compute distinct books per decade that have been rated
book_counts = merged.groupby('decade')['book_id'].nunique().reset_index(name='n_books')
eligible_decades = book_counts[book_counts['n_books'] >= 10]['decade']

if eligible_decades.empty:
    result = None
else:
    eligible_merged = merged[merged['decade'].isin(eligible_decades)]
    decade_avg = eligible_merged.groupby('decade')['rating'].mean().reset_index()
    top_row = decade_avg.sort_values(['rating','decade'], ascending=[False, True]).iloc[0]
    decade_label = f"{int(top_row['decade'])}s"
    result = decade_label

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_o2vVUSxGbqcuJGQfA143BB6Z': 'file_storage/call_o2vVUSxGbqcuJGQfA143BB6Z.json', 'var_call_LexYewvl4y1c5XsW33MDOwV9': ['books_info'], 'var_call_ucZ6Wvcb002jSLn2rrN87Wdw': ['review'], 'var_call_Lmv5aAvECFqxjHwqJDyVOU4q': 'file_storage/call_Lmv5aAvECFqxjHwqJDyVOU4q.json'}

exec(code, env_args)
