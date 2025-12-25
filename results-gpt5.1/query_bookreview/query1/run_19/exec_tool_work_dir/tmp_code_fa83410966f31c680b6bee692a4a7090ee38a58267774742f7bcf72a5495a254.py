code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_8rwhmcQGWfuqNkRu5aNe6D0I, 'r') as f:
    ratings = json.load(f)
with open(var_call_TDJDp141PWKNvlShNKp9B4qm, 'r') as f:
    books = json.load(f)

ratings_df = pd.DataFrame(ratings)
books_df = pd.DataFrame(books)

# Ensure numeric avg_rating
ratings_df['avg_rating'] = pd.to_numeric(ratings_df['avg_rating'], errors='coerce')

# Extract publication year from details using regex
year_pattern = re.compile(r'(19|20)\d{2}')

def extract_year(details):
    if not isinstance(details, str):
        return None
    # Look for phrases like 'published ... on <Month> <day>, <year>' or 'released on <Month> <day>, <year>'
    matches = year_pattern.findall(details)
    if not matches:
        return None
    # year_pattern with group returns tuples; reconstruct
    years = []
    for m in matches:
        if isinstance(m, tuple):
            years.append(int(''.join(m) + details))
        else:
            try:
                years.append(int(m))
            except:
                pass
    # Simpler: re-find with full match
    full_matches = re.findall(r'(?:19|20)\d{2}', details)
    if not full_matches:
        return None
    years = [int(y) for y in full_matches]
    # Heuristic: earliest year is likely publication year
    return min(years)

books_df['pub_year'] = books_df['details'].apply(extract_year)
books_df['decade'] = books_df['pub_year'].apply(lambda y: int(y//10*10) if pd.notnull(y) else None)

# Join ratings with books on purchase_id ~ book_id (exact string equality per hint)
merged = ratings_df.merge(books_df[['book_id','decade']], left_on='purchase_id', right_on='book_id', how='inner')

# Drop rows without decade
merged = merged.dropna(subset=['decade'])

# Compute per-decade stats: number of distinct books and average rating across books
book_stats = merged.groupby(['decade','book_id'])['avg_rating'].mean().reset_index(name='book_avg_rating')

# Filter decades with at least 10 distinct books
decade_book_counts = book_stats.groupby('decade')['book_id'].nunique().reset_index(name='num_books')
eligible_decades = decade_book_counts[decade_book_counts['num_books'] >= 10]['decade']

eligible_stats = book_stats[book_stats['decade'].isin(eligible_decades)]

# Average the book-level averages per decade
decade_avg = eligible_stats.groupby('decade')['book_avg_rating'].mean().reset_index(name='decade_avg_rating')

if decade_avg.empty:
    result = None
else:
    best_row = decade_avg.sort_values('decade_avg_rating', ascending=False).iloc[0]
    result = f"{int(best_row['decade'])}s"

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_TDJDp141PWKNvlShNKp9B4qm': 'file_storage/call_TDJDp141PWKNvlShNKp9B4qm.json', 'var_call_KPTQZF6CiK0VD0XD718NWkqs': ['review'], 'var_call_8rwhmcQGWfuqNkRu5aNe6D0I': 'file_storage/call_8rwhmcQGWfuqNkRu5aNe6D0I.json'}

exec(code, env_args)
