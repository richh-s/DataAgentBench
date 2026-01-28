code = """import json
from datetime import datetime
from collections import defaultdict

records = var_call_asNa9GQyYnN3quFjn5YVb02X
sums = defaultdict(int)
counts = defaultdict(int)
for r in records:
    owner = r.get('owner_id')
    created_str = r.get('created_date')
    csd_str = r.get('company_signed_date')
    if not owner or not created_str or not csd_str:
        continue
    try:
        created_dt = datetime.strptime(created_str, '%Y-%m-%dT%H:%M:%S.%f%z')
    except ValueError:
        try:
            created_dt = datetime.strptime(created_str, '%Y-%m-%dT%H:%M:%S%z')
        except ValueError:
            continue
    try:
        csd_date = datetime.strptime(csd_str, '%Y-%m-%d').date()
    except ValueError:
        continue
    days = (csd_date - created_dt.date()).days
    sums[owner] += days
    counts[owner] += 1

averages = {}
for owner in sums:
    averages[owner] = sums[owner] / counts[owner]

if not averages:
    result = None
else:
    min_avg = min(averages.values())
    candidates = [o for o,a in averages.items() if a == min_avg]
    best = sorted(candidates)[0]
    result = best

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_asNa9GQyYnN3quFjn5YVb02X': [{'opp_id': '#006Wt000007BChmIAG', 'owner_id': '005Wt000003NJgAIAW', 'created_date': '2023-04-25T10:45:30.000+0000', 'contract_id': '#800Wt00000DE9FFIA1', 'company_signed_date': '2023-06-13'}, {'opp_id': '006Wt000007BDApIAO', 'owner_id': '005Wt000003NISMIA4', 'created_date': '2023-04-10T10:15:30.000+0000', 'contract_id': '800Wt00000DE8sgIAD', 'company_signed_date': '2023-10-13'}, {'opp_id': '006Wt000007BHPhIAO', 'owner_id': '005Wt000003NEa3IAG', 'created_date': '2023-04-15T09:12:34.000+0000', 'contract_id': '800Wt00000DE9ryIAD', 'company_signed_date': '2023-09-30'}]}

exec(code, env_args)
