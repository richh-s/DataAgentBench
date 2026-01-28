code = """import json, re, pandas as pd

def load(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

books = load(var_call_UIDMUIlErSd8uU0NHsw9kruj)
reviews = load(var_call_FpLxJMyPVifznyyFf0he7sNP)

df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')
df_reviews = df_reviews.dropna(subset=['purchase_id','rating'])

# fuzzy join: purchaseid_123 -> bookid_123
extract_num = lambda s: (re.search(r'(\d+)', str(s)).group(1) if re.search(r'(\d+)', str(s)) else None)
df_reviews['id_num'] = df_reviews['purchase_id'].map(extract_num)
df_books['id_num'] = df_books['book_id'].map(extract_num)

def extract_year(details):
    if details is None:
        return None
    s = str(details)
    # look for full date patterns like 'January 1, 2004'
    m = re.search(r'\b(1[6-9]\d{2}|20\d{2})\b', s)
    if m:
        return int(m.group(1))
    return None

df_books['pub_year'] = df_books['details'].map(extract_year)

# join
merged = df_reviews.merge(df_books[['id_num','pub_year']], on='id_num', how='inner')
merged = merged.dropna(subset=['pub_year'])
merged['pub_year'] = merged['pub_year'].astype(int)
merged['decade_start'] = (merged['pub_year']//10)*10
merged['decade'] = merged['decade_start'].astype(str) + 's'

# require at least 10 distinct books with at least one rating in decade
books_per_decade = merged.groupby('decade')['id_num'].nunique().rename('distinct_books')
avg_rating = merged.groupby('decade')['rating'].mean().rename('avg_rating')
summary = pd.concat([books_per_decade, avg_rating], axis=1).reset_index()
summary = summary[summary['distinct_books']>=10]
if summary.empty:
    best = None
else:
    best_row = summary.sort_values(['avg_rating','distinct_books'], ascending=[False, False]).iloc[0]
    best = str(best_row['decade'])

print('__RESULT__:')
print(json.dumps({'best_decade': best}))"""

env_args = {'var_call_UIDMUIlErSd8uU0NHsw9kruj': 'file_storage/call_UIDMUIlErSd8uU0NHsw9kruj.json', 'var_call_JiXeYsnQHCmeUGA9F7MBfTck': ['review'], 'var_call_FpLxJMyPVifznyyFf0he7sNP': 'file_storage/call_FpLxJMyPVifznyyFf0he7sNP.json'}

exec(code, env_args)
