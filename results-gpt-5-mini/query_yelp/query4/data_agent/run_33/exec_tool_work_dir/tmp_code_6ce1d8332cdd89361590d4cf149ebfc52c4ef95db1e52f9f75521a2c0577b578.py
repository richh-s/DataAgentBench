code = """import json
import pandas as pd

with open(var_call_By0YsQSKO0TUH7HYGOuh2IE3, 'r') as f:
    businesses = json.load(f)
with open(var_call_TlPasEwRwrpoipslO3NtzTX9, 'r') as f:
    reviews = json.load(f)

b = pd.DataFrame(businesses)

# counts
total = len(b)
attr_nonnull = b['attributes'].notna().sum() if 'attributes' in b.columns else 0

# detect accepts credit

def accepts_cc(attr):
    if attr is None:
        return False
    if isinstance(attr, dict):
        v = attr.get('BusinessAcceptsCreditCards')
        if v is None:
            return False
        return 'true' in str(v).lower()
    s = str(attr).lower()
    return ('businessacceptscreditcards' in s and 'true' in s)

if 'attributes' not in b.columns:
    b['attributes'] = None
b['accepts_cc'] = b['attributes'].apply(accepts_cc)
accepts_count = int(b['accepts_cc'].sum())

# show first 10 businesses that accept cc with their attributes and description
samples = b[b['accepts_cc']==True].head(10)[['business_id','name','attributes','description']].to_dict(orient='records')

res = {'total_businesses': int(total), 'attributes_nonnull': int(attr_nonnull), 'accepts_cc_count': accepts_count, 'sample_accepts': samples}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_zYWWfxdtpjIy5owlOM4SaGDn': ['business', 'checkin'], 'var_call_mHA3vgr16eyfCZYaS9qPg3uP': ['review', 'tip', 'user'], 'var_call_By0YsQSKO0TUH7HYGOuh2IE3': 'file_storage/call_By0YsQSKO0TUH7HYGOuh2IE3.json', 'var_call_TlPasEwRwrpoipslO3NtzTX9': 'file_storage/call_TlPasEwRwrpoipslO3NtzTX9.json', 'var_call_y3E5KsRHzfEDIvVCCDQoNDKU': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_4EyBBhMx0IX87GBMEIVF9q5X': 'file_storage/call_4EyBBhMx0IX87GBMEIVF9q5X.json', 'var_call_5gb3J7A0uHjJTrUuB8IRGuPQ': {'category': None, 'business_count': 0, 'average_rating': None}}

exec(code, env_args)
