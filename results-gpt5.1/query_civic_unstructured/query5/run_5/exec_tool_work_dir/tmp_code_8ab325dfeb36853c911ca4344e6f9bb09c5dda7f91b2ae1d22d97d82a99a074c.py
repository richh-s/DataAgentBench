code = """import json, re
from pathlib import Path

p = Path(var_call_IcBZilRVasxcAhdwzTJthD9M)
with p.open() as f:
    funding = json.load(f)

disaster_keywords = ['(FEMA', '(CalOES', '(CalJPIA']

total = 0
for row in funding:
    name = row.get('Project_Name','')
    if any(k in name for k in disaster_keywords):
        # assume all these are disaster-related; no year info in funding so include all
        total += int(row.get('Amount',0))

print('__RESULT__:')
print(json.dumps({'total_disaster_funding_all_years': total}))"""

env_args = {'var_call_HA3G875VP1SZt1QW81T7quiX': 'file_storage/call_HA3G875VP1SZt1QW81T7quiX.json', 'var_call_IcBZilRVasxcAhdwzTJthD9M': 'file_storage/call_IcBZilRVasxcAhdwzTJthD9M.json'}

exec(code, env_args)
