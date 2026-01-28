code = """import json
with open(var_call_5u72CFr6RYHT6MZ5xk6hTNxq, 'r') as f:
    businesses = json.load(f)

# Gather keys and check if any doc has 'categories'
keys = set()
has_cat = 0
for d in businesses:
    keys.update(d.keys())
    if 'categories' in d and d['categories'] not in (None, '', 'None'):
        has_cat += 1

res = {'total_businesses': len(businesses), 'unique_keys': sorted(list(keys)), 'businesses_with_categories_count': has_cat}

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_call_33tJdYSKyPvqCFR6GBOv64VT': ['checkin', 'business'], 'var_call_0RUxKzrFEwaCMBIFUgyyM9Wi': ['review', 'tip', 'user'], 'var_call_5u72CFr6RYHT6MZ5xk6hTNxq': 'file_storage/call_5u72CFr6RYHT6MZ5xk6hTNxq.json', 'var_call_pPOFbEeTYqEA9ypm58fbm9eV': 'file_storage/call_pPOFbEeTYqEA9ypm58fbm9eV.json', 'var_call_6UZlN7mgqPlUyWPxluQtvec9': {'category': None, 'business_count': 0, 'average_rating': None}}

exec(code, env_args)
