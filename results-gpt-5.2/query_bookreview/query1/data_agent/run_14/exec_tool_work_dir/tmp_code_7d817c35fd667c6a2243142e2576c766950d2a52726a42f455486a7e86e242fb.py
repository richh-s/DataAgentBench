code = """import json, re, pandas as pd

# Load books details
books_src = var_call_bXJU9ys4bWx8Lr96fFBL8xY2
if isinstance(books_src, str):
    with open(books_src, 'r', encoding='utf-8') as f:
        books = json.load(f)
else:
    books = books_src

# Load reviews
rev_src = var_call_onlOrNbRZnbyW4tptUcsleot
if isinstance(rev_src, str):
    with open(rev_src, 'r', encoding='utf-8') as f:
        reviews = json.load(f)
else:
    reviews = rev_src

bdf = pd.DataFrame(books)
rdf = pd.DataFrame(reviews)

# Parse publication year from details text
def extract_year(s):
    if s is None:
        return None
    s = str(s)
    # Prefer explicit published/released/on patterns
    m = re.search(r'\b(?:published|release(?:d)?|released|publication|first edition.*?released)\b[^\d]{0,50}(\b(18|19|20)\d{2}\b)', s, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    # Any year in plausible range
    years = [int(y) for y in re.findall(r'\b(18\d{2}|19\d{2}|20\d{2})\b', s)]
    if not years:
        return None
    # choose earliest as publication year often earliest mentioned
    return min(years)

bdf['pub_year'] = bdf['details'].apply(extract_year)

# Coerce ids: purchaseid_X vs bookid_X -> join by numeric suffix
bdf['id_num'] = bdf['book_id'].astype(str).str.extract(r'(\d+)')[0]
rdf['id_num'] = rdf['purchase_id'].astype(str).str.extract(r'(\d+)')[0]

# ratings to float
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')

j = rdf.merge(bdf[['id_num','book_id','pub_year']], on='id_num', how='inner')
j = j.dropna(subset=['rating','pub_year'])

# decades
def decade_label(y):
    y=int(y)
    d=(y//10)*10
    return f"{d}s"

j['decade'] = j['pub_year'].astype(int).apply(decade_label)

# Only decades with >=10 distinct books rated
agg = j.groupby('decade').agg(avg_rating=('rating','mean'), distinct_books=('book_id','nunique'))
agg = agg[agg['distinct_books']>=10].sort_values(['avg_rating','distinct_books'], ascending=[False,False])

if agg.shape[0]==0:
    out = None
else:
    out = agg.reset_index().iloc[0].to_dict()

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_bXJU9ys4bWx8Lr96fFBL8xY2': 'file_storage/call_bXJU9ys4bWx8Lr96fFBL8xY2.json', 'var_call_SZjg6uraXVUAdpb7nBeBUXLR': ['review'], 'var_call_onlOrNbRZnbyW4tptUcsleot': 'file_storage/call_onlOrNbRZnbyW4tptUcsleot.json'}

exec(code, env_args)
