code = """import json, re
from datetime import datetime
path = var_call_6s1Hx5RlvxTCOOHk3gPsx0tp
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

def has_de(pi):
    if not pi: return False
    s = pi.upper()
    if 'GERMANY' in s: return True
    if re.search(r'\bDE\b', s): return True
    if re.search(r'DE[-_]\d', s): return True
    if ' FROM DE' in s or 'DE,' in s: return True
    return False

res = []
for r in records:
    gd = r.get('grant_date','')
    if '2019' not in str(gd):
        continue
    if has_de(r.get('Patents_info','')):
        res.append({'id': r.get('id'), 'Patents_info': r.get('Patents_info'), 'grant_date': r.get('grant_date')})

print('__RESULT__:')
print(json.dumps({'count': len(res), 'examples': res[:20]}, ensure_ascii=False))"""

env_args = {'var_call_DOJ8NTBO8k3pUFTiKas6Zehx': 'file_storage/call_DOJ8NTBO8k3pUFTiKas6Zehx.json', 'var_call_3x0kyDCCcHjS363jdKiOeLf0': {'groups': []}, 'var_call_6s1Hx5RlvxTCOOHk3gPsx0tp': 'file_storage/call_6s1Hx5RlvxTCOOHk3gPsx0tp.json', 'var_call_B7VsHRM5f0Jdk9w0iMgkWsUb': {'symbols': [], 'groups': []}}

exec(code, env_args)
