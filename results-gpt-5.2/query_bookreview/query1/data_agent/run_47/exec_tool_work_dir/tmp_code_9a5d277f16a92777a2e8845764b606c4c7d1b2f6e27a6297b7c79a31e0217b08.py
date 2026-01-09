code = """import json, re
import pandas as pd

def load(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

reviews = load(var_call_8F5Ge0elQjC7oE5HYbGtoHSZ)
books = load(var_call_NY25wsOgXQctCIBaWCK8aZzR)

rdf = pd.DataFrame(reviews)
bdf = pd.DataFrame(books)

rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
rdf = rdf.dropna(subset=['purchase_id','rating'])

# map purchaseid_### -> bookid_###
rdf['book_id'] = rdf['purchase_id'].astype(str).str.replace('purchaseid_','bookid_', regex=False)

# extract year from details
pat = re.compile(r'\b(18\d{2}|19\d{2}|20\d{2})\b')

def get_year(s):
    if not isinstance(s, str):
        return None
    m = pat.search(s)
    if not m:
        return None
    return int(m.group(1))

bdf['year'] = bdf['details'].apply(get_year)
bdf = bdf.dropna(subset=['book_id','year'])
bdf['year'] = bdf['year'].astype(int)

# join
j = rdf.merge(bdf[['book_id','year']], on='book_id', how='inner')

# decades with at least 10 distinct books rated
j['decade_start'] = (j['year']//10)*10
j['decade'] = j['decade_start'].astype(int).astype(str) + 's'

books_per_decade = j.groupby('decade')['book_id'].nunique()
eligible = books_per_decade[books_per_decade >= 10].index
j2 = j[j['decade'].isin(eligible)].copy()

avg_by_decade = j2.groupby('decade')['rating'].mean().sort_values(ascending=False)
if len(avg_by_decade)==0:
    ans = None
else:
    ans = avg_by_decade.index[0]

print('__RESULT__:')
print(json.dumps({'decade': ans}))"""

env_args = {'var_call_NY25wsOgXQctCIBaWCK8aZzR': 'file_storage/call_NY25wsOgXQctCIBaWCK8aZzR.json', 'var_call_HIeMrJRoX6TDc7DG83da4KwQ': ['review'], 'var_call_8F5Ge0elQjC7oE5HYbGtoHSZ': 'file_storage/call_8F5Ge0elQjC7oE5HYbGtoHSZ.json'}

exec(code, env_args)
