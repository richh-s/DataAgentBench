code = """import json, re
import pandas as pd

# Load data from storage-provided file paths
books_path = var_call_6V48HU793kqkzE36srvbG2rc
reviews_path = var_call_4jU3qsOwNnv4gODAXNUHZ148

with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# Extract numeric ids
df_books['id_num'] = df_books['book_id'].astype(str).str.extract(r'(\d+)', expand=False)
df_reviews['id_num'] = df_reviews['purchase_id'].astype(str).str.extract(r'(\d+)', expand=False)

# Merge on numeric id
df_merged = pd.merge(df_reviews, df_books, left_on='id_num', right_on='id_num', how='inner', suffixes=('_rev','_book'))

# Convert ratings to float
# Some ratings might be strings; handle gracefully
df_merged['rating'] = pd.to_numeric(df_merged['rating'], errors='coerce')

# Extract publication year from details using regex for 4-digit years (1000-2099)
year_re = re.compile(r"\b(1[0-9]{3}|20[0-9]{2})\b")

def extract_year(details):
    if not isinstance(details, str):
        return None
    m = year_re.search(details)
    if m:
        try:
            return int(m.group(0))
        except:
            return None
    return None

df_merged['pub_year'] = df_merged['details'].apply(extract_year)
# Drop rows without a publication year or without rating
df_merged = df_merged.dropna(subset=['pub_year', 'rating', 'id_num'])

# Compute decade string
df_merged['decade'] = df_merged['pub_year'].astype(int).floordiv(10).mul(10).astype(int).astype(str) + 's'

# Compute per-book average rating and associated decade (a book should have single pub_year but ensure using most common decade per book)
# Determine book's decade by taking the most common decade among its merged rows
book_decade = df_merged.groupby('id_num')['decade'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else x.iloc[0])
book_mean_rating = df_merged.groupby('id_num')['rating'].mean()

books_summary = pd.concat([book_mean_rating, book_decade], axis=1).reset_index()
books_summary.columns = ['id_num', 'avg_rating', 'decade']

# Now compute per-decade stats
decade_stats = books_summary.groupby('decade').agg(num_books=('id_num', 'nunique'), decade_avg_rating=('avg_rating', 'mean')).reset_index()

# Filter decades with at least 10 distinct books
decade_stats_filtered = decade_stats[decade_stats['num_books'] >= 10]

if decade_stats_filtered.empty:
    result = json.dumps('No decade with at least 10 distinct books that have been rated found')
else:
    # Find decade with highest average rating
    top = decade_stats_filtered.sort_values(['decade_avg_rating','decade'], ascending=[False, True]).iloc[0]
    result = json.dumps(top['decade'])

print("__RESULT__:")
print(result)"""

env_args = {'var_call_kiPtII8oe91XNWvvouU9bPbh': ['review'], 'var_call_uVnP3Bi1pPgSYguFwzO9j4wu': ['books_info'], 'var_call_6V48HU793kqkzE36srvbG2rc': 'file_storage/call_6V48HU793kqkzE36srvbG2rc.json', 'var_call_4jU3qsOwNnv4gODAXNUHZ148': 'file_storage/call_4jU3qsOwNnv4gODAXNUHZ148.json'}

exec(code, env_args)
