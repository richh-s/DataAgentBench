code = """import json, re
import pandas as pd

# Load previous query results from files
with open(var_call_bgy7NnthY8qVkVhKapqDrr3a, 'r') as f:
    reviews = json.load(f)
with open(var_call_8ukhj5fzRnUrrlkJCdjsgV06, 'r') as f:
    books = json.load(f)

# Create DataFrames
df_reviews = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

# Normalize ratings to numeric
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

# Map purchase_id like 'purchaseid_186' -> 'bookid_186'
# Extract trailing digits
df_reviews['book_num'] = df_reviews['purchase_id'].astype(str).str.extract(r'_(\d+)$')[0]
# Drop rows without numeric mapping
df_reviews = df_reviews[df_reviews['book_num'].notna()].copy()

df_reviews['book_id'] = 'bookid_' + df_reviews['book_num']

# Compute per-book average rating
book_avg = df_reviews.groupby('book_id', as_index=False)['rating'].mean().rename(columns={'rating': 'mean_rating'})

# Extract publication year from books.details using regex for 4-digit years
year_regex = re.compile(r"\b(1[0-9]{3}|20[0-9]{2})\b")

def extract_year(s):
    if not isinstance(s, str):
        return None
    m = year_regex.search(s)
    if m:
        try:
            return int(m.group(0))
        except:
            return None
    return None

df_books['year'] = df_books['details'].apply(extract_year)

# Merge per-book averages with books info to get year
df = pd.merge(book_avg, df_books[['book_id', 'year']], on='book_id', how='left')

# Drop entries without year
df = df[df['year'].notna()].copy()

df['year'] = df['year'].astype(int)
# Compute decade string like '1980s'
df['decade'] = (df['year'] // 10 * 10).astype(int).astype(str) + 's'

# Group by decade: count distinct books and average of per-book mean ratings
grp = df.groupby('decade').agg(book_count=('book_id', 'nunique'), decade_avg_rating=('mean_rating', 'mean')).reset_index()

# Filter decades with at least 10 distinct books
valid = grp[grp['book_count'] >= 10].copy()

result = None
if not valid.empty:
    # Find decade with highest average rating
    best = valid.sort_values(['decade_avg_rating', 'decade'], ascending=[False, True]).iloc[0]
    result = {
        'decade': best['decade'],
        'average_rating': round(float(best['decade_avg_rating']), 4),
        'book_count': int(best['book_count'])
    }
else:
    result = {'decade': None, 'average_rating': None, 'book_count': 0}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_yHT06gPC3OVISNuAFSZ8n22R': ['review'], 'var_call_twVeKBGWWsdjl4D2CJl3AwkY': ['books_info'], 'var_call_bgy7NnthY8qVkVhKapqDrr3a': 'file_storage/call_bgy7NnthY8qVkVhKapqDrr3a.json', 'var_call_8ukhj5fzRnUrrlkJCdjsgV06': 'file_storage/call_8ukhj5fzRnUrrlkJCdjsgV06.json'}

exec(code, env_args)
