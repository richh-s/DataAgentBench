code = """import json, re, pandas as pd
# Load data from storage file paths
with open(var_call_hJhSKxNPsIMtotEo12gIULBh, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(var_call_pzh5iwAXLY2XmL5KLbUzpHZ1, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# DataFrames
df_b = pd.DataFrame(books)
df_r = pd.DataFrame(reviews)

# Clean ratings
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = pd.NA

# Map purchase_id -> book_id by extracting digits
if 'purchase_id' in df_r.columns:
    df_r['num'] = df_r['purchase_id'].astype(str).str.extract(r'(\d+)')
    df_r['book_id'] = 'bookid_' + df_r['num'].astype(str)
else:
    df_r['book_id'] = None

# Per-book average rating
book_avg = df_r.groupby('book_id', as_index=False)['rating'].mean()
book_avg.rename(columns={'rating':'avg_rating'}, inplace=True)

# Extract publication year from details (take earliest year found between 1500 and 2023)
def extract_year(s):
    if not isinstance(s, str):
        return None
    yrs = re.findall(r'\b(1[5-9]\d{2}|20\d{2})\b', s)
    yrs = [int(y) for y in yrs if 1500 <= int(y) <= 2023]
    if not yrs:
        return None
    return min(yrs)

if 'details' in df_b.columns:
    df_b['year'] = df_b['details'].apply(extract_year)
else:
    df_b['year'] = None

# Keep relevant columns
df_b = df_b[['book_id', 'title', 'year']]

# Merge book averages with book info
df = pd.merge(book_avg, df_b, on='book_id', how='left')

# Drop rows without a parsed year or without a book_id
df = df[df['book_id'].notna()]
df = df[df['year'].notna()]
if not df.empty:
    df['year'] = df['year'].astype(int)
    df['decade'] = (df['year'] // 10 * 10).astype(str) + 's'

# Compute per-decade statistics: number of distinct books and mean of per-book averages
if df.empty:
    result = None
else:
    decade_group = df.groupby('decade').agg(book_count=('book_id','nunique'), decade_avg=('avg_rating','mean')).reset_index()
    decade_group = decade_group[decade_group['book_count'] >= 10]
    if decade_group.empty:
        result = None
    else:
        top = decade_group.sort_values(['decade_avg','decade'], ascending=[False, True]).iloc[0]
        result = top['decade']

# Output result as JSON-serializable string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_4Z9Zd6jcwuhvA5oZKBdtSYSf': ['books_info'], 'var_call_hJhSKxNPsIMtotEo12gIULBh': 'file_storage/call_hJhSKxNPsIMtotEo12gIULBh.json', 'var_call_TEJcLaMXnTWZ11aoucDvsRzm': ['review'], 'var_call_pzh5iwAXLY2XmL5KLbUzpHZ1': 'file_storage/call_pzh5iwAXLY2XmL5KLbUzpHZ1.json'}

exec(code, env_args)
