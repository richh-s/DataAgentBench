code = """import json
from datetime import datetime, timezone
# var_call_HZa7QwdJTW30uhZEzXEOoVYu is available from previous query
rows = var_call_HZa7QwdJTW30uhZEzXEOoVYu

# Helper to clean IDs
def clean_id(s):
    if s is None:
        return s
    s = s.strip()
    if s.startswith('#'):
        return s[1:]
    return s

# Parse dates and compute days difference
results = {}
for r in rows:
    owner = clean_id(r.get('OwnerId'))
    created = r.get('CreatedDate')
    signed = r.get('CompanySignedDate')
    if not owner or not created or not signed:
        continue
    # Parse created datetime like '2023-04-10T10:15:30.000+0000'
    try:
        # Normalize timezone +0000 -> +00:00
        cd = created
        if '+' in cd:
            base, tz = cd.split('+', 1)
            if len(tz) == 4:
                tz = tz[:2] + ':' + tz[2:]
            cd_norm = base + '+' + tz
            created_dt = datetime.fromisoformat(cd_norm)
        elif cd.endswith('Z'):
            created_dt = datetime.fromisoformat(cd.replace('Z', '+00:00'))
        else:
            created_dt = datetime.fromisoformat(cd)
        # make naive by converting to UTC and dropping tzinfo
        if created_dt.tzinfo is not None:
            created_dt = created_dt.astimezone(timezone.utc).replace(tzinfo=None)
    except Exception:
        # Fallback: parse date portion only
        created_dt = datetime.fromisoformat(created.split('T')[0])
    # Parse signed date YYYY-MM-DD (naive date at midnight)
    try:
        signed_dt = datetime.fromisoformat(signed)
    except Exception:
        signed_dt = datetime.fromisoformat(signed.strip())
    delta_days = (signed_dt - created_dt).total_seconds() / 86400.0
    results.setdefault(owner, []).append(delta_days)

# Compute averages
averages = {owner: sum(vals)/len(vals) for owner, vals in results.items()}
# Find owner with minimum average
if averages:
    quickest_owner = min(averages, key=lambda k: averages[k])
else:
    quickest_owner = None

print("__RESULT__:")
print(json.dumps(quickest_owner))"""

env_args = {'var_call_HZa7QwdJTW30uhZEzXEOoVYu': [{'OpportunityId': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}, {'OpportunityId': '006Wt000007BHPhIAO', 'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}]}

exec(code, env_args)
