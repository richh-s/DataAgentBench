code = """import json, re, pandas as pd

# Load large results from files
with open(var_call_uchwLGZVLOCuVzXlGZfF1I7G, 'r') as f:
    details_data = json.load(f)
with open(var_call_rXF1TIjEdHBnhLFwzSntItwU, 'r') as f:
    titles_data = json.load(f)
with open(var_call_BOkRWSO36rmsPWexECvXCsbA, 'r') as f:
    review_data = json.load(f)

# Create DataFrames
Details = pd.DataFrame(details_data)  # book_id, details
Titles = pd.DataFrame(titles_data)    # book_id, title
Reviews = pd.DataFrame(review_data)   # purchase_id, rating

# Extract publication year from details text

def extract_year(text):
    if not isinstance(text, str):
        return None
    # look for patterns like 'on January 1, 2004' or 'on May 20, 1996' or ', 2012,' or ' 2013th edition'
    m = re.search(r'(19|20)\d{2}', text)
    if m:
        return int(m.group(0))
    return None

Details['year'] = Details['details'].apply(extract_year)
Details = Details.dropna(subset=['year'])
Details['year'] = Details['year'].astype(int)
Details['decade'] = (Details['year'] // 10) * 10

# Map purchase_id to book_id via fuzzy assumption: ids share the same numeric suffix
# purchaseid_186 -> bookid_186 etc.

def purchase_to_book(pid):
    if not isinstance(pid, str):
        return None
    m = re.search(r'(\d+)$', pid)
    if not m:
        return None
    num = m.group(1)
    return f'bookid_{num}'

Reviews['book_id'] = Reviews['purchase_id'].apply(purchase_to_book)
Reviews['rating'] = Reviews['rating'].astype(float)

# Join Reviews with Details (for decade)
merged = pd.merge(Reviews, Details[['book_id', 'decade']], on='book_id', how='inner')

# For each book_id, compute its average rating (so distinct book rated)
book_avg = merged.groupby(['book_id', 'decade'])['rating'].mean().reset_index(name='book_avg_rating')

# For each decade, consider only when there are at least 10 distinct books
decade_stats = book_avg.groupby('decade').agg(num_books=('book_id', 'nunique'), avg_rating=('book_avg_rating', 'mean')).reset_index()
eligible = decade_stats[decade_stats['num_books'] >= 10]

if eligible.empty:
    result = None
else:
    # decade with highest avg_rating; tie-breaker: earliest decade
    best_row = eligible.sort_values(['avg_rating', 'decade'], ascending=[False, True]).iloc[0]
    decade_str = f"{int(best_row['decade'])}s"
    result = decade_str

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_uchwLGZVLOCuVzXlGZfF1I7G': 'file_storage/call_uchwLGZVLOCuVzXlGZfF1I7G.json', 'var_call_rXF1TIjEdHBnhLFwzSntItwU': 'file_storage/call_rXF1TIjEdHBnhLFwzSntItwU.json', 'var_call_1TQJtYxqrrNAqpQ901CUVdRq': ['review'], 'var_call_BOkRWSO36rmsPWexECvXCsbA': 'file_storage/call_BOkRWSO36rmsPWexECvXCsbA.json'}

exec(code, env_args)
