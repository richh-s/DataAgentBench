code = """import json, re, pandas as pd

# Load full books_info data
with open(var_call_DsD8NWTEIxYwZyngauIpQmhO, 'r') as f:
    books = json.load(f)

books_df = pd.DataFrame(books)

# Extract publication year from 'details' using regex on patterns like 'on January 1, 2004' or 'on May 18, 2014' etc.

def extract_year(details):
    if not isinstance(details, str):
        return None
    # common patterns: 'on January 1, 2004', 'on May 18, 2014', 'on  January 1, 1993', 'on March 20, 1995', 'on January 1, 1945'
    m = re.search(r'on [A-Za-z]+\s+\d{1,2},\s*(\d{4})', details)
    if m:
        return int(m.group(1))
    # sometimes: 'released on November 15, 2000', 'released on January 1, 1997'
    m = re.search(r'released on [A-Za-z]+\s+\d{1,2},\s*(\d{4})', details)
    if m:
        return int(m.group(1))
    # sometimes: 'on January 1, 1993' without preceding words
    m = re.search(r'\b(\d{4})\b', details)
    if m:
        year = int(m.group(1))
        if 1500 <= year <= 2100:
            return year
    return None

books_df['year'] = books_df['details'].apply(extract_year)
books_df['decade'] = (books_df['year'] // 10 * 10).astype('Int64')

# Load full review data
with open(var_call_TTSsa0S79moTnDfyusSoHrUC, 'r') as f:
    reviews = json.load(f)

reviews_df = pd.DataFrame(reviews)
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')

# Fuzzy join purchase_id <-> book_id: they seem to be like 'purchaseid_186' vs 'bookid_186'
# Map purchaseid_X -> X and bookid_X -> X

def extract_numeric_id(x):
    if not isinstance(x, str):
        return None
    m = re.search(r'_(\d+)$', x)
    return int(m.group(1)) if m else None

books_df['num_id'] = books_df['book_id'].apply(extract_numeric_id)
reviews_df['num_id'] = reviews_df['purchase_id'].apply(extract_numeric_id)

merged = pd.merge(reviews_df, books_df[['book_id','num_id','decade']], on='num_id', how='inner')

# Compute average rating per book (distinct book_id)
book_avg = merged.groupby(['book_id','decade'], dropna=True)['rating'].mean().reset_index(name='book_avg_rating')

# Filter to decades where there are at least 10 distinct books with ratings
decade_stats = book_avg.groupby('decade').agg(num_books=('book_id','nunique'), decade_avg=('book_avg_rating','mean')).reset_index()
eligible = decade_stats[decade_stats['num_books'] >= 10]

if eligible.empty:
    result = None
else:
    best_row = eligible.sort_values(['decade_avg','decade'], ascending=[False, True]).iloc[0]
    decade = int(best_row['decade'])
    result = f"{decade}s"

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_DsD8NWTEIxYwZyngauIpQmhO': 'file_storage/call_DsD8NWTEIxYwZyngauIpQmhO.json', 'var_call_ZwgXbmDOH4UmpSMeDS4ExSgf': ['review'], 'var_call_TTSsa0S79moTnDfyusSoHrUC': 'file_storage/call_TTSsa0S79moTnDfyusSoHrUC.json'}

exec(code, env_args)
