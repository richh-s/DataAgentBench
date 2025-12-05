code = """import json, re, pandas as pd

with open(var_call_mgfSX46ObKYM4mOmZXAfXos3, 'r') as f:
    ratings = json.load(f)
with open(var_call_OeIYAdjEAjl6ViLF28q38qny, 'r') as f:
    books = json.load(f)

ratings_df = pd.DataFrame(ratings)
books_df = pd.DataFrame(books)

# Fix avg_rating to float
ratings_df['avg_rating'] = ratings_df['avg_rating'].astype(float)

# Fuzzy join on numeric id part
ratings_df['num_id'] = ratings_df['purchase_id'].str.extract(r'(\d+)').astype(int)
books_df['num_id'] = books_df['book_id'].str.extract(r'(\d+)').astype(int)

merged = pd.merge(ratings_df, books_df, on='num_id', how='inner')

# Extract publication year from details
year_regex = re.compile(r'(19|20)\d{2}')

def get_year(details):
    if not isinstance(details, str):
        return None
    matches = year_regex.findall(details)
    # year_regex with group returns tuples like ('19','99') -> join parts
    years = []
    for m in matches:
        if isinstance(m, tuple):
            years.append(int(''.join(m)))
        else:
            years.append(int(m))
    if not years:
        return None
    return min(years)

merged['year'] = merged['details'].apply(get_year)
merged = merged.dropna(subset=['year'])
merged['year'] = merged['year'].astype(int)

# Compute decade label
def decade_label(y):
    base = int(y) // 10 * 10
    return f"{base}s"

merged['decade'] = merged['year'].apply(decade_label)

# Aggregate to book-level average first (already per purchase_id/book), then decade-level
book_decade = merged[['purchase_id','avg_rating','decade']].drop_duplicates(subset=['purchase_id'])

# Filter decades with at least 10 distinct books
decade_stats = book_decade.groupby('decade').agg(
    n_books=('purchase_id','nunique'),
    decade_avg_rating=('avg_rating','mean')
).reset_index()

eligible = decade_stats[decade_stats['n_books'] >= 10]

if eligible.empty:
    result = None
else:
    best = eligible.sort_values('decade_avg_rating', ascending=False).iloc[0]
    result = {
        'decade': best['decade'],
        'average_rating': round(float(best['decade_avg_rating']), 3),
        'n_books': int(best['n_books'])
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_OeIYAdjEAjl6ViLF28q38qny': 'file_storage/call_OeIYAdjEAjl6ViLF28q38qny.json', 'var_call_JKhOa6zEdwuQxOzgdcsepzS1': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}], 'var_call_1DkIiC3fIN7InZJ9bl6JHStt': ['review'], 'var_call_mgfSX46ObKYM4mOmZXAfXos3': 'file_storage/call_mgfSX46ObKYM4mOmZXAfXos3.json', 'var_call_uSfZZljSLoFjAjkjKsK8PVsQ': 'debug'}

exec(code, env_args)
