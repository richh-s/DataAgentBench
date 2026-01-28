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

pat_year = re.compile(r'\b((?:18|19|20)\d{2})\b')

def extract_year(s):
    if not isinstance(s, str):
        return None
    ms = pat_year.findall(s)
    if not ms:
        return None
    for ystr in ms:
        y = int(ystr)
        if 1800 <= y <= 2026:
            return y
    return None

bdf['year'] = bdf['details'].map(extract_year)
bdf = bdf.dropna(subset=['year'])
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
bdf = bdf.dropna(subset=['idnum','decade'])

# debug counts
out = {
  'books_total': int(len(pd.DataFrame(books))),
  'books_with_year': int(len(bdf)),
  'reviews_total': int(len(pd.DataFrame(reviews))),
  'reviews_with_idnum': int(rdf['idnum'].notna().sum()),
  'books_idnum_minmax': [int(bdf['idnum'].min()), int(bdf['idnum'].max())] if len(bdf)>0 else None,
  'reviews_idnum_minmax': [int(rdf['idnum'].min()), int(rdf['idnum'].max())] if len(rdf)>0 else None,
  'overlap_idnums': int(len(set(bdf['idnum']).intersection(set(rdf['idnum'])))),
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_jZvKmGTWt2TUGPmTACI1h7CW': 'file_storage/call_jZvKmGTWt2TUGPmTACI1h7CW.json', 'var_call_5PTqlZhumzQPD3wQUWcfaVIs': ['review'], 'var_call_eqMJuo6igZ2tVwHU7eZwffsx': 'file_storage/call_eqMJuo6igZ2tVwHU7eZwffsx.json', 'var_call_3lw45hNpfhdEuEhxlU682fsZ': {'error': 'No decades with at least 10 distinct rated books after join.'}, 'var_call_Qe2IwX2UoH8ew3EkKVFMDoTv': 'file_storage/call_Qe2IwX2UoH8ew3EkKVFMDoTv.json', 'var_call_YKjsebaxG1CCTUT4yiSt3MIX': {'error': 'No decades with at least 10 distinct rated books after join.', 'decade_counts': []}, 'var_call_vBIJ8abtXSnrmc0y0RrXgb4L': [{'purchase_id': 'purchaseid_196', 'n_reviews': '194'}, {'purchase_id': 'purchaseid_8', 'n_reviews': '190'}, {'purchase_id': 'purchaseid_3', 'n_reviews': '146'}, {'purchase_id': 'purchaseid_178', 'n_reviews': '118'}, {'purchase_id': 'purchaseid_186', 'n_reviews': '80'}, {'purchase_id': 'purchaseid_20', 'n_reviews': '42'}, {'purchase_id': 'purchaseid_10', 'n_reviews': '40'}, {'purchase_id': 'purchaseid_145', 'n_reviews': '36'}, {'purchase_id': 'purchaseid_190', 'n_reviews': '34'}, {'purchase_id': 'purchaseid_154', 'n_reviews': '29'}, {'purchase_id': 'purchaseid_148', 'n_reviews': '29'}, {'purchase_id': 'purchaseid_48', 'n_reviews': '27'}, {'purchase_id': 'purchaseid_5', 'n_reviews': '25'}, {'purchase_id': 'purchaseid_158', 'n_reviews': '24'}, {'purchase_id': 'purchaseid_95', 'n_reviews': '23'}, {'purchase_id': 'purchaseid_62', 'n_reviews': '22'}, {'purchase_id': 'purchaseid_165', 'n_reviews': '22'}, {'purchase_id': 'purchaseid_99', 'n_reviews': '20'}, {'purchase_id': 'purchaseid_72', 'n_reviews': '19'}, {'purchase_id': 'purchaseid_89', 'n_reviews': '18'}]}

exec(code, env_args)
