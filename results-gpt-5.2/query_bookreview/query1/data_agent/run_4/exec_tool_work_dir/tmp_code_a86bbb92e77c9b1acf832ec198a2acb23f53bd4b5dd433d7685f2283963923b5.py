code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

books = load_records(var_call_dL4fGbnsklIm6zzcPRBcb0xG)
reviews = load_records(var_call_3QxT7isfB5YG9kx4I1SnI74t)

# parse publication year from details
pat = re.compile(r'\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[ ,.-]+\d{1,2}[, ]+((?:19|20)\d{2})\b|\b((?:19|20)\d{2})\b')

years = []
for r in books:
    d = r.get('details') or ''
    m = pat.search(d)
    y = None
    if m:
        y = m.group(1) or m.group(2)
    if y and r.get('book_id'):
        years.append({'book_id': r['book_id'], 'year': int(y)})

df_year = pd.DataFrame(years).drop_duplicates('book_id')

df_rev = pd.DataFrame(reviews)
df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')
df_rev = df_rev.dropna(subset=['rating','purchase_id'])

# fuzzy join: purchaseid_x <-> bookid_x
# create a normalized key numeric suffix
suffix_pat = re.compile(r'(\d+)$')

def suffix(s):
    if pd.isna(s):
        return None
    m = suffix_pat.search(str(s))
    return m.group(1) if m else None

df_rev['sid'] = df_rev['purchase_id'].map(suffix)
df_year['sid'] = df_year['book_id'].map(suffix)

merged = df_rev.merge(df_year[['sid','year']], on='sid', how='inner')
merged['decade'] = (merged['year']//10)*10

books_per_decade = merged.groupby('decade')['sid'].nunique()
valid = books_per_decade[books_per_decade>=10].index
agg = merged[merged['decade'].isin(valid)].groupby('decade').agg(
    avg_rating=('rating','mean'),
    distinct_books=('sid','nunique')
).reset_index()

if agg.empty:
    out = {'decade': None}
else:
    top = agg.sort_values(['avg_rating','distinct_books','decade'], ascending=[False,False,True]).iloc[0]
    out = {'decade': f"{int(top['decade'])}s"}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_dL4fGbnsklIm6zzcPRBcb0xG': 'file_storage/call_dL4fGbnsklIm6zzcPRBcb0xG.json', 'var_call_kHRelDeoCMhXdiVb8sJ8lc04': ['review'], 'var_call_3QxT7isfB5YG9kx4I1SnI74t': 'file_storage/call_3QxT7isfB5YG9kx4I1SnI74t.json'}

exec(code, env_args)
