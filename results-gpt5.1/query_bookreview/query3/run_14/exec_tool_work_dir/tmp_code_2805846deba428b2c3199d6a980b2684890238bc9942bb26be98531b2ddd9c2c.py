code = """import json, pandas as pd

# Load full books_info result
books_path = var_call_IBOh2MBMUZxfhRatQdswGGqo
with open(books_path, 'r') as f:
    books = json.load(f)

books_df = pd.DataFrame(books)

# Filter Children's Books
def is_childrens(cat_str):
    try:
        cats = json.loads(cat_str) if isinstance(cat_str, str) and cat_str else []
    except Exception:
        return False
    return any("Children's Books" in c for c in cats)

books_df_child = books_df[books_df['categories'].apply(is_childrens)][['book_id','title']]

# Load full review result
rev_path = var_call_yDkSpZ6v0l6Dtc61o6pP86dX
with open(rev_path, 'r') as f:
    rev = json.load(f)

rev_df = pd.DataFrame(rev)
rev_df['rating'] = rev_df['rating'].astype(float)

# Compute average rating per purchase_id from 2020 onwards (already filtered in SQL)
avg_ratings = rev_df.groupby('purchase_id', as_index=False)['rating'].mean()

# Join on id equality (purchase_id == book_id)
merged = pd.merge(books_df_child, avg_ratings, left_on='book_id', right_on='purchase_id')

# Filter avg rating >= 4.5
res = merged[merged['rating'] >= 4.5].sort_values('title')[['title','book_id','rating']]

out = res.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_IBOh2MBMUZxfhRatQdswGGqo': 'file_storage/call_IBOh2MBMUZxfhRatQdswGGqo.json', 'var_call_4yb51XerypIme1aa4ACPZE6u': ['review'], 'var_call_yDkSpZ6v0l6Dtc61o6pP86dX': 'file_storage/call_yDkSpZ6v0l6Dtc61o6pP86dX.json'}

exec(code, env_args)
