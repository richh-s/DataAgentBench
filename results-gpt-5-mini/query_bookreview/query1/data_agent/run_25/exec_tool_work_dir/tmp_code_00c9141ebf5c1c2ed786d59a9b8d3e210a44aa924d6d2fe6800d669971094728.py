code = """import json
import re
import pandas as pd

# Load data from storage variables (they may be file paths or lists)
reviews_var = var_call_MyId8mdVLrVtojHMJW2xs9TM
books_var = var_call_vW6yU6yl3aiYQgMIFLPcgkNL

def load_var(v):
    if isinstance(v, str):
        # assume this is a filepath to a JSON file
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

reviews = load_var(reviews_var)
books = load_var(books_var)

rv_df = pd.DataFrame(reviews)
bk_df = pd.DataFrame(books)

# Normalize rating to float
rv_df['rating'] = pd.to_numeric(rv_df['rating'], errors='coerce')

# Extract numeric id from purchase_id and book_id
def extract_num(s):
    if pd.isna(s):
        return None
    m = re.search(r'(\d+)$', str(s))
    return int(m.group(1)) if m else None

rv_df['num_id'] = rv_df['purchase_id'].apply(extract_num)
bk_df['num_id'] = bk_df['book_id'].apply(extract_num)

# Merge on numeric id
merged = pd.merge(rv_df, bk_df[['book_id','details','num_id']], on='num_id', how='left')

# Function to extract a plausible publication year from details
def extract_year(text):
    if not isinstance(text, str):
        return None
    # find all 4-digit numbers between 1500 and 2023
    years = re.findall(r'\b(1[5-9]\d{2}|20\d{2})\b', text)
    if not years:
        # also catch 1945 etc (19xx)
        years = re.findall(r'\b(19\d{2})\b', text)
    # years may include >2023, filter
    for y in years:
        try:
            yi = int(y)
            if 1500 <= yi <= 2023:
                return yi
        except:
            continue
    return None

merged['pub_year'] = merged['details'].apply(extract_year)

# Drop rows without pub_year or without book_id
merged = merged[merged['pub_year'].notna() & merged['book_id'].notna()]

# Compute decade string per book
merged['decade_start'] = (merged['pub_year'] // 10) * 10
merged['decade'] = merged['decade_start'].astype(int).astype(str) + 's'

# Compute per-book average rating (for books that have at least one rating)
book_avgs = merged.groupby('book_id').agg({
    'rating': 'mean',
    'decade': lambda x: x.mode().iloc[0] if not x.mode().empty else x.iloc[0]
}).rename(columns={'rating':'book_avg_rating'}).reset_index()

# Now compute per-decade stats: number of distinct books and average of book averages
decade_stats = book_avgs.groupby('decade').agg(
    distinct_books=('book_id','nunique'),
    decade_avg_rating=('book_avg_rating','mean')
).reset_index()

# Filter decades with at least 10 distinct books
eligible = decade_stats[decade_stats['distinct_books'] >= 10]

if eligible.empty:
    result = {'decade': None, 'decade_avg_rating': None, 'distinct_books': 0}
else:
    # select decade with highest average rating; if tie, take the one with more books, then earliest decade
    eligible_sorted = eligible.sort_values(by=['decade_avg_rating','distinct_books','decade'], ascending=[False, False, True])
    top = eligible_sorted.iloc[0]
    result = {
        'decade': top['decade'],
        'decade_avg_rating': round(float(top['decade_avg_rating']), 4),
        'distinct_books': int(top['distinct_books'])
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ecpYdauCnUEflfIyECFObCv4': ['review'], 'var_call_MdQ2J5L1juUqLUJPjcC5pD9x': ['books_info'], 'var_call_MyId8mdVLrVtojHMJW2xs9TM': 'file_storage/call_MyId8mdVLrVtojHMJW2xs9TM.json', 'var_call_vW6yU6yl3aiYQgMIFLPcgkNL': 'file_storage/call_vW6yU6yl3aiYQgMIFLPcgkNL.json'}

exec(code, env_args)
