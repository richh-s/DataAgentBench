code = """import json, pandas as pd, re

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

books = load_records(var_call_Qe2IwX2UoH8ew3EkKVFMDoTv)
reviews = load_records(var_call_eqMJuo6igZ2tVwHU7eZwffsx)

bdf = pd.DataFrame(books)
rdf = pd.DataFrame(reviews)

# extract year: prefer explicit 'released on <Month> <d>, <year>' etc; take first plausible year
pat_year = re.compile(r'\b(18|19|20)\d{2}\b')

def extract_year(s):
    if not isinstance(s, str):
        return None
    years = [int(y) for y in pat_year.findall(s)]
    # pat_year.findall with groups returns tuples; adjust
    return None

# correct extraction
pat_year2 = re.compile(r'\b((?:18|19|20)\d{2})\b')

def extract_year2(s):
    if not isinstance(s, str):
        return None
    ms = pat_year2.findall(s)
    if not ms:
        return None
    for ystr in ms:
        y = int(ystr)
        if 1800 <= y <= 2026:
            return y
    return None

bdf['year'] = bdf['details'].map(extract_year2)
bdf = bdf.dropna(subset=['year'])
bdf['year'] = bdf['year'].astype(int)
bdf['decade'] = (bdf['year']//10*10).astype(int)

idnum_pat = re.compile(r'(\d+)')

def idnum(x):
    if not isinstance(x, str):
        return None
    m = idnum_pat.search(x)
    return int(m.group(1)) if m else None

bdf['idnum'] = bdf['book_id'].map(idnum)
rdf['idnum'] = rdf['purchase_id'].map(idnum)

rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
rdf = rdf.dropna(subset=['idnum','rating'])

j = rdf.merge(bdf[['idnum','decade']], on='idnum', how='inner')

agg = j.groupby('decade').agg(avg_rating=('rating','mean'), distinct_books=('idnum', pd.Series.nunique)).reset_index()
eligible = agg[agg['distinct_books']>=10].copy()
if eligible.empty:
    out = {'error':'No decades with at least 10 distinct rated books after join.', 'decade_counts': agg.sort_values('distinct_books', ascending=False).head(20).to_dict(orient='records')}
else:
    best = eligible.sort_values(['avg_rating','distinct_books','decade'], ascending=[False,False,True]).iloc[0]
    out = {'decade': f"{int(best['decade'])}s", 'avg_rating': float(best['avg_rating']), 'distinct_books': int(best['distinct_books'])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_jZvKmGTWt2TUGPmTACI1h7CW': 'file_storage/call_jZvKmGTWt2TUGPmTACI1h7CW.json', 'var_call_5PTqlZhumzQPD3wQUWcfaVIs': ['review'], 'var_call_eqMJuo6igZ2tVwHU7eZwffsx': 'file_storage/call_eqMJuo6igZ2tVwHU7eZwffsx.json', 'var_call_3lw45hNpfhdEuEhxlU682fsZ': {'error': 'No decades with at least 10 distinct rated books after join.'}, 'var_call_Qe2IwX2UoH8ew3EkKVFMDoTv': 'file_storage/call_Qe2IwX2UoH8ew3EkKVFMDoTv.json'}

exec(code, env_args)
