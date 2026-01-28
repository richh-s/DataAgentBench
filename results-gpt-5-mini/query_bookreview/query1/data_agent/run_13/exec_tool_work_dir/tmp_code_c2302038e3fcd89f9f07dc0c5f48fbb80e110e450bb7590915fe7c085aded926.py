code = """import json
import pandas as pd
import re

books_path = var_call_pRLFf1uGnd9sIAK58vrpRrTd
reviews_path = var_call_bWD8aiXmknR4yB0zMqClK4JE
with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)
books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')
reviews_df['book_id'] = reviews_df['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)

# regex
year_re = re.compile(r"\b(1[0-9]{3}|20[0-2][0-9]|2023)\b")
def extract_year(detail):
    if not isinstance(detail, str):
        return None
    m = year_re.search(detail)
    if m:
        try:
            y = int(m.group(1))
            if 1000 <= y <= 2023:
                return y
        except:
            return None
    return None

books_df['pub_year'] = books_df['details'].apply(extract_year)
books_with_year = books_df.dropna(subset=['pub_year'])
books_df['has_year'] = books_df['pub_year'].notna()

# counts
total_books = len(books_df)
books_with_year_count = int(books_df['has_year'].sum())

# decades distribution
books_with_year['decade'] = (books_with_year['pub_year'] // 10 * 10).astype(int).astype(str) + 's'
decade_counts = books_with_year['decade'].value_counts().to_dict()

# merged counts
merged = pd.merge(reviews_df, books_with_year[['book_id','decade']], on='book_id', how='inner')
unique_books_in_merged = merged['book_id'].nunique()
unique_books_per_decade = merged.groupby('decade')['book_id'].nunique().to_dict()

out = {
    'total_books_in_books_db': total_books,
    'books_with_extracted_year': books_with_year_count,
    'decade_counts_in_books_with_year': decade_counts,
    'unique_books_in_reviews_joined_with_books': int(unique_books_in_merged),
    'unique_books_per_decade_in_merged': unique_books_per_decade,
    'sample_books_with_no_year': books_df[books_df['pub_year'].isna()].head(5)[['book_id','title','details']].to_dict(orient='records')
}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_HjCwp3kP57Wi9qGfmIhDYN3p': ['books_info'], 'var_call_pRLFf1uGnd9sIAK58vrpRrTd': 'file_storage/call_pRLFf1uGnd9sIAK58vrpRrTd.json', 'var_call_6OqtxT8HeK3FLZ5u4gMbPLp4': ['review'], 'var_call_bWD8aiXmknR4yB0zMqClK4JE': 'file_storage/call_bWD8aiXmknR4yB0zMqClK4JE.json', 'var_call_4rVGdv08NLfl4bToC7WwgqbT': {'decade': None, 'avg_rating': None, 'book_count': 0}}

exec(code, env_args)
