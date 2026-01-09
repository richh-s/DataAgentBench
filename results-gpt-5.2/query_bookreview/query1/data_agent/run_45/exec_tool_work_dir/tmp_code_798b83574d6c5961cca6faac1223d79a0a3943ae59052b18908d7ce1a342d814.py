code = """import json, re, pandas as pd

def load_var(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

books = load_var(var_call_w9kephAs9lV6vtl5EjRI2Pb4)
reviews = load_var(var_call_gWsx4NUArdS75jsawRa8jxJ6)

bdf = pd.DataFrame(books)
rdf = pd.DataFrame(reviews)

# normalize ids to join (purchaseid_x vs bookid_x)
pat = re.compile(r'(\d+)')

def norm_id(x):
    if x is None:
        return None
    m = pat.search(str(x))
    return m.group(1) if m else None

bdf['nid'] = bdf['book_id'].map(norm_id)
rdf['nid'] = rdf['purchase_id'].map(norm_id)

# parse year from details text
# try patterns like 'on May 8, 2012', 'on January 1, 2004', 'in January 2004', 'September 1, 1987'
year_re = re.compile(r'\b(17\d{2}|18\d{2}|19\d{2}|20\d{2})\b')

def extract_year(s):
    if not isinstance(s, str):
        return None
    yrs = year_re.findall(s)
    if not yrs:
        return None
    # choose last year mentioned (often publication date at end)
    return int(yrs[-1])

bdf['pub_year'] = bdf['details'].map(extract_year)

mdf = pd.merge(rdf, bdf[['nid','pub_year']], on='nid', how='inner')
mdf['rating'] = pd.to_numeric(mdf['rating'], errors='coerce')
mdf = mdf.dropna(subset=['rating','pub_year'])
mdf['decade_start'] = (mdf['pub_year']//10)*10

# ensure decades with at least 10 distinct books that have been rated
# distinct books based on nid within decade
books_per_decade = mdf.groupby('decade_start')['nid'].nunique()
eligible_decades = books_per_decade[books_per_decade >= 10].index.tolist()

res = None
if eligible_decades:
    avg_rating = mdf[mdf['decade_start'].isin(eligible_decades)].groupby('decade_start')['rating'].mean()
    best_decade = int(avg_rating.idxmax())
    res = f"{best_decade}s"
else:
    res = None

print('__RESULT__:')
print(json.dumps({'decade': res}))"""

env_args = {'var_call_FZd3fcjGSaS3KNNmK5mbQl5M': ['review'], 'var_call_jHsEN6E2YuryUOpBR1ATOvUu': ['books_info'], 'var_call_w9kephAs9lV6vtl5EjRI2Pb4': 'file_storage/call_w9kephAs9lV6vtl5EjRI2Pb4.json', 'var_call_gWsx4NUArdS75jsawRa8jxJ6': 'file_storage/call_gWsx4NUArdS75jsawRa8jxJ6.json'}

exec(code, env_args)
