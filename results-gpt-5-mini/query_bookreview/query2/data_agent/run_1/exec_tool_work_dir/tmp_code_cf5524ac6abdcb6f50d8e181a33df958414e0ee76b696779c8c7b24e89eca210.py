code = """import json
import pandas as pd
import re

# Load data from previous tool calls stored in variables
# var_call_tragOMZg8AJTGhTXctHV0zYe and var_call_athQhDCQJCrQdVJJmLYzUisw

def load_var(v):
    if isinstance(v, str):
        # it's a file path to JSON
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

reviews = load_var(var_call_tragOMZg8AJTGhTXctHV0zYe)
books = load_var(var_call_athQhDCQJCrQdVJJmLYzUisw)

# Create DataFrames
df_r = pd.DataFrame(reviews)
df_b = pd.DataFrame(books)

# Extract numeric ids from purchase_id and book_id
df_r['id_num'] = df_r['purchase_id'].astype(str).str.extract(r'(\d+)')
df_b['id_num'] = df_b['book_id'].astype(str).str.extract(r'(\d+)')

# Merge on id_num
merged = pd.merge(df_r, df_b, on='id_num', how='inner', suffixes=('_rev', '_book'))

# Prepare output records
out = []
for _, row in merged.iterrows():
    try:
        rating_number = int(row['rating_number'])
    except Exception:
        try:
            rating_number = int(float(row['rating_number']))
        except Exception:
            rating_number = None
    try:
        price = float(row['price'])
    except Exception:
        price = None
    try:
        avg_rating = float(row['avg_rating'])
    except Exception:
        try:
            avg_rating = float(str(row['avg_rating']).strip())
        except Exception:
            avg_rating = None
    try:
        review_count = int(row['review_count'])
    except Exception:
        try:
            review_count = int(float(row['review_count']))
        except Exception:
            review_count = None

    rec = {
        'book_id': row.get('book_id'),
        'title': row.get('title'),
        'author': row.get('author'),
        'categories': row.get('categories'),
        'rating_number': rating_number,
        'price': price,
        'purchase_id': row.get('purchase_id'),
        'avg_rating': avg_rating,
        'review_count': review_count,
        'sample_title': row.get('sample_title')
    }
    out.append(rec)

# Remove duplicates by book_id
seen = set()
unique_out = []
for r in out:
    bid = r.get('book_id')
    if bid not in seen:
        unique_out.append(r)
        seen.add(bid)

print("__RESULT__:")
print(json.dumps(unique_out))"""

env_args = {'var_call_KQhoAonEWOKCkMYj2OyCUbt5': ['review'], 'var_call_tragOMZg8AJTGhTXctHV0zYe': 'file_storage/call_tragOMZg8AJTGhTXctHV0zYe.json', 'var_call_59E4WtqJZ7JdzL5qRsFMZLO2': ['books_info'], 'var_call_athQhDCQJCrQdVJJmLYzUisw': 'file_storage/call_athQhDCQJCrQdVJJmLYzUisw.json'}

exec(code, env_args)
