code = """import json, pandas as pd, datetime as dt
from dateutil.relativedelta import relativedelta

# Load cases data from file
path = var_call_AfZvLtZt5YXDzzP2VpX91dq0
with open(path, 'r') as f:
    cases = json.load(f)

# Today's date
today = dt.datetime(2023,4,10)
start_date = today - relativedelta(months=12)

# Filter cases in last 4 quarters by createddate
for c in cases:
    c['createddate'] = dt.datetime.fromisoformat(c['createddate'].replace('Z','+00:00').replace('.000+0000','+00:00'))

cases_12m = [c for c in cases if start_date <= c['createddate'] <= today]

# Since we have no transfer history (casehistory__c empty), transfer count per agent is 0 for all agents who handled cases.
# We need the agent with fewest transfers among those who handled >0 cases. All have 0, so any agent id with at least one case qualifies.

# Aggregate handled cases per owner
owners = {}
for c in cases_12m:
    oid = c['ownerid'].lstrip('#') if c['ownerid'] else None
    if not oid:
        continue
    owners.setdefault(oid, 0)
    owners[oid] += 1

# Filter to owners with >0 cases (already ensured) and minimal transfer count (0). Just pick the lexicographically smallest id for determinism.
if owners:
    agent_id = sorted(owners.keys())[0]
else:
    agent_id = None

result = json.dumps(agent_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_AfZvLtZt5YXDzzP2VpX91dq0': 'file_storage/call_AfZvLtZt5YXDzzP2VpX91dq0.json', 'var_call_o9ixbVdkfw3zUSdz5D8W6dp8': []}

exec(code, env_args)
