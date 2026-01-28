code = """import json, re
p = var_call_dTdMzELB4RK2SW9tG9NA5SiF
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)
# show first 30 entries with business_id, attributes.WiFi, description
out = []
for rec in data[:30]:
    wifi = None
    attrs = rec.get('attributes')
    if isinstance(attrs, dict):
        wifi = attrs.get('WiFi')
    out.append({'business_id': rec.get('business_id'), 'WiFi': wifi, 'description': rec.get('description')})

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ZESpVOW8rLKXaIlEar1igsb3': ['business', 'checkin'], 'var_call_BkALsWIa0Flqm7nUNmc0QjvX': ['review', 'tip', 'user'], 'var_call_M0ZKJDSbejRHfgoAjAgTh3bp': 'file_storage/call_M0ZKJDSbejRHfgoAjAgTh3bp.json', 'var_call_dTdMzELB4RK2SW9tG9NA5SiF': 'file_storage/call_dTdMzELB4RK2SW9tG9NA5SiF.json', 'var_call_MB1DQMPUGde9BdwSfFxfMM1s': {'business_refs': [], 'ref_to_state': {}}}

exec(code, env_args)
