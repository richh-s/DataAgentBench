code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

books = load_records(var_call_dL4fGbnsklIm6zzcPRBcb0xG)
reviews = load_records(var_call_3QxT7isfB5YG9kx4I1SnI74t)

# normalize key name
for r in books[:5]:
    pass

# parse year
pat = re.compile(r'\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[ ,.-]+\d{1,2}[, ]+((?:19|20)\d{2})\b|\b((?:19|20)\d{2})\b')

years=[]
for r in books:
    bid = r.get('book_id') or r.get('bookid') or r.get('id')
    if not bid:
        continue
    d = r.get('details') or ''
    m = pat.search(d)
    y=None
    if m:
        y = m.group(1) or m.group(2)
    if y:
        years.append({'book_id': bid, 'year': int(y)})

df_year = pd.DataFrame(years)

if df_year.empty:
    out={'decade': None}
else:
    df_year = df_year.drop_duplicates('book_id')
    df_rev = pd.DataFrame(reviews)
    df_rev['rating']=pd.to_numeric(df_rev['rating'], errors='coerce')
    df_rev=df_rev.dropna(subset=['rating','purchase_id'])

    sufpat=re.compile(r'(\d+)$')
    def suf(x):
        m=sufpat.search(str(x))
        return m.group(1) if m else None

    df_rev['sid']=df_rev['purchase_id'].map(suf)
    df_year['sid']=df_year['book_id'].map(suf)

    merged=df_rev.merge(df_year[['sid','year']], on='sid', how='inner')
    merged['decade']=(merged['year']//10)*10

    books_per_decade=merged.groupby('decade')['sid'].nunique()
    valid=books_per_decade[books_per_decade>=10].index
    agg=merged[merged['decade'].isin(valid)].groupby('decade')['rating'].mean().reset_index(name='avg_rating')

    if agg.empty:
        out={'decade': None}
    else:
        top=agg.sort_values('avg_rating', ascending=False).iloc[0]
        out={'decade': f"{int(top['decade'])}s"}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_dL4fGbnsklIm6zzcPRBcb0xG': 'file_storage/call_dL4fGbnsklIm6zzcPRBcb0xG.json', 'var_call_kHRelDeoCMhXdiVb8sJ8lc04': ['review'], 'var_call_3QxT7isfB5YG9kx4I1SnI74t': 'file_storage/call_3QxT7isfB5YG9kx4I1SnI74t.json'}

exec(code, env_args)
