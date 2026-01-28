code = """import json, re
with open(var_call_2KWjt8JKvALQF3B1Xrp7spAo, 'r') as f:
    records = json.load(f)

months_h2 = ['jul','july','aug','august','sep','sept','september','oct','october','nov','november','dec','december']

samples = []
country_counter = {}
for r in records:
    gd = (r.get('grant_date') or '').lower()
    if '2019' not in gd:
        continue
    if not any(m in gd for m in months_h2):
        continue
    pi = r.get('Patents_info','')
    # extract token patterns like 'from XX' or ' (no. DE-' etc
    m1 = re.search(r'from\s+([A-Z]{2})', pi)
    m2 = re.search(r'\b([A-Z]{2})[-\d]', pi)
    m3 = re.search(r'from\s+([A-Za-z]+)', pi)
    country = None
    if m1:
        country = m1.group(1)
    elif m2:
        country = m2.group(1)
    elif m3:
        country = m3.group(1)
    else:
        # try find full 'Germany' word
        if 'germany' in pi.lower() or 'deutsch' in pi.lower():
            country = 'DE'
    if country:
        country_counter[country] = country_counter.get(country,0)+1
    if len(samples) < 50:
        samples.append({'grant_date': r.get('grant_date'), 'Patents_info': pi[:200]})

out = {'country_counts': country_counter, 'samples': samples[:50]}
print('__RESULT__:')
import json
print(json.dumps(out))"""

env_args = {'var_call_2KWjt8JKvALQF3B1Xrp7spAo': 'file_storage/call_2KWjt8JKvALQF3B1Xrp7spAo.json', 'var_call_DoMQ2XCAoGqwJKBJyG5u70sk': {'groups': [], 'group_codes': []}}

exec(code, env_args)
