code = """import json, pandas as pd, re

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

books = load_records(var_call_jZvKmGTWt2TUGPmTACI1h7CW)
reviews = load_records(var_call_eqMJuo6igZ2tVwHU7eZwffsx)

bdf = pd.DataFrame(books)
rdf = pd.DataFrame(reviews)

# parse year from details
pat_year = re.compile(r'\b(18|19|20)\d{2}\b')

def extract_year(s):
    if not isinstance(s, str):
        return None
    m = pat_year.search(s)
    if not m:
        return None
    y = int(m.group(0))
    # guardrails for plausible years
    if 1800 <= y <= 2026:
        return y
    return None

bdf['year'] = bdf['details'].map(extract_year)
bdf = bdf.dropna(subset=['year'])
bdf['year'] = bdf['year'].astype(int)
bdf['decade'] = (bdf['year']//10*10).astype(int)

# normalize ids to numeric suffix to join purchaseid_X with bookid_X
idnum_pat = re.compile(r'(\d+)')

def idnum(x):
    if not isinstance(x, str):
        return None
    m = idnum_pat.search(x)
    return int(m.group(1)) if m else None

bdf['idnum'] = bdf['book_id'].map(idnum)
rdf['idnum'] = rdf['purchase_id'].map(idnum)

# ratings to float
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
rdf = rdf.dropna(subset=['idnum','rating'])
bdf = bdf.dropna(subset=['idnum','decade'])

j = rdf.merge(bdf[['idnum','decade']], on='idnum', how='inner')

# count distinct books (idnum) rated per decade
agg = j.groupby('decade').agg(
    avg_rating=('rating','mean'),
    distinct_books=('idnum', pd.Series.nunique)
).reset_index()

eligible = agg[agg['distinct_books']>=10].copy()
if eligible.empty:
    out = {'error':'No decades with at least 10 distinct rated books after join.'}
else:
    best = eligible.sort_values(['avg_rating','distinct_books','decade'], ascending=[False,False,True]).iloc[0]
    decade_label = f"{int(best['decade'])}s"
    out = {
        'decade': decade_label,
        'avg_rating': float(best['avg_rating']),
        'distinct_books': int(best['distinct_books'])
    }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_jZvKmGTWt2TUGPmTACI1h7CW': 'file_storage/call_jZvKmGTWt2TUGPmTACI1h7CW.json', 'var_call_5PTqlZhumzQPD3wQUWcfaVIs': ['review'], 'var_call_eqMJuo6igZ2tVwHU7eZwffsx': 'file_storage/call_eqMJuo6igZ2tVwHU7eZwffsx.json'}

exec(code, env_args)
