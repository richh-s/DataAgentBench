code = """import json, re, pandas as pd

# Load full books details
with open(var_call_sbxVBH3vG5p1341xkJUKazEA, 'r') as f:
    books = json.load(f)

reviews = var_call_UK9JEAKrQiHMdXHSuzCkkF1W

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# extract year from details text
def extract_year(text):
    if not isinstance(text, str):
        return None
    m = re.search(r"(19|20)\d{2}", text)
    if m:
        return int(m.group(0))
    return None

books_df['year'] = books_df['details'].apply(extract_year)
books_df['decade'] = books_df['year'].apply(lambda y: (y//10)*10 if pd.notnull(y) else None)

# join reviews to books on purchase_id/book_id (they seem to match exactly in sample)
merged = reviews_df.merge(books_df[['book_id','decade']], left_on='purchase_id', right_on='book_id', how='inner')

# cast rating to float
merged['rating'] = merged['rating'].astype(float)

# compute per-book average rating
book_avg = merged.groupby(['book_id','decade'])['rating'].mean().reset_index(name='book_avg_rating')

# filter books with at least one rating already implied; requirement is per decade with >=10 distinct books
# compute decade stats
decade_stats = book_avg.groupby('decade').agg(
    n_books=('book_id','nunique'),
    decade_avg_rating=('book_avg_rating','mean')
).reset_index()

eligible = decade_stats[decade_stats['n_books'] >= 10]

if eligible.empty:
    result = None
else:
    top = eligible.sort_values('decade_avg_rating', ascending=False).iloc[0]
    decade_label = f"{int(top['decade'])}s"
    result = decade_label

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_sbxVBH3vG5p1341xkJUKazEA': 'file_storage/call_sbxVBH3vG5p1341xkJUKazEA.json', 'var_call_mcSFSA5rZtzSiOs9x3eXIQ0t': ['books_info'], 'var_call_f0HYJrbvEZ5KxQOVUhezB4mP': ['review'], 'var_call_UK9JEAKrQiHMdXHSuzCkkF1W': 'file_storage/call_UK9JEAKrQiHMdXHSuzCkkF1W.json'}

exec(code, env_args)
