code = """import json
from datetime import datetime

records = var_call_xdXrAmqF15chKV7RSA2MXY2r

# Clean and compute days between created_date and company_signed_date
from collections import defaultdict

owner_days = defaultdict(list)

for r in records:
    owner = r.get('owner_id')
    if owner is None:
        continue
    owner_clean = owner.strip()
    if owner_clean.startswith('#'):
        owner_clean = owner_clean[1:]
    # parse created_date
    cd_str = r.get('created_date')
    try:
        # format: 2023-04-25T10:45:30.000+0000
        created_dt = datetime.strptime(cd_str, '%Y-%m-%dT%H:%M:%S.%f%z')
    except Exception:
        # try without milliseconds
        created_dt = datetime.strptime(cd_str, '%Y-%m-%dT%H:%M:%S%z')
    # parse company_signed_date (date only)
    cs_str = r.get('company_signed_date')
    company_signed_dt = datetime.strptime(cs_str, '%Y-%m-%d')
    # Use date difference (company_signed_date - created_date.date())
    delta = (company_signed_dt.date() - created_dt.date()).days
    owner_days[owner_clean].append(delta)

# compute average per owner
avg_per_owner = {}
for owner, days in owner_days.items():
    if len(days) == 0:
        continue
    avg = sum(days) / len(days)
    avg_per_owner[owner] = avg

# find owner with minimum average turnaround
if not avg_per_owner:
    result_agent = None
else:
    # in case of tie, choose lexicographically smallest id
    min_avg = min(avg_per_owner.values())
    candidates = [o for o, a in avg_per_owner.items() if a == min_avg]
    result_agent = sorted(candidates)[0]

print("__RESULT__:")
print(json.dumps(result_agent))"""

env_args = {'var_call_xdXrAmqF15chKV7RSA2MXY2r': [{'opp_id': '#006Wt000007BChmIAG', 'owner_id': '005Wt000003NJgAIAW', 'created_date': '2023-04-25T10:45:30.000+0000', 'contract_id': '#800Wt00000DE9FFIA1', 'company_signed_date': '2023-06-13'}, {'opp_id': '006Wt000007BDApIAO', 'owner_id': '005Wt000003NISMIA4', 'created_date': '2023-04-10T10:15:30.000+0000', 'contract_id': '800Wt00000DE8sgIAD', 'company_signed_date': '2023-10-13'}, {'opp_id': '006Wt000007BHPhIAO', 'owner_id': '#005Wt000003NEa3IAG', 'created_date': '2023-04-15T09:12:34.000+0000', 'contract_id': '800Wt00000DE9ryIAD', 'company_signed_date': '2023-09-30'}]}

exec(code, env_args)
