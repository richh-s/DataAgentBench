code = """import json
import pandas as pd
import re

# Load data from storage paths provided by previous tool calls
# var_call_pRLFf1uGnd9sIAK58vrpRrTd and var_call_bWD8aiXmknR4yB0zMqClK4JE are available

# Determine whether these are file paths or direct lists
books_path = var_call_pRLFf1uGnd9sIAK58vrpRrTd
reviews_path = var_call_bWD8aiXmknR4yB0zMqClK4JE

# Read JSON files
with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Normalize column names if necessary
# Convert rating to numeric
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')
# Map purchase_id to book_id by replacing prefix
reviews_df['book_id'] = reviews_df['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)

# Parse year from books.details using regex for first 4-digit year between 1000 and 2023
year_re = re.compile(r"\b(1[0-9]{3}|20[0-2][0-9]|2023)\b")

def extract_year(detail):
    if not isinstance(detail, str):
        return None
    m = year_re.search(detail)
    if m:
        try:
            y = int(m.group(1))
            if 1000 <= y <= 2023:
                return y
        except:
            return None
    return None

books_df['pub_year'] = books_df['details'].apply(extract_year)
# Drop books without pub_year
books_df = books_df.dropna(subset=['pub_year'])
books_df['pub_year'] = books_df['pub_year'].astype(int)

# Compute decade label
books_df['decade'] = (books_df['pub_year'] // 10 * 10).astype(int).astype(str) + 's'

# Join reviews and books on book_id
merged = pd.merge(reviews_df, books_df[['book_id','decade']], on='book_id', how='inner')

# Compute per-book average rating
book_avg = merged.groupby('book_id', as_index=False).agg({'rating':'mean', 'decade':'first'})
book_avg.rename(columns={'rating':'avg_rating'}, inplace=True)

# For each decade, compute count of distinct books and average of book averages
decade_stats = book_avg.groupby('decade').agg(book_count=('book_id','nunique'), decade_avg_rating=('avg_rating','mean')).reset_index()

# Filter decades with at least 10 distinct books
decade_stats = decade_stats[decade_stats['book_count'] >= 10]

if decade_stats.empty:
    result = {'decade': None, 'avg_rating': None, 'book_count': 0}
else:
    # Find decade with highest average rating; if tie, choose the decade with more books, then earliest decade
    top = decade_stats.sort_values(by=['decade_avg_rating','book_count','decade'], ascending=[False, False, True]).iloc[0]
    result = {'decade': top['decade'], 'avg_rating': round(float(top['decade_avg_rating']),4), 'book_count': int(top['book_count'])}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HjCwp3kP57Wi9qGfmIhDYN3p': ['books_info'], 'var_call_pRLFf1uGnd9sIAK58vrpRrTd': 'file_storage/call_pRLFf1uGnd9sIAK58vrpRrTd.json', 'var_call_6OqtxT8HeK3FLZ5u4gMbPLp4': ['review'], 'var_call_bWD8aiXmknR4yB0zMqClK4JE': 'file_storage/call_bWD8aiXmknR4yB0zMqClK4JE.json'}

exec(code, env_args)
