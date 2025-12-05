code = """import json, pandas as pd, re
from pathlib import Path

# Load mapping book_id->decade
with open(Path(var_call_Ugmt5Va0mIjHEe5pGb1Uivx9), 'r') as f:
    book_years = json.load(f)
map_df = pd.DataFrame(book_years)

# Build mapping between purchase_id and book_id via numeric suffix
map_df['num'] = map_df['book_id'].str.extract(r'(\d+)$').astype(int)

# Load reviews
with open(Path(var_call_QPq0jaryQdcXSoXiv1DJ5W3B), 'r') as f:
    reviews = json.load(f)
rev_df = pd.DataFrame(reviews)
rev_df['num'] = rev_df['purchase_id'].str.extract(r'(\d+)$').astype(int)
rev_df['rating'] = rev_df['rating'].astype(float)

# Join on numeric id
merged = pd.merge(rev_df, map_df[['num','decade','book_id']], on='num', how='inner')

# Compute per-book average rating
book_avg = merged.groupby('book_id')['rating'].mean().reset_index()
book_avg = book_avg.merge(map_df[['book_id','decade']], on='book_id', how='left')

# Filter decades with at least 10 distinct books rated
decade_counts = book_avg.groupby('decade')['book_id'].nunique().reset_index(name='n_books')
valid_decades = decade_counts[decade_counts['n_books']>=10]['decade']
valid_book_avg = book_avg[book_avg['decade'].isin(valid_decades)]

# Compute decade average of book averages
decade_avg = valid_book_avg.groupby('decade')['rating'].mean().reset_index()

# Find decade with max avg rating
if len(decade_avg)==0:
    result = None
else:
    best_row = decade_avg.sort_values(['rating','decade'], ascending=[False, True]).iloc[0]
    result = int(best_row['decade'])

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_tOUdm6RV9jzUYiES0dAT6dHM': 'file_storage/call_tOUdm6RV9jzUYiES0dAT6dHM.json', 'var_call_Ugmt5Va0mIjHEe5pGb1Uivx9': 'file_storage/call_Ugmt5Va0mIjHEe5pGb1Uivx9.json', 'var_call_XRXANXo50rw1n94N5woaNtPH': ['review'], 'var_call_QPq0jaryQdcXSoXiv1DJ5W3B': 'file_storage/call_QPq0jaryQdcXSoXiv1DJ5W3B.json'}

exec(code, env_args)
