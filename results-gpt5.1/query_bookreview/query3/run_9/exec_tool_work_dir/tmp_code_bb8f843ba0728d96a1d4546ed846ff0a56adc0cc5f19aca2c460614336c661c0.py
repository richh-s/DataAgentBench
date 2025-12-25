code = """import json, pandas as pd

# Load books_info from file
with open(var_call_S8KfkaFJkm3UbNGELQuBWZuN, 'r') as f:
    books = json.load(f)

books_df = pd.DataFrame(books)

# Filter to Children's Books via substring match in categories
child_books = books_df[books_df['categories'].str.contains("Children's Books", na=False)].copy()

# Load reviews from file
with open(var_call_wOjly9pP9p5bvzvMBBaM6sic, 'r') as f:
    reviews = json.load(f)

rev_df = pd.DataFrame(reviews)
rev_df['rating'] = rev_df['rating'].astype(float)

# Fuzzy join: assume purchase_id matches book_id exactly (as hinted)
merged = rev_df.merge(child_books[['book_id','title']], left_on='purchase_id', right_on='book_id', how='inner')

# Compute average rating per book from 2020 onwards
avg_ratings = merged.groupby(['book_id','title'])['rating'].mean().reset_index()

res = avg_ratings[avg_ratings['rating'] >= 4.5].sort_values('rating', ascending=False)

result = res.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_S8KfkaFJkm3UbNGELQuBWZuN': 'file_storage/call_S8KfkaFJkm3UbNGELQuBWZuN.json', 'var_call_AlVrg6ZrzKsT51gHVbV9eyZY': ['review'], 'var_call_wOjly9pP9p5bvzvMBBaM6sic': 'file_storage/call_wOjly9pP9p5bvzvMBBaM6sic.json'}

exec(code, env_args)
