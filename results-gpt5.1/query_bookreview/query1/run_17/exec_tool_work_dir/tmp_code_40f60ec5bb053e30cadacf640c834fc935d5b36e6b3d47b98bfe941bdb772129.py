code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_9jP8VJV39rgBFlukEyRcb2XK, 'r') as f:
    review_avg = json.load(f)
with open(var_call_6X9M1yf8Pm5QlmTjjqpW2fLR, 'r') as f:
    books = json.load(f)

# Build DataFrames
df_reviews = pd.DataFrame(review_avg)
df_books = pd.DataFrame(books)

# Extract publication year from details using regex, many patterns like 'on January 1, 2004', 'on May 18, 2014', 'on January 1, 1945', 'in 2012', etc.

year_pattern = re.compile(r'(19|20)\d{2}')

def extract_year(text):
    if not isinstance(text, str):
        return None
    m = year_pattern.search(text)
    return int(m.group(0)) if m else None

df_books['pub_year'] = df_books['details'].apply(extract_year)

# Map purchase_id to book_id via simple exact id scheme: assume purchaseid_X corresponds to bookid_X
# Create numeric part columns

def extract_num(s, prefix):
    if not isinstance(s, str):
        return None
    m = re.match(prefix + r'(\d+)$', s)
    return int(m.group(1)) if m else None

df_reviews['num'] = df_reviews['purchase_id'].apply(lambda s: extract_num(s, 'purchaseid_'))
df_books['num'] = df_books['book_id'].apply(lambda s: extract_num(s, 'bookid_'))

# Merge on numeric part where available
merged = pd.merge(df_reviews, df_books, on='num', how='inner')

# Keep only rows with publication year
merged = merged.dropna(subset=['pub_year'])

# Convert avg_rating to float
merged['avg_rating'] = merged['avg_rating'].astype(float)

# Compute decade
merged['decade'] = (merged['pub_year'] // 10) * 10

# For each decade, compute number of distinct books (book_id) and average of avg_rating
agg = merged.groupby('decade').agg(
    distinct_books=('book_id', 'nunique'),
    decade_avg_rating=('avg_rating', 'mean')
).reset_index()

# Filter decades with at least 10 distinct books with ratings
eligible = agg[agg['distinct_books'] >= 10]

if eligible.empty:
    result = None
else:
    best_row = eligible.sort_values('decade_avg_rating', ascending=False).iloc[0]
    decade_label = f"{int(best_row['decade'])}s"
    result = decade_label

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_6X9M1yf8Pm5QlmTjjqpW2fLR': 'file_storage/call_6X9M1yf8Pm5QlmTjjqpW2fLR.json', 'var_call_EjLbOJUHqXMcBV3ALhR0UAuZ': ['review'], 'var_call_9jP8VJV39rgBFlukEyRcb2XK': 'file_storage/call_9jP8VJV39rgBFlukEyRcb2XK.json'}

exec(code, env_args)
