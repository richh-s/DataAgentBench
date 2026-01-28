code = """import json
import pandas as pd
import ast

# Load data from storage file paths
with open(var_call_vUoeFP56X39VQjBOwwWtInFG, 'r') as f:
    reviews = json.load(f)
with open(var_call_a21RYii2vyGavATzBNHQdIHa, 'r') as f:
    books = json.load(f)

# Create dataframes
dfr = pd.DataFrame(reviews)
dfb = pd.DataFrame(books)

# Normalize and filter reviews from 2020 onwards
dfr['rating'] = pd.to_numeric(dfr['rating'], errors='coerce')
dfr['review_time'] = pd.to_datetime(dfr['review_time'], errors='coerce')
dfr = dfr[dfr['review_time'] >= pd.to_datetime('2020-01-01')]

# Group by purchase_id to compute averages
group = dfr.groupby('purchase_id').agg(average_rating=('rating', 'mean'), review_count=('rating', 'count')).reset_index()

# Convert purchase_id (purchaseid_123) to book_id (bookid_123)
group['book_id'] = group['purchase_id'].str.replace('purchaseid_', 'bookid_', regex=False)

# Parse categories in books table
def parse_cats(s):
    if s is None:
        return []
    try:
        parsed = ast.literal_eval(s)
        if isinstance(parsed, list):
            return parsed
        return []
    except Exception:
        return []

if 'categories' not in dfb.columns:
    dfb['categories'] = '[]'

dfb['categories_parsed'] = dfb['categories'].apply(parse_cats)

# Merge grouped review stats with books
merged = pd.merge(group, dfb, on='book_id', how='left')

# Filter to Children's Books
merged['is_children'] = merged['categories_parsed'].apply(lambda x: "Children's Books" in x if isinstance(x, list) else False)
res = merged[(merged['is_children']) & (merged['average_rating'] >= 4.5)].copy()

# Prepare output
output = []
for _, row in res.sort_values(['average_rating', 'review_count'], ascending=[False, False]).iterrows():
    output.append({
        'book_id': row.get('book_id'),
        'title': row.get('title'),
        'average_rating': round(float(row.get('average_rating')), 3) if pd.notna(row.get('average_rating')) else None,
        'review_count': int(row.get('review_count')) if pd.notna(row.get('review_count')) else 0,
        'categories': row.get('categories_parsed')
    })

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_cwPiVzdAOIaFTIqgBWsz9br0': ['review'], 'var_call_sx244X30ltxeinje7ZOZmqjP': ['books_info'], 'var_call_vUoeFP56X39VQjBOwwWtInFG': 'file_storage/call_vUoeFP56X39VQjBOwwWtInFG.json', 'var_call_a21RYii2vyGavATzBNHQdIHa': 'file_storage/call_a21RYii2vyGavATzBNHQdIHa.json'}

exec(code, env_args)
