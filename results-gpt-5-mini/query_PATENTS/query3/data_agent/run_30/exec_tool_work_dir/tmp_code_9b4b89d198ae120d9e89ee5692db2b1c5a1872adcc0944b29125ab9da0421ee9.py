code = """import json, re
path = var_call_dEoQDTzU3g8MBJxJTTtcYTmC
with open(path, 'r') as f:
    records = json.load(f)
pubs = set()
# regex to match patterns like US-1234567-A1, WO-..., TW-..., US-200... etc
re_pub = re.compile(r'\b[A-Z]{2}-[0-9]{4,}[A-Z0-9\-]*\b')
for rec in records:
    pi = rec.get('Patents_info') or ''
    for m in re_pub.finditer(pi.upper()):
        pubs.add(m.group(0))
# also look for patterns like 'publication number US-11421276-B2' captured already
res = sorted(pubs)
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_5I4DtjpcM4Fv7fjmRPlhswNj': 'file_storage/call_5I4DtjpcM4Fv7fjmRPlhswNj.json', 'var_call_3VyetCwrZExI2Xpet9Um2Z3I': 'file_storage/call_3VyetCwrZExI2Xpet9Um2Z3I.json', 'var_call_aQiaaKewuvuNUgNV4DvyEt09': {'pairs': [], 'codes': []}, 'var_call_dEoQDTzU3g8MBJxJTTtcYTmC': 'file_storage/call_dEoQDTzU3g8MBJxJTTtcYTmC.json'}

exec(code, env_args)
