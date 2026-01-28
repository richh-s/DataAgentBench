code = """import json
import pandas as pd
import re

# Load data from storage file paths
with open(var_call_bmIgUAXKjX8yjxSfPgATyeTy, 'r') as f:
    reviews = json.load(f)
with open(var_call_PqDutk8xXQUKu7IuHjYHFlrN, 'r') as f:
    books = json.load(f)

# Create DataFrames
df_r = pd.DataFrame(reviews)
df_b = pd.DataFrame(books)

# Clean and filter reviews from 2020 onwards
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = pd.Series(dtype=float)

if 'review_time' in df_r.columns:
    df_r['review_time'] = pd.to_datetime(df_r['review_time'], errors='coerce')
else:
    df_r['review_time'] = pd.Series(pd.NaT)

# Filter for reviews on or after 2020-01-01
df_r = df_r[df_r['review_time'] >= pd.Timestamp('2020-01-01')].copy()

# Map purchase_id -> book_id by extracting digits
def to_bookid(pid):
    if pd.isna(pid):
        return None
    m = re.search(r"(\d+)", str(pid))
    if m:
        return 'bookid_' + m.group(1)
    return None

if 'purchase_id' in df_r.columns:
    df_r['book_id'] = df_r['purchase_id'].apply(to_bookid)
else:
    df_r['book_id'] = None

# Drop rows without book_id or rating
df_r = df_r.dropna(subset=['book_id', 'rating'])

# Identify children books via categories string containing "Children's Books"
if 'categories' in df_b.columns:
    df_b['is_children'] = df_b['categories'].astype(str).str.contains("Children's Books", na=False)
else:
    df_b['is_children'] = False

children = df_b[df_b['is_children']].copy()

# Merge reviews with children books
merged = pd.merge(df_r, children[['book_id', 'title']], on='book_id', how='inner')

result = []
if not merged.empty:
    grp = merged.groupby(['book_id', 'title']).agg(avg_rating=('rating', 'mean'), review_count=('rating', 'count')).reset_index()
    grp['avg_rating'] = grp['avg_rating'].round(3)
    # Filter avg_rating >= 4.5
    res = grp[grp['avg_rating'] >= 4.5].sort_values(['avg_rating', 'review_count'], ascending=[False, False])
    result = res.to_dict(orient='records')

# Ensure all types are JSON serializable
for r in result:
    r['avg_rating'] = float(r['avg_rating'])
    r['review_count'] = int(r['review_count'])

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_V4Ay7XT6DZjxMcFI1xYIrbr3': ['review'], 'var_call_xjSOnwYTFge2cGaFGNaZqfAm': ['books_info'], 'var_call_bmIgUAXKjX8yjxSfPgATyeTy': 'file_storage/call_bmIgUAXKjX8yjxSfPgATyeTy.json', 'var_call_PqDutk8xXQUKu7IuHjYHFlrN': 'file_storage/call_PqDutk8xXQUKu7IuHjYHFlrN.json'}

exec(code, env_args)
