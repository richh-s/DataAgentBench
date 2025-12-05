code = """import pandas as pd, json, re
from collections import defaultdict

# Load full datasets
with open(var_call_sCLlFRe4SVgrbxiGRNfbtF9L, 'r') as f:
    books = json.load(f)
with open(var_call_Wqol85ShMocfWttUMzMWeslW, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Extract year from details using regex
year_pattern = re.compile(r'(19|20)\d{2}')

def extract_year(text):
    if not isinstance(text, str):
        return None
    m = year_pattern.search(text)
    return int(m.group(0)) if m else None

books_df['year'] = books_df['details'].apply(extract_year)
books_df = books_df.dropna(subset=['year'])
books_df['year'] = books_df['year'].astype(int)
books_df['decade'] = (books_df['year'] // 10) * 10

# Map purchase_id to decade via book_id. The hint suggests fuzzy join, but IDs look distinct, so
# assume purchase_id directly corresponds to book_id when adjusted from 'purchaseid_X' to 'bookid_X'.

def purchase_to_book(pid):
    if not isinstance(pid, str):
        return None
    m = re.match(r'purchaseid_(\d+)', pid)
    if not m:
        return None
    return f'bookid_{m.group(1)}'

reviews_df['book_id'] = reviews_df['purchase_id'].apply(purchase_to_book)

merged = reviews_df.merge(books_df[['book_id','decade']], on='book_id', how='inner')
merged['rating'] = merged['rating'].astype(float)

# Compute per-decade stats with at least 10 distinct books
agg = merged.groupby('decade').agg(avg_rating=('rating','mean'), n_books=('book_id', lambda x: x.nunique())).reset_index()
filtered = agg[agg['n_books'] >= 10]

if filtered.empty:
    result = None
else:
    best = filtered.sort_values('avg_rating', ascending=False).iloc[0]
    decade_str = f"{int(best['decade'])}s"
    result = decade_str

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_UtDF4kzHbd4F5FWGH92kIa44': ['books_info'], 'var_call_riLh8qoft4eDcEmUA77UQujM': ['review'], 'var_call_sCLlFRe4SVgrbxiGRNfbtF9L': 'file_storage/call_sCLlFRe4SVgrbxiGRNfbtF9L.json', 'var_call_Wqol85ShMocfWttUMzMWeslW': 'file_storage/call_Wqol85ShMocfWttUMzMWeslW.json'}

exec(code, env_args)
