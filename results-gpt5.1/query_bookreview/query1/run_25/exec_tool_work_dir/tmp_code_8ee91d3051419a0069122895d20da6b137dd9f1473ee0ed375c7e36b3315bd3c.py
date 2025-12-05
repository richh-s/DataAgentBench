code = """import json, re, pandas as pd

# Load full reviews aggregate from file
path = var_call_4mjXIte44JFy7OTYBfsTWqXO
with open(path, 'r') as f:
    reviews = json.load(f)

# Load all books_info rows from file path stored in var_call_QDiVZxiZKWxVgQgADDZHX6lE
books_path = var_call_QDiVZxiZKWxVgQgADDZHX6lE
with open(books_path, 'r') as f:
    books = json.load(f)

reviews_df = pd.DataFrame(reviews)
books_df = pd.DataFrame(books)

year_pattern = re.compile(r"(19\d{2}|20\d{2})")

def extract_year(details):
    if not isinstance(details, str):
        return None
    years = year_pattern.findall(details)
    if not years:
        return None
    years_int = sorted(int(y) for y in years)
    return years_int[0]

books_df['pub_year'] = books_df['details'].apply(extract_year)
books_df['decade'] = books_df['pub_year'].apply(lambda y: None if pd.isna(y) else int(y//10*10))


def id_to_num(x):
    if not isinstance(x, str):
        return None
    m = re.search(r"(\d+)$", x)
    return m.group(1) if m else None

reviews_df['id_num'] = reviews_df['purchase_id'].apply(id_to_num)
books_df['id_num'] = books_df['book_id'].apply(id_to_num)

merged = pd.merge(reviews_df, books_df[['book_id','id_num','decade']], on='id_num', how='inner')

merged = merged[merged['decade'].notna()]

merged['avg_rating'] = merged['avg_rating'].astype(float)

book_avg = merged.groupby(['book_id','decade'], as_index=False)['avg_rating'].mean()

decade_stats = book_avg.groupby('decade').agg(num_books=('book_id','nunique'), decade_avg_rating=('avg_rating','mean')).reset_index()

decade_stats = decade_stats[decade_stats['num_books'] >= 10]

if decade_stats.empty:
    result = None
else:
    max_avg = decade_stats['decade_avg_rating'].max()
    candidates = decade_stats[decade_stats['decade_avg_rating'] == max_avg]
    best_decade = candidates['decade'].max()
    result = f"{int(best_decade)}s"

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_QDiVZxiZKWxVgQgADDZHX6lE': 'file_storage/call_QDiVZxiZKWxVgQgADDZHX6lE.json', 'var_call_sWfKwU8tczFxO5s7otXkXhKn': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}], 'var_call_a3kBBHuYBKbOE0VxP5IICctn': ['review'], 'var_call_4mjXIte44JFy7OTYBfsTWqXO': 'file_storage/call_4mjXIte44JFy7OTYBfsTWqXO.json'}

exec(code, env_args)
