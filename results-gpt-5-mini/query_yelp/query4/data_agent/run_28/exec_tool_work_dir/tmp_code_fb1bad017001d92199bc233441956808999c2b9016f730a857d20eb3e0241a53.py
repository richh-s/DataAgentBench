code = """import json
from collections import Counter
bs = json.load(open(var_call_ou0kDmsEGophro3skhOhh6QK, 'r'))
keys = set()
cat_types = Counter()
nonnull_count = 0
samples = []
for b in bs:
    for k in b.keys():
        keys.add(k)
    cats = b.get('categories', None)
    if cats is None:
        cat_types['None'] += 1
    else:
        cat_types[type(cats).__name__] += 1
        nonnull_count += 1
        if len(samples) < 10:
            samples.append({'business_id': b.get('business_id'), 'categories': cats})

out = {'total_businesses': len(bs), 'keys': sorted(list(keys)), 'categories_type_counts': dict(cat_types), 'categories_nonnull_count': nonnull_count, 'samples_with_categories': samples}
import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_Tr7v1meRsP00OcMGJDl6aa2F': 'file_storage/call_Tr7v1meRsP00OcMGJDl6aa2F.json', 'var_call_ou0kDmsEGophro3skhOhh6QK': 'file_storage/call_ou0kDmsEGophro3skhOhh6QK.json', 'var_call_svDbO7SbTNBU2g0AkksEFtMr': 'file_storage/call_svDbO7SbTNBU2g0AkksEFtMr.json', 'var_call_5Lnd0nzzRblE2HUGw1vK92Zc': {'category': None, 'business_count': 0, 'average_rating': None, 'num_reviews_used': 0}}

exec(code, env_args)
