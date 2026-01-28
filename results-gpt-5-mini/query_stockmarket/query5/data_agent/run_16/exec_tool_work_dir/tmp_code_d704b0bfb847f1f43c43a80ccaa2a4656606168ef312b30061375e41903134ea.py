code = """import json
p1 = var_call_M0U5buiAvISz429MtqwKvqqA
p2 = var_call_4e328mmHfSVOI68hPDqpaEt8
d1 = json.load(open(p1))
d2 = json.load(open(p2))
set2 = set(d2)
s = [rec['Symbol'] for rec in d1 if rec['Symbol'] in set2]
out = {'count': len(s), 'symbols_sample': s[:200]}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_M0U5buiAvISz429MtqwKvqqA': 'file_storage/call_M0U5buiAvISz429MtqwKvqqA.json', 'var_call_4e328mmHfSVOI68hPDqpaEt8': 'file_storage/call_4e328mmHfSVOI68hPDqpaEt8.json'}

exec(code, env_args)
