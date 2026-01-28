code = """import json
with open(var_call_ZBHW94XWp3U3AoDfUe6ZQ30P, 'r') as f:
    businesses = json.load(f)

# collect keys
all_keys = set()
for b in businesses[:50]:
    all_keys.update(b.keys())

# sample descriptions and attributes
samples = []
for b in businesses[:50]:
    samples.append({'business_id': b.get('business_id'), 'name': b.get('name'), 'keys': list(b.keys()), 'categories': b.get('categories', None), 'description': b.get('description', None), 'attributes': b.get('attributes', None)})

import json
print("__RESULT__:")
print(json.dumps({'all_keys': sorted(list(all_keys)), 'samples': samples[:10]}))"""

env_args = {'var_call_57VwjpZjKapp8oKO6AmPqfMm': ['checkin', 'business'], 'var_call_CMobM1WcPKVp7Qb5DZI2SJHs': ['review', 'tip', 'user'], 'var_call_ZBHW94XWp3U3AoDfUe6ZQ30P': 'file_storage/call_ZBHW94XWp3U3AoDfUe6ZQ30P.json', 'var_call_sRAONQyMLlvwgo57IQUKQv8l': 'file_storage/call_sRAONQyMLlvwgo57IQUKQv8l.json', 'var_call_KuR1nE5ViTXo2PfbImwlsyZW': {'category': None, 'num_businesses': 0, 'avg_rating': None}}

exec(code, env_args)
