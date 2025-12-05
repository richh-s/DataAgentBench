code = """import json, re, pandas as pd

# Load review data
with open(var_call_SY3yXnoa8J9Q8flKUrcS3EOk, 'r') as f:
    reviews = json.load(f)

# Load books data
with open(var_call_KrI2n1CnYJE9rUrEa9NRKlpL, 'r') as f:
    books = json.load(f)

reviews_df = pd.DataFrame(reviews)
books_df = pd.DataFrame(books)

# Normalize types
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')

# Map purchase_id like 'purchaseid_186' to bookid_186
def purchase_to_book(p):
    return p.replace('purchaseid_', 'bookid_') if isinstance(p, str) else None

reviews_df['book_id'] = reviews_df['purchase_id'].apply(purchase_to_book)

# Extract publication year from details using regex for 4-digit years between, say, 1900 and 2029
year_pattern = re.compile(r'(19\d{2}|20[0-2]\d)')

def extract_year(details):
    if not isinstance(details, str):
        return None
    years = year_pattern.findall(details)
    if not years:
        return None
    # Heuristic: pick the earliest year as publication year
    years_int = sorted(int(y) for y in years)
    return years_int[0]

books_df['pub_year'] = books_df['details'].apply(extract_year)
books_df['decade'] = books_df['pub_year'].dropna().astype('Int64') // 10 * 10

# Merge reviews with book publication decade
merged = pd.merge(reviews_df, books_df[['book_id', 'decade']], on='book_id', how='left')

# Drop rows without decade or rating
merged = merged.dropna(subset=['decade', 'rating'])

# Compute per book average rating then per decade stats
book_avg = merged.groupby(['book_id', 'decade'])['rating'].mean().reset_index(name='book_avg_rating')

# Count distinct books per decade and average their ratings
decade_stats = book_avg.groupby('decade').agg(
    num_books=('book_id', 'nunique'),
    avg_rating=('book_avg_rating', 'mean')
).reset_index()

# Filter decades with at least 10 distinct books
eligible = decade_stats[decade_stats['num_books'] >= 10]

if eligible.empty:
    result = None
else:
    best_row = eligible.sort_values(['avg_rating', 'decade'], ascending=[False, True]).iloc[0]
    decade_int = int(best_row['decade'])
    decade_label = f"{decade_int}s"
    result = {
        'decade': decade_label,
        'average_rating': round(float(best_row['avg_rating']), 3),
        'num_books': int(best_row['num_books'])
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_FMh9Dm90p1gWQKLylvPu0qaT': ['review'], 'var_call_SY3yXnoa8J9Q8flKUrcS3EOk': 'file_storage/call_SY3yXnoa8J9Q8flKUrcS3EOk.json', 'var_call_KrI2n1CnYJE9rUrEa9NRKlpL': 'file_storage/call_KrI2n1CnYJE9rUrEa9NRKlpL.json'}

exec(code, env_args)
