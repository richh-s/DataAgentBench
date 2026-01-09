code = """import json, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

books = load_records(var_call_Qe2IwX2UoH8ew3EkKVFMDoTv)
bdf = pd.DataFrame(books)

sample = bdf['details'].dropna().head(5).tolist()

print('__RESULT__:')
print(json.dumps(sample))"""

env_args = {'var_call_jZvKmGTWt2TUGPmTACI1h7CW': 'file_storage/call_jZvKmGTWt2TUGPmTACI1h7CW.json', 'var_call_5PTqlZhumzQPD3wQUWcfaVIs': ['review'], 'var_call_eqMJuo6igZ2tVwHU7eZwffsx': 'file_storage/call_eqMJuo6igZ2tVwHU7eZwffsx.json', 'var_call_3lw45hNpfhdEuEhxlU682fsZ': {'error': 'No decades with at least 10 distinct rated books after join.'}, 'var_call_Qe2IwX2UoH8ew3EkKVFMDoTv': 'file_storage/call_Qe2IwX2UoH8ew3EkKVFMDoTv.json', 'var_call_YKjsebaxG1CCTUT4yiSt3MIX': {'error': 'No decades with at least 10 distinct rated books after join.', 'decade_counts': []}, 'var_call_vBIJ8abtXSnrmc0y0RrXgb4L': [{'purchase_id': 'purchaseid_196', 'n_reviews': '194'}, {'purchase_id': 'purchaseid_8', 'n_reviews': '190'}, {'purchase_id': 'purchaseid_3', 'n_reviews': '146'}, {'purchase_id': 'purchaseid_178', 'n_reviews': '118'}, {'purchase_id': 'purchaseid_186', 'n_reviews': '80'}, {'purchase_id': 'purchaseid_20', 'n_reviews': '42'}, {'purchase_id': 'purchaseid_10', 'n_reviews': '40'}, {'purchase_id': 'purchaseid_145', 'n_reviews': '36'}, {'purchase_id': 'purchaseid_190', 'n_reviews': '34'}, {'purchase_id': 'purchaseid_154', 'n_reviews': '29'}, {'purchase_id': 'purchaseid_148', 'n_reviews': '29'}, {'purchase_id': 'purchaseid_48', 'n_reviews': '27'}, {'purchase_id': 'purchaseid_5', 'n_reviews': '25'}, {'purchase_id': 'purchaseid_158', 'n_reviews': '24'}, {'purchase_id': 'purchaseid_95', 'n_reviews': '23'}, {'purchase_id': 'purchaseid_62', 'n_reviews': '22'}, {'purchase_id': 'purchaseid_165', 'n_reviews': '22'}, {'purchase_id': 'purchaseid_99', 'n_reviews': '20'}, {'purchase_id': 'purchaseid_72', 'n_reviews': '19'}, {'purchase_id': 'purchaseid_89', 'n_reviews': '18'}], 'var_call_2jVPchpE5or3GgyHqGyuic6M': {'books_total': 200, 'books_with_year': 0, 'reviews_total': 1833, 'reviews_with_idnum': 1833, 'books_idnum_minmax': None, 'reviews_idnum_minmax': [1, 200], 'overlap_idnums': 0}}

exec(code, env_args)
