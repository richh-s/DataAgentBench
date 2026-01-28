code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

books = load_records(var_call_7qHE6SSJopN8SMr6i6l6TN70)
reviews = load_records(var_call_dUIOTWeD0TQ8QlGAdFYOaq0V)

df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# parse year from details
year_re = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_year(s):
    if not isinstance(s, str):
        return None
    # prefer years that appear near 'published'/'released'/'publication'
    m = re.search(r'(?i)(published|released|publication|first edition|edition)\D{0,50}\b(19\d{2}|20\d{2})\b', s)
    if m:
        return int(m.group(2))
    # fallback first plausible year
    m2 = year_re.search(s)
    if m2:
        return int(m2.group(1))
    return None

df_books['year'] = df_books['details'].apply(extract_year)
df_books = df_books.dropna(subset=['year'])
df_books['year'] = df_books['year'].astype(int)
df_books['decade_start'] = (df_books['year']//10)*10

# fuzzy join: purchaseid_X vs bookid_X
get_suffix = lambda x: re.search(r'(\d+)$', str(x)).group(1) if re.search(r'(\d+)$', str(x)) else None

df_reviews['suffix'] = df_reviews['purchase_id'].apply(get_suffix)
df_books['suffix'] = df_books['book_id'].apply(get_suffix)

# rating to float
# ratings stored as strings in sqlite extraction

df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')
df_reviews = df_reviews.dropna(subset=['rating','suffix'])

df_join = df_reviews.merge(df_books[['suffix','decade_start']], on='suffix', how='inner')

# distinct books rated per decade
# ensure distinct book based on suffix
books_per_decade = df_join[['decade_start','suffix']].drop_duplicates().groupby('decade_start').size().rename('distinct_books')
ratings_per_decade = df_join.groupby('decade_start')['rating'].mean().rename('avg_rating')

df_dec = pd.concat([books_per_decade, ratings_per_decade], axis=1).dropna().reset_index()

# filter decades with >=10 distinct books rated
eligible = df_dec[df_dec['distinct_books']>=10].copy()
if eligible.empty:
    result = None
else:
    top = eligible.sort_values(['avg_rating','distinct_books'], ascending=[False, False]).iloc[0]
    decade_label = f"{int(top['decade_start'])}s"
    result = decade_label

print('__RESULT__:')
print(json.dumps({'decade': result}))"""

env_args = {'var_call_7qHE6SSJopN8SMr6i6l6TN70': 'file_storage/call_7qHE6SSJopN8SMr6i6l6TN70.json', 'var_call_HHwhSTQhtew1uCFsbuAXSnrx': ['review'], 'var_call_dUIOTWeD0TQ8QlGAdFYOaq0V': 'file_storage/call_dUIOTWeD0TQ8QlGAdFYOaq0V.json'}

exec(code, env_args)
