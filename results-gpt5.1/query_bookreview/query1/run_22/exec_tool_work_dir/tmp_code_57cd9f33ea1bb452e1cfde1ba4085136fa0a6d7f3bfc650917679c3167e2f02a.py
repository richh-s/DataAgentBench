code = """import json, pandas as pd, re

# Load full results
with open(var_call_Ut48gFwM40nolkaXdPKpl4bD, 'r') as f:
    reviews = json.load(f)
with open(var_call_XN8CGDo90FpVSKDqtF28ezrR, 'r') as f:
    books = json.load(f)

# Create DataFrames
df_rev = pd.DataFrame(reviews)
df_rev['avg_rating'] = df_rev['avg_rating'].astype(float)

# Extract publication year from details
pattern = re.compile(r"(19|20)\d{2}")

def extract_year(details):
    if not isinstance(details, str):
        return None
    m = pattern.search(details)
    return int(m.group(0)) if m else None

books_df = pd.DataFrame(books)
books_df['year'] = books_df['details'].apply(extract_year)
books_df = books_df.dropna(subset=['year'])
books_df['year'] = books_df['year'].astype(int)
books_df['decade'] = (books_df['year'] // 10) * 10

# Join on fuzzy id: assume purchase_id like 'purchaseid_123' and book_id like 'bookid_123'
# Extract numeric part
num_pat = re.compile(r"(\d+)")

df_rev['num'] = df_rev['purchase_id'].apply(lambda x: int(num_pat.search(x).group(1)) if isinstance(x,str) and num_pat.search(x) else None)
books_df['num'] = books_df['book_id'].apply(lambda x: int(num_pat.search(x).group(1)) if isinstance(x,str) and num_pat.search(x) else None)

merged = pd.merge(df_rev.dropna(subset=['num']), books_df.dropna(subset=['num']), on='num', how='inner')

# For each decade, consider distinct books (num) with ratings; need decades with at least 10 distinct books
agg = merged.groupby(['decade','num'])['avg_rating'].mean().reset_index()

decade_stats = agg.groupby('decade').agg(distinct_books=('num','nunique'), avg_rating=('avg_rating','mean')).reset_index()

eligible = decade_stats[decade_stats['distinct_books'] >= 10]

if eligible.empty:
    result = None
else:
    best_row = eligible.sort_values('avg_rating', ascending=False).iloc[0]
    decade_str = f"{int(best_row['decade'])}s"
    result = decade_str

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_XN8CGDo90FpVSKDqtF28ezrR': 'file_storage/call_XN8CGDo90FpVSKDqtF28ezrR.json', 'var_call_vdhR4sApbNvCxfsDcnBJmqGT': ['review'], 'var_call_Ut48gFwM40nolkaXdPKpl4bD': 'file_storage/call_Ut48gFwM40nolkaXdPKpl4bD.json'}

exec(code, env_args)
