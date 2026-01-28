code = """import json, re, pandas as pd

# Load full datasets
books_path = var_call_MDPfIXbMwAp09wW0IREDePEE
reviews_path = var_call_ZinQCbJBVRFdBSYmvUy9gOmT

with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

bdf = pd.DataFrame(books)
rdf = pd.DataFrame(reviews)

# normalize ids for fuzzy-ish join: compare numeric suffix
bdf['id_num'] = bdf['book_id'].astype(str).str.extract(r'(\d+)$')[0]
rdf['id_num'] = rdf['purchase_id'].astype(str).str.extract(r'(\d+)$')[0]

# Extract publication year from details
year_re = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_year(s):
    if not isinstance(s, str):
        return None
    years = [int(y) for y in year_re.findall(s)]
    if not years:
        return None
    # choose earliest plausible year as publication year
    return min(years)

bdf['pub_year'] = bdf['details'].map(extract_year)

# Join reviews to books via id_num
j = rdf.merge(bdf[['id_num','pub_year']], on='id_num', how='inner')

# numeric ratings
j['rating'] = pd.to_numeric(j['rating'], errors='coerce')
j = j.dropna(subset=['rating','pub_year'])
j['pub_year'] = j['pub_year'].astype(int)

# decade label
j['decade_start'] = (j['pub_year']//10)*10
j['decade'] = j['decade_start'].astype(str) + 's'

# only decades with at least 10 distinct books that have been rated
# distinct books identified by id_num within that decade
books_per_decade = j.groupby('decade')['id_num'].nunique().rename('distinct_books')
avg_rating = j.groupby('decade')['rating'].mean().rename('avg_rating')
summary = pd.concat([books_per_decade, avg_rating], axis=1).reset_index()
eligible = summary[summary['distinct_books']>=10].copy()

if eligible.empty:
    result = {"decade": None, "avg_rating": None, "distinct_books": 0}
else:
    top = eligible.sort_values(['avg_rating','distinct_books','decade'], ascending=[False, False, True]).iloc[0]
    result = {"decade": str(top['decade']), "avg_rating": float(top['avg_rating']), "distinct_books": int(top['distinct_books'])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_MDPfIXbMwAp09wW0IREDePEE': 'file_storage/call_MDPfIXbMwAp09wW0IREDePEE.json', 'var_call_NQv5G17XlywOeyESiFlu0i2S': ['review'], 'var_call_ZinQCbJBVRFdBSYmvUy9gOmT': 'file_storage/call_ZinQCbJBVRFdBSYmvUy9gOmT.json'}

exec(code, env_args)
