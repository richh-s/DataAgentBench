code = """import json
import pandas as pd
import re

# Load data from storage variables
# var_call_nEKx9HLEybN5j6cENT4T5t5i and var_call_KAKXnWhseGCPFD7c0ftk0GJ5 are provided by previous tool calls

def load_var(var):
    # If var is a string, it's a file path to json
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return var

reviews = load_var(var_call_nEKx9HLEybN5j6cENT4T5t5i)
books = load_var(var_call_KAKXnWhseGCPFD7c0ftk0GJ5)

# Convert to DataFrame
df_rev = pd.DataFrame(reviews)
# Ensure numeric
if 'avg_rating' in df_rev.columns:
    df_rev['avg_rating'] = pd.to_numeric(df_rev['avg_rating'], errors='coerce')

# Extract numeric id
def extract_num_id(s):
    if not isinstance(s, str):
        return None
    m = re.search(r"(\d+)", s)
    return int(m.group(1)) if m else None

df_rev['num_id'] = df_rev['purchase_id'].apply(extract_num_id)

# Books
df_books = pd.DataFrame(books)
# Extract num id from book_id
df_books['num_id'] = df_books['book_id'].apply(extract_num_id)

# Extract year from details using regex for 4-digit years between 1500 and 2023

def extract_year(s):
    if not isinstance(s, str):
        return None
    matches = re.findall(r"(17\d{2}|18\d{2}|19\d{2}|20\d{2})", s)
    if not matches:
        return None
    # pick the first plausible year within 1500-2023
    for m in matches:
        y = int(m)
        if 1500 <= y <= 2023:
            return y
    return None

if 'details' in df_books.columns:
    df_books['year'] = df_books['details'].apply(extract_year)
else:
    df_books['year'] = None

# Merge on num_id
merged = pd.merge(df_books, df_rev[['num_id','avg_rating']], on='num_id', how='inner')

# Drop entries without year or avg_rating
merged = merged.dropna(subset=['year','avg_rating'])
merged['year'] = merged['year'].astype(int)

# Compute decade label
merged['decade_start'] = (merged['year'] // 10) * 10
merged['decade'] = merged['decade_start'].astype(str) + 's'

# For distinct books: ensure unique book_id entries
merged_unique = merged.drop_duplicates(subset=['book_id'])

# Group by decade
grp = merged_unique.groupby('decade').agg(book_count=('book_id','nunique'), avg_rating=('avg_rating','mean')).reset_index()

# Filter decades with at least 10 distinct books
grp_filtered = grp[grp['book_count'] >= 10]

if grp_filtered.empty:
    result = None
else:
    # Find decade with highest average rating
    best = grp_filtered.sort_values(['avg_rating','book_count'], ascending=[False, False]).iloc[0]
    result = {'decade': best['decade'], 'avg_rating': round(float(best['avg_rating']), 6), 'book_count': int(best['book_count'])}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_yHwpd3SU4Euhw2wCiMh9ESVc': ['review'], 'var_call_tQjYsbVtWJZ9pLjGyR7dinda': ['books_info'], 'var_call_nEKx9HLEybN5j6cENT4T5t5i': 'file_storage/call_nEKx9HLEybN5j6cENT4T5t5i.json', 'var_call_KAKXnWhseGCPFD7c0ftk0GJ5': 'file_storage/call_KAKXnWhseGCPFD7c0ftk0GJ5.json'}

exec(code, env_args)
