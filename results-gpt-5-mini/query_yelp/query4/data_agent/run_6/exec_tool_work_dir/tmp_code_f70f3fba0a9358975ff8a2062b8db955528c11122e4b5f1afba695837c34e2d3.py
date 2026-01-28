code = """import json
import collections
with open(var_call_5u72CFr6RYHT6MZ5xk6hTNxq, 'r') as f:
    businesses = json.load(f)

attr_keys = collections.Counter()
attr_values_sample = {}
for d in businesses:
    a = d.get('attributes')
    if isinstance(a, dict):
        for k,v in a.items():
            attr_keys[k] += 1
            if k not in attr_values_sample and v is not None:
                attr_values_sample[k] = v
    else:
        # if string, try to find key names via regex-like splitting
        s = str(a)
        # naive splitting on commas for samples
        parts = [p.strip() for p in s.split(',') if ':' in p or '=' in p]
        for p in parts[:5]:
            # just note sample
            attr_keys[p] += 1

res = {'attr_key_counts': attr_keys.most_common(), 'attr_values_sample': attr_values_sample}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_33tJdYSKyPvqCFR6GBOv64VT': ['checkin', 'business'], 'var_call_0RUxKzrFEwaCMBIFUgyyM9Wi': ['review', 'tip', 'user'], 'var_call_5u72CFr6RYHT6MZ5xk6hTNxq': 'file_storage/call_5u72CFr6RYHT6MZ5xk6hTNxq.json', 'var_call_pPOFbEeTYqEA9ypm58fbm9eV': 'file_storage/call_pPOFbEeTYqEA9ypm58fbm9eV.json', 'var_call_6UZlN7mgqPlUyWPxluQtvec9': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_VDQDNIHu2J1InFMvRt5klaj8': {'total_businesses': 100, 'unique_keys': ['_id', 'attributes', 'business_id', 'is_open', 'name', 'review_count'], 'businesses_with_categories_count': 0}}

exec(code, env_args)
