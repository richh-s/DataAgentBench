code = """import json, pandas as pd, ast

# Load full books_info result
with open(var_call_a8oq4HlQDXmgbiAUkFM9iFdm, 'r') as f:
    books = json.load(f)

books_df = pd.DataFrame(books)

# Identify Children's Books based on 'categories' containing "Children's Books"
def is_children(cat_str):
    try:
        cats = ast.literal_eval(cat_str) if isinstance(cat_str, str) and cat_str else []
    except Exception:
        return False
    return any("Children's Books" in c for c in cats)

books_df['is_children'] = books_df['categories'].apply(is_children)
children_books = books_df[books_df['is_children']][['book_id','title']]

# Load reviews from 2020 onwards
with open(var_call_cPThepGNUzVAweYFdGAFigJw, 'r') as f:
    reviews = json.load(f)

reviews_df = pd.DataFrame(reviews)

# Ensure numeric rating
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'])

# Compute average rating per purchase_id
avg_ratings = reviews_df.groupby('purchase_id', as_index=False)['rating'].mean()

# Join with children's books on book_id == purchase_id (exact match as ids appear consistent)
merged = pd.merge(children_books, avg_ratings, left_on='book_id', right_on='purchase_id', how='inner')

# Filter for avg rating >= 4.5
high_rated = merged[merged['rating'] >= 4.5]

# Prepare result list of titles (unique)
result_titles = sorted(high_rated['title'].unique().tolist())

import json as _json
out = _json.dumps(result_titles)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_a8oq4HlQDXmgbiAUkFM9iFdm': 'file_storage/call_a8oq4HlQDXmgbiAUkFM9iFdm.json', 'var_call_p06GOrVCLJX0MIyRLxjTnkwu': ['review'], 'var_call_cPThepGNUzVAweYFdGAFigJw': 'file_storage/call_cPThepGNUzVAweYFdGAFigJw.json'}

exec(code, env_args)
