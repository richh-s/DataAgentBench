code = """import json, re
with open(var_call_cKAUvs32jTulvBxlVKm3UG9A, 'r') as f:
    businesses = json.load(f)

total = len(businesses)
with_attrs = sum(1 for b in businesses if b.get('attributes'))

wifi_key_businesses = []
for b in businesses:
    attrs = b.get('attributes')
    if not isinstance(attrs, dict):
        continue
    for k in attrs.keys():
        if k and ('wifi' in str(k).lower() or 'wi-fi' in str(k).lower()):
            wifi_key_businesses.append({'business_id': b.get('business_id'), 'name': b.get('name'), 'wifi_key': k, 'wifi_val': attrs.get(k), 'description': b.get('description')})
            break

sample = wifi_key_businesses[:20]
res = {'total_businesses': total, 'with_attributes': with_attrs, 'wifi_key_count': len(wifi_key_businesses), 'samples': sample}
import json
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_cKAUvs32jTulvBxlVKm3UG9A': 'file_storage/call_cKAUvs32jTulvBxlVKm3UG9A.json', 'var_call_HqfVjLmSpm2LUwUZsWZG8Qg2': 'file_storage/call_HqfVjLmSpm2LUwUZsWZG8Qg2.json', 'var_call_YQstDHrjxqbZGF1nEQksbPZw': {'error': 'No results'}}

exec(code, env_args)
