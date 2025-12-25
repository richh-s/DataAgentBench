code = """import json, re, pandas as pd

# Load full files
with open(var_call_SLuR0Nm3Yg1nHgZSZvhsw3dJ, 'r') as f:
    reviews = json.load(f)
with open(var_call_MfGlobIMeT2pze96Gn4olnrn, 'r') as f:
    books = json.load(f)

rev_df = pd.DataFrame(reviews)
books_df = pd.DataFrame(books)

# Ensure numeric ratings
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
rev_df = rev_df.dropna(subset=['rating'])

# Fuzzy join via ID pattern: assume purchaseid_X maps to bookid_X
def map_purchase_to_book(pid):
    m = re.search(r'(\d+)$', str(pid))
    return f'bookid_{m.group(1)}' if m else None

rev_df['book_id'] = rev_df['purchase_id'].apply(map_purchase_to_book)

# Extract publication year from details
year_pattern = re.compile(r'(19|20)\d{2}')

def extract_year(details):
    if not isinstance(details, str):
        return None
    # Look for phrases like '2004' preferably near 'published' or 'edition' or explicit date
    years = year_pattern.findall(details)
    # year_pattern with groups returns tuples; recompute properly
    years2 = re.findall(r'(?:19|20)\d{2}', details)
    if not years2:
        return None
    # Heuristic: earliest year is likely original publication
    return int(sorted(set(int(y) for y in years2))[0])

books_df['pub_year'] = books_df['details'].apply(extract_year)
books_df = books_df.dropna(subset=['pub_year'])
books_df['pub_year'] = books_df['pub_year'].astype(int)
books_df['decade'] = (books_df['pub_year'] // 10) * 10

# Merge reviews with books via book_id
merged = pd.merge(rev_df, books_df[['book_id','decade']], on='book_id', how='inner')

# Compute per-book average rating
book_avg = merged.groupby(['book_id','decade'])['rating'].mean().reset_index(name='book_avg_rating')

# For each decade, keep books with at least one rating, then require at least 10 distinct books
decade_book_counts = book_avg.groupby('decade')['book_id'].nunique().reset_index(name='book_count')
eligible_decades = decade_book_counts[decade_book_counts['book_count'] >= 10]['decade']

if eligible_decades.empty:
    result = None
else:
    eligible = book_avg[book_avg['decade'].isin(eligible_decades)]
    decade_avg = eligible.groupby('decade')['book_avg_rating'].mean().reset_index(name='decade_avg_rating')
    best_row = decade_avg.sort_values('decade_avg_rating', ascending=False).iloc[0]
    result = {
        'decade': int(best_row['decade']),
        'label': f"{int(best_row['decade'])}s",
        'average_rating': round(float(best_row['decade_avg_rating']), 3)
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_MfGlobIMeT2pze96Gn4olnrn': 'file_storage/call_MfGlobIMeT2pze96Gn4olnrn.json', 'var_call_ajRfpkphilabfUbvQD3PmETf': ['review'], 'var_call_SLuR0Nm3Yg1nHgZSZvhsw3dJ': 'file_storage/call_SLuR0Nm3Yg1nHgZSZvhsw3dJ.json'}

exec(code, env_args)
