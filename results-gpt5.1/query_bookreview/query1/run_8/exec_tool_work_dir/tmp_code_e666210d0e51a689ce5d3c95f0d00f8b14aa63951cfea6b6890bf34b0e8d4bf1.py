code = """import json, pandas as pd, re
from pathlib import Path

# Load full reviews
review_path = Path(var_call_zhEl0WrwIBa0thxtFNt06IH4)
reviews = json.loads(review_path.read_text())

# Load full books details
books_path = Path(var_call_L23UpRAK3iiP5WiKKXbBzIHN)
books = json.loads(books_path.read_text())

# Build dataframes
rev_df = pd.DataFrame(reviews)
rev_df['rating'] = rev_df['rating'].astype(float)

books_df = pd.DataFrame(books)

# Extract publication year from details using regex on first 4-digit year between 1800-2099
year_pattern = re.compile(r"(18|19|20)\d{2}")

def extract_year(text):
    if not isinstance(text, str):
        return None
    m = year_pattern.search(text)
    if m:
        return int(m.group(0))
    return None

books_df['year'] = books_df['details'].apply(extract_year)

# Map purchase_id (reviews) to book_id; here they correspond directly
rev_df = rev_df.rename(columns={'purchase_id': 'book_id'})

# Merge on book_id
merged = rev_df.merge(books_df[['book_id','year']], on='book_id', how='left')

# Drop rows without year
merged = merged.dropna(subset=['year'])

# Compute decade
merged['year'] = merged['year'].astype(int)
merged['decade'] = (merged['year'] // 10) * 10

# Compute average rating per book per decade to ensure distinct books
book_decade = merged.groupby(['book_id','decade'])['rating'].mean().reset_index(name='book_avg_rating')

# Filter decades with at least 10 distinct books
decade_counts = book_decade.groupby('decade')['book_id'].nunique().reset_index(name='n_books')
valid_decades = decade_counts[decade_counts['n_books'] >= 10]['decade']

filtered = book_decade[book_decade['decade'].isin(valid_decades)]

# Compute overall average rating per decade
decade_avg = filtered.groupby('decade')['book_avg_rating'].mean().reset_index()

# Get decade with highest average rating
if not decade_avg.empty:
    best_row = decade_avg.sort_values(['book_avg_rating','decade'], ascending=[False, True]).iloc[0]
    decade_label = f"{int(best_row['decade'])}s"
else:
    decade_label = None

result = json.dumps(decade_label)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_L23UpRAK3iiP5WiKKXbBzIHN': 'file_storage/call_L23UpRAK3iiP5WiKKXbBzIHN.json', 'var_call_9h3vfJtMMArdVZcTe0l4dt4M': [{'book_id': 'bookid_1'}, {'book_id': 'bookid_2'}, {'book_id': 'bookid_3'}, {'book_id': 'bookid_4'}, {'book_id': 'bookid_5'}], 'var_call_WzQe8CnMYiuqzAaI9gCuDq5r': ['review'], 'var_call_zhEl0WrwIBa0thxtFNt06IH4': 'file_storage/call_zhEl0WrwIBa0thxtFNt06IH4.json'}

exec(code, env_args)
