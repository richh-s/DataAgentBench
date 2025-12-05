code = """import json, re, pandas as pd

# Load full results
with open(var_call_EtziSOG4z7wOruzXP9j0AB1O, 'r') as f:
    reviews = json.load(f)
with open(var_call_cX45zKhcjNy0ZlDlfb0R73Rs, 'r') as f:
    books = json.load(f)

# Convert to DataFrames
df_reviews = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

# Ensure numeric avg_rating
df_reviews['avg_rating'] = pd.to_numeric(df_reviews['avg_rating'], errors='coerce')

# Extract publication year from details using regex
# Look for patterns like 'on January 1, 2004' or 'on May 20, 1996' or 'on March 20, 1995'
year_pattern = re.compile(r'on\s+\w+\s+\d{1,2},\s+(\d{4})')

def extract_year(details):
    if not isinstance(details, str):
        return None
    m = year_pattern.search(details)
    if m:
        return int(m.group(1))
    # fallback: look for 'on January 1, 1945' etc already caught; maybe generic 'on 2012' etc
    m2 = re.search(r'\b(19\d{2}|20\d{2})\b', details)
    if m2:
        return int(m2.group(1))
    return None

df_books['pub_year'] = df_books['details'].apply(extract_year)

# Keep books with a pub_year
df_books = df_books.dropna(subset=['pub_year'])

# Fuzzy join: purchase_id like 'purchaseid_123' vs book_id like 'bookid_123'
# Extract numeric suffix from both and join on that
num_pattern = re.compile(r'(\d+)$')

def extract_num(s):
    if not isinstance(s, str):
        return None
    m = num_pattern.search(s)
    return int(m.group(1)) if m else None

df_reviews['id_num'] = df_reviews['purchase_id'].apply(extract_num)
df_books['id_num'] = df_books['book_id'].apply(extract_num)

# Drop rows without id_num
df_reviews = df_reviews.dropna(subset=['id_num'])
df_books = df_books.dropna(subset=['id_num'])

# Merge on id_num
merged = pd.merge(df_reviews, df_books[['id_num','pub_year']], on='id_num', how='inner')

# Compute decade
merged['decade'] = (merged['pub_year'] // 10) * 10

# For each book (id_num), we already have avg_rating; now aggregate by decade.
# First, ensure distinct books per decade: count distinct books and filter decades with at least 10 books.
books_per_decade = merged.groupby('decade')['id_num'].nunique().reset_index(name='book_count')
valid_decades = books_per_decade[books_per_decade['book_count'] >= 10]['decade']

filtered = merged[merged['decade'].isin(valid_decades)]

# Average rating per decade (across distinct books). Use mean of book avg_ratings within each decade.
# Since each purchase_id/book appears once, just mean of avg_rating.
decade_avg = filtered.groupby('decade')['avg_rating'].mean().reset_index()

if decade_avg.empty:
    result = None
else:
    best_row = decade_avg.sort_values('avg_rating', ascending=False).iloc[0]
    decade_label = f"{int(best_row['decade'])}s"
    result = decade_label

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_cX45zKhcjNy0ZlDlfb0R73Rs': 'file_storage/call_cX45zKhcjNy0ZlDlfb0R73Rs.json', 'var_call_6nuGecHmW8TUGkqvMt1UresM': ['review'], 'var_call_EtziSOG4z7wOruzXP9j0AB1O': 'file_storage/call_EtziSOG4z7wOruzXP9j0AB1O.json'}

exec(code, env_args)
