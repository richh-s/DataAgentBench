code = """import json, re, pandas as pd

def load_records(x):
    if isinstance(x, str):
        with open(x, 'r') as f:
            return json.load(f)
    return x

books = load_records(var_call_Wx5tY3gII2dti3PGOjN6WE3x)
reviews = load_records(var_call_NgkpTFmYD1fKkgAUtly1Rhn5)

bdf = pd.DataFrame(books)
rdf = pd.DataFrame(reviews)

# extract 4-digit year from details
pat = re.compile(r'\b(18\d{2}|19\d{2}|20\d{2})\b')

def extract_year(s):
    if not isinstance(s, str):
        return None
    m = pat.search(s)
    if not m:
        return None
    y = int(m.group(1))
    if 1800 <= y <= 2026:
        return y
    return None

bdf['year'] = bdf['details'].map(extract_year)
# decade label
bdf['decade_start'] = (bdf['year']//10)*10
bdf['decade'] = bdf['decade_start'].apply(lambda x: f"{int(x)}s" if pd.notnull(x) else None)

# map purchaseid_N -> bookid_N (fuzzy join via numeric suffix)

def suffix_num(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'(\d+)$', s)
    return int(m.group(1)) if m else None

rdf['sid'] = rdf['purchase_id'].map(suffix_num)
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')

bdf['sid'] = bdf['book_id'].map(suffix_num)

jdf = pd.merge(rdf[['sid','rating']], bdf[['sid','decade']], on='sid', how='inner')

# consider only rated reviews
jdf = jdf.dropna(subset=['rating','decade'])

# require decade has at least 10 distinct books that have been rated
# distinct books = distinct sid within decade present in merged ratings
books_per_decade = jdf.groupby('decade')['sid'].nunique().rename('distinct_books')
avg_rating = jdf.groupby('decade')['rating'].mean().rename('avg_rating')
res = pd.concat([books_per_decade, avg_rating], axis=1).reset_index()
res = res[res['distinct_books'] >= 10]
res = res.sort_values(['avg_rating','distinct_books','decade'], ascending=[False, False, True])

top = None
if len(res):
    top = res.iloc[0].to_dict()

out = {'top_decade': top['decade'] if top else None, 'avg_rating': float(top['avg_rating']) if top else None, 'distinct_books': int(top['distinct_books']) if top else None}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Wx5tY3gII2dti3PGOjN6WE3x': 'file_storage/call_Wx5tY3gII2dti3PGOjN6WE3x.json', 'var_call_YiMHOcaQawFPkcwkI8o1qzKJ': ['review'], 'var_call_NgkpTFmYD1fKkgAUtly1Rhn5': 'file_storage/call_NgkpTFmYD1fKkgAUtly1Rhn5.json'}

exec(code, env_args)
