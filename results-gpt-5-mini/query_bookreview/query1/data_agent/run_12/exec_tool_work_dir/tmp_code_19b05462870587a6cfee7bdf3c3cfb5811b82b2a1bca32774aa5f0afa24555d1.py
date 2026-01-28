code = """import json, re
import pandas as pd

# Load data from storage-provided file paths
with open(var_call_6WoZDfl8aCkmE0RSXKjlX7Va, 'r', encoding='utf-8') as f:
    reviews_data = json.load(f)
with open(var_call_T9KH1XmrNQShZQzpEwHBejfe, 'r', encoding='utf-8') as f:
    books_data = json.load(f)

# Create DataFrames
df_rev = pd.DataFrame(reviews_data)
df_books = pd.DataFrame(books_data)

# Ensure columns exist
if 'purchase_id' not in df_rev.columns or 'rating' not in df_rev.columns:
    result = "No review data available"
else:
    # Clean ratings
    df_rev = df_rev[df_rev['purchase_id'].notna() & df_rev['rating'].notna()].copy()
    df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')
    df_rev = df_rev[df_rev['rating'].notna()]

    # Map purchase_id to book_id by replacing prefix
    df_rev['book_id'] = df_rev['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)

    # Compute per-book average rating
    book_avg = df_rev.groupby('book_id', as_index=False)['rating'].mean().rename(columns={'rating': 'avg_rating'})

    # Merge with books to get details
    if 'book_id' not in df_books.columns or 'details' not in df_books.columns:
        result = "No book details available"
    else:
        df_merged = pd.merge(book_avg, df_books[['book_id', 'details']], on='book_id', how='left')

        # Extract year from details using regex for years between 1500 and 2029
        year_re = re.compile(r'(?<!\d)(1[5-9]\d{2}|20[0-2]\d)(?!\d)')
        def extract_year(text):
            if not isinstance(text, str):
                return None
            m = year_re.search(text)
            return int(m.group(0)) if m else None

        df_merged['year'] = df_merged['details'].apply(extract_year)
        df_merged = df_merged[df_merged['year'].notna()].copy()
        df_merged['year'] = df_merged['year'].astype(int)

        # Compute decade label
        df_merged['decade_start'] = (df_merged['year'] // 10) * 10
        df_merged['decade'] = df_merged['decade_start'].astype(str) + 's'

        # Group by decade, count distinct books and average the per-book average ratings
        grp = df_merged.groupby('decade').agg(
            n_books=('book_id', 'nunique'),
            avg_rating=('avg_rating', 'mean')
        ).reset_index()

        # Filter decades with at least 10 distinct books
        grp_filtered = grp[grp['n_books'] >= 10].copy()

        if grp_filtered.empty:
            result = "No decade with at least 10 distinct books rated found"
        else:
            # Find decade with highest average rating; in case of tie, pick the earliest decade by average_rating then by decade_start
            max_avg = grp_filtered['avg_rating'].max()
            best = grp_filtered[grp_filtered['avg_rating'] == max_avg].sort_values('decade').iloc[0]
            result = best['decade']

# Print result in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_oSrnGUMcLijZZXBkDFBtkuNU': ['review'], 'var_call_6WoZDfl8aCkmE0RSXKjlX7Va': 'file_storage/call_6WoZDfl8aCkmE0RSXKjlX7Va.json', 'var_call_7UKOzxxv6jjDxlSeFidkoHvz': ['books_info'], 'var_call_T9KH1XmrNQShZQzpEwHBejfe': 'file_storage/call_T9KH1XmrNQShZQzpEwHBejfe.json'}

exec(code, env_args)
