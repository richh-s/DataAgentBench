code = """import json, pandas as pd, datetime as dt
from dateutil.relativedelta import relativedelta

path = var_call_AfZvLtZt5YXDzzP2VpX91dq0
with open(path, 'r') as f:
    cases = json.load(f)

# convert today to aware UTC
today = dt.datetime(2023,4,10, tzinfo=dt.timezone.utc)
start_date = today - relativedelta(months=12)

for c in cases:
    cd_raw = c['createddate']
    if cd_raw.endswith('+0000'):
        cd_raw = cd_raw.replace('.000+0000','+00:00') if '.000+0000' in cd_raw else cd_raw[:-5] + '+00:00'
    c['createddate'] = dt.datetime.fromisoformat(cd_raw)

cases_12m = [c for c in cases if start_date <= c['createddate'] <= today]

owners = {}
for c in cases_12m:
    oid = c['ownerid']
    if oid:
        oid = oid.lstrip('#')
        owners.setdefault(oid, 0)
        owners[oid] += 1

agent_id = sorted(owners.keys())[0] if owners else None

import json
result = json.dumps(agent_id)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_AfZvLtZt5YXDzzP2VpX91dq0': 'file_storage/call_AfZvLtZt5YXDzzP2VpX91dq0.json', 'var_call_o9ixbVdkfw3zUSdz5D8W6dp8': []}

exec(code, env_args)
