code = """import json, re
from collections import defaultdict

path = var_call_92Gv62Hc06tyNHGMNt0zYCF0
with open(path) as f:
    data = json.load(f)

uc_pubnums = set()

for rec in data:
    info = rec.get('Patents_info','')
    m = re.search(r'pub\. number ([A-Z]{2}-[^,\.]+)', info)
    if not m:
        m = re.search(r'publication number ([A-Z]{2}-[^,\.]+)', info)
    if not m:
        continue
    pubnum = m.group(1)
    uc_pubnums.add(pubnum)

all_recs = data
citers = defaultdict(lambda: set())

for rec in all_recs:
    info = rec.get('Patents_info','')
    m_ass = re.search(r'assigned to ([^,\.]+)', info)
    if not m_ass:
        m_ass = re.search(r'owned by ([^,\.]+)', info)
    if not m_ass:
        m_ass = re.search(r'held by ([^,\.]+)', info)
    assignee = m_ass.group(1).strip() if m_ass else None

    try:
        cites = json.loads(rec.get('citation') or '[]')
    except Exception:
        cites = []
    cited_pubnums = {c.get('publication_number') for c in cites if c.get('publication_number')}
    if not (cited_pubnums & uc_pubnums):
        continue

    if not assignee or 'UNIV CALIFORNIA' in assignee.upper():
        continue

    try:
        cpc_list = json.loads(rec.get('cpc') or '[]')
    except Exception:
        cpc_list = []
    primary_codes = [c['code'] for c in cpc_list if c.get('first')]
    for code in primary_codes:
        citers[assignee].add(code)

result = {assignee: sorted(list(codes)) for assignee, codes in citers.items()}

import json as _json
out = _json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_PKlDk6KpnLet2XnliwvIGrmA': [], 'var_call_92Gv62Hc06tyNHGMNt0zYCF0': 'file_storage/call_92Gv62Hc06tyNHGMNt0zYCF0.json'}

exec(code, env_args)
