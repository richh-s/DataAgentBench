code = """import json
import pandas as pd
import re

# Load data from provided file paths
with open(var_call_pCh6WYZF3Nx6LSCtoM0KUaOo, 'r') as f:
    reviews = json.load(f)
with open(var_call_ktleHPveooDetEpJXbPMHdXS, 'r') as f:
    books = json.load(f)

# Create DataFrames
rev_df = pd.DataFrame(reviews)
books_df = pd.DataFrame(books)

# Clean and convert ratings
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

# Extract numeric id from purchase_id and form book_id
def purchase_to_bookid(pid):
    if not isinstance(pid, str):
        return None
    m = re.search(r'(\d+)$', pid)
    if m:
        return f"bookid_{m.group(1)}"
    m2 = re.search(r'bookid_(\d+)', pid)
    if m2:
        return f"bookid_{m2.group(1)}"
    return None

rev_df['book_id'] = rev_df['purchase_id'].apply(purchase_to_bookid)

# Filter out records without mapped book_id
rev_df = rev_df[rev_df['book_id'].notna()].copy()

# Identify children's books in books_df by checking categories string
def is_childrens(categories):
    if not isinstance(categories, str):
        return False
    return "Children's Books" in categories or "Children\'s Books" in categories

books_df['is_childrens'] = books_df['categories'].apply(is_childrens)
child_books = books_df[books_df['is_childrens']].copy()

# Merge review stats
stats = rev_df.groupby('book_id').agg(avg_rating=('rating','mean'), review_count=('rating','count')).reset_index()

# Join with child books
merged = pd.merge(child_books, stats, on='book_id', how='inner')

# Filter average rating >= 4.5
result_df = merged[merged['avg_rating'] >= 4.5].copy()

# Prepare output
result_df['avg_rating'] = result_df['avg_rating'].round(3)
output = []
for _, row in result_df.sort_values(['avg_rating', 'review_count'], ascending=[False, False]).iterrows():
    output.append({
        'book_id': row['book_id'],
        'title': row['title'],
        'avg_rating': float(row['avg_rating']),
        'review_count': int(row['review_count']),
        'categories': row.get('categories', None)
    })

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_EJKv8l92DeHCibK9lNckmBEu': ['review'], 'var_call_Kcqp7hNO9tyLMsxGPthjK5Y1': ['books_info'], 'var_call_pCh6WYZF3Nx6LSCtoM0KUaOo': 'file_storage/call_pCh6WYZF3Nx6LSCtoM0KUaOo.json', 'var_call_ktleHPveooDetEpJXbPMHdXS': 'file_storage/call_ktleHPveooDetEpJXbPMHdXS.json'}

exec(code, env_args)
