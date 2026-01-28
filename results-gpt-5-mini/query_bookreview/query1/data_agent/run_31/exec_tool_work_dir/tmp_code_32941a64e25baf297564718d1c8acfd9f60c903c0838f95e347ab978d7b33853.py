code = """import json
import pandas as pd
import re

# Load data from previous tool calls (file paths are stored in these variables)
reviews = json.load(open(var_call_WlrGLx1LCFgDgKZLmUueijnS, 'r'))
books = json.load(open(var_call_vKWiF2E5uXPzS29UGFqvx2dZ, 'r'))

df_rev = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

# Clean ratings
df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')
# Map purchase_id like 'purchaseid_186' -> 'bookid_186'
df_rev['book_id'] = df_rev['purchase_id'].astype(str).str.replace(r'^purchaseid_', 'bookid_', regex=True)

# Extract year from books.details using regex
def extract_year(details):
    if not isinstance(details, str):
        return None
    m = re.search(r'(19|20)\d{2}', details)
    if m:
        try:
            y = int(m.group(0))
            return y
        except:
            return None
    return None

# Apply extraction
df_books['year'] = df_books['details'].apply(extract_year)

# Merge reviews with books on book_id
merged = pd.merge(df_rev, df_books[['book_id','year']], on='book_id', how='inner')

# Drop rows with missing rating or year
merged = merged.dropna(subset=['rating','year'])
merged['year'] = merged['year'].astype(int)

# Compute per-book average rating
book_means = merged.groupby('book_id', as_index=False).agg({'rating':'mean','year':'first'})
book_means.rename(columns={'rating':'book_avg_rating'}, inplace=True)

# Compute decade for each book
book_means['decade'] = (book_means['year'] // 10 * 10).astype(int).astype(str) + 's'

# Group by decade: count distinct books and average of book averages
decade_stats = book_means.groupby('decade', as_index=False).agg(
    book_count=('book_id','nunique'),
    avg_rating=('book_avg_rating','mean')
)

# Filter decades with at least 10 distinct books
eligible = decade_stats[decade_stats['book_count'] >= 10]

result = None
if eligible.empty:
    result = {'decade': None, 'average_rating': None, 'book_count': 0}
else:
    # Find decade with highest average rating
    best = eligible.sort_values(['avg_rating','book_count'], ascending=[False, False]).iloc[0]
    result = {
        'decade': best['decade'],
        'average_rating': round(float(best['avg_rating']), 4),
        'book_count': int(best['book_count'])
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NfzZsjAtgRkJ5YXx1km4y2Sj': ['review'], 'var_call_WlrGLx1LCFgDgKZLmUueijnS': 'file_storage/call_WlrGLx1LCFgDgKZLmUueijnS.json', 'var_call_Gbq9AbdQy5kJiZMvin2CJhUj': ['books_info'], 'var_call_vKWiF2E5uXPzS29UGFqvx2dZ': 'file_storage/call_vKWiF2E5uXPzS29UGFqvx2dZ.json'}

exec(code, env_args)
