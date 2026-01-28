code = """import json
import pandas as pd
import re

# Load the query results from storage files
with open(var_call_5GpLjTMeav25PQSBHqR6wEsM, 'r') as f:
    books = json.load(f)

with open(var_call_2D0KL4ETj8BEU4Y4wGcI0ucP, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# Convert avg_rating to float
df_reviews['avg_rating'] = pd.to_numeric(df_reviews['avg_rating'], errors='coerce')

# Map purchase_id -> book_id by replacing prefix
# Handle possible mismatches by a simple replacement
if 'purchase_id' in df_reviews.columns:
    df_reviews['book_id'] = df_reviews['purchase_id'].str.replace('purchaseid_', 'bookid_', regex=False)

# Merge on book_id
df_merged = pd.merge(df_reviews, df_books[['book_id', 'details']], on='book_id', how='inner')

# Function to extract a valid publication year (1000-2023) from details text
def extract_year(text):
    if not isinstance(text, str):
        return None
    # Find all 4-digit numbers
    years = re.findall(r'(\d{4})', text)
    for y in years:
        try:
            yi = int(y)
            if 1000 <= yi <= 2023:
                return yi
        except:
            continue
    return None

# Extract year and decade
df_merged['year'] = df_merged['details'].apply(extract_year)
# Drop rows without year or without avg_rating
df_merged = df_merged.dropna(subset=['year', 'avg_rating'])

# Compute decade label
df_merged['decade'] = df_merged['year'].astype(int).floordiv(10).mul(10).astype(int).astype(str) + 's'

# For each distinct book (book_id) we have an avg_rating already; group by decade
grp = df_merged.groupby('decade').agg(distinct_books=('book_id', 'nunique'), avg_of_book_avg=('avg_rating', 'mean'))

# Filter decades with at least 10 distinct books
grp_filtered = grp[grp['distinct_books'] >= 10]

# If no decade meets criteria, return None
if grp_filtered.empty:
    result = {'decade_with_highest_avg': None}
else:
    # Find decade with highest average rating (if ties, choose the one with highest avg; pandas idxmax returns first)
    top_decade = grp_filtered['avg_of_book_avg'].idxmax()
    top_avg = float(grp_filtered.loc[top_decade, 'avg_of_book_avg'])
    top_count = int(grp_filtered.loc[top_decade, 'distinct_books'])
    result = {'decade_with_highest_avg': top_decade, 'average_rating': round(top_avg, 4), 'distinct_books': top_count}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Wp6Tco4PhM5OwSa8hUqDzvlN': ['review'], 'var_call_nYT9U2aMLph9JPSZQnbivaPT': ['books_info'], 'var_call_5GpLjTMeav25PQSBHqR6wEsM': 'file_storage/call_5GpLjTMeav25PQSBHqR6wEsM.json', 'var_call_2D0KL4ETj8BEU4Y4wGcI0ucP': 'file_storage/call_2D0KL4ETj8BEU4Y4wGcI0ucP.json'}

exec(code, env_args)
