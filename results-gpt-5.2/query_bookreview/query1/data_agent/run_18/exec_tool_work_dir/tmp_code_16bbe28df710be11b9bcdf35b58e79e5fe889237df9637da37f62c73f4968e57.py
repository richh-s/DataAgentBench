code = """import json, re, pandas as pd

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

reviews = load_records(var_call_ybhbolEXEUIcmJ7M3VvaKNoc)
books = load_records(var_call_v0H5T3pdwiWDnaoJcgKZFfEl)

df_r = pd.DataFrame(reviews)
df_b = pd.DataFrame(books)

# parse numeric id
id_re = re.compile(r'(\d+)')
df_r['num'] = df_r['purchase_id'].astype(str).str.extract(id_re)[0].astype('Int64')
df_b['num'] = df_b['book_id'].astype(str).str.extract(id_re)[0].astype('Int64')

# parse rating
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
df_r = df_r.dropna(subset=['num','rating'])

# parse publication year from details
year_pat = re.compile(r'\b(18\d{2}|19\d{2}|20\d{2})\b')

def extract_year(s):
    if not isinstance(s, str):
        return None
    m = year_pat.search(s)
    if not m:
        return None
    y = int(m.group(1))
    # guard rails
    if y < 1800 or y > 2026:
        return None
    return y

df_b['year'] = df_b['details'].apply(extract_year)
df_b = df_b.dropna(subset=['num','year'])
df_b['year'] = df_b['year'].astype(int)
df_b['decade_start'] = (df_b['year']//10)*10

# join
merged = df_r.merge(df_b[['num','decade_start']], on='num', how='inner')

# distinct books rated per decade
books_per_decade = merged.groupby('decade_start')['num'].nunique().rename('distinct_books')
ratings_per_decade = merged.groupby('decade_start')['rating'].mean().rename('avg_rating')
summary = pd.concat([books_per_decade, ratings_per_decade], axis=1).reset_index()
summary = summary[summary['distinct_books']>=10].copy()

if summary.empty:
    ans = None
else:
    best = summary.sort_values(['avg_rating','distinct_books','decade_start'], ascending=[False, False, True]).iloc[0]
    ans = f"{int(best['decade_start'])}s"

print('__RESULT__:')
print(json.dumps({'decade': ans}))"""

env_args = {'var_call_v0H5T3pdwiWDnaoJcgKZFfEl': 'file_storage/call_v0H5T3pdwiWDnaoJcgKZFfEl.json', 'var_call_zaWX5zm4nIuGOPclDXDOz35u': ['review'], 'var_call_ybhbolEXEUIcmJ7M3VvaKNoc': 'file_storage/call_ybhbolEXEUIcmJ7M3VvaKNoc.json'}

exec(code, env_args)
