code = """import json, re
path = var_call_HRbzImfiTlPYDcmxv9Hcahb4
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# show total
total = len(records)

# collect sample wifi values and descriptions
wifi_vals = {}
samples = []
for i, r in enumerate(records[:200]):
    attrs = r.get('attributes') or {}
    wifi = attrs.get('WiFi') if isinstance(attrs, dict) else None
    wifi_vals[str(wifi)] = wifi_vals.get(str(wifi), 0) + 1
    if i < 20:
        samples.append({'business_id': r.get('business_id'), 'WiFi': wifi, 'description': r.get('description')})

out = {'total': total, 'wifi_vals_count': len(wifi_vals), 'wifi_vals_examples': list(wifi_vals.items())[:20], 'samples': samples}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FcU8ULKgLTvgq2xHt8RuPo4k': ['checkin', 'business'], 'var_call_HRbzImfiTlPYDcmxv9Hcahb4': 'file_storage/call_HRbzImfiTlPYDcmxv9Hcahb4.json', 'var_call_TYPbttHMnXwKVSgULW5ys9HS': {'business_refs': [], 'biz_state_map': {}, 'state_counts': {}}}

exec(code, env_args)
