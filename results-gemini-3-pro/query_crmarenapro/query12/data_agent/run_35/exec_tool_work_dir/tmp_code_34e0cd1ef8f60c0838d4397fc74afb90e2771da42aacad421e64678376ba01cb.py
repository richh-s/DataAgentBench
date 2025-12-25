code = """import json
from datetime import datetime

with open(locals()['var_function-call-8504362619409159086'], 'r') as f:
    opportunities = json.load(f)

with open(locals()['var_function-call-8504362619409159979'], 'r') as f:
    contracts = json.load(f)

def clean_id(x):
    if not isinstance(x, str):
        return x
    x = x.strip()
    if x.startswith('#'):
        return x[1:]
    return x

# Count contracts in April 2023
april_contracts = []
for c in contracts:
    c_id = clean_id(c.get('Id'))
    signed_date = c.get('CompanySignedDate')
    if signed_date:
        try:
            dt = datetime.strptime(signed_date, "%Y-%m-%d")
            if dt.year == 2023 and dt.month == 4:
                april_contracts.append(c_id)
        except:
            pass

print(f"Contracts in April 2023: {len(april_contracts)}")

# Count opportunities linked to these contracts
linked_opps = 0
opps_with_contracts = 0
april_contract_set = set(april_contracts)

for opp in opportunities:
    c_id = clean_id(opp.get('ContractID__c'))
    if c_id and c_id != 'None':
        opps_with_contracts += 1
        if c_id in april_contract_set:
            linked_opps += 1

print(f"Opportunities with any contract: {opps_with_contracts}")
print(f"Opportunities linked to April 2023 contracts: {linked_opps}")
print("__RESULT__:")
print(json.dumps({"april_contracts_count": len(april_contracts), "linked_opps": linked_opps}))"""

env_args = {'var_function-call-8504362619409159086': 'file_storage/function-call-8504362619409159086.json', 'var_function-call-8504362619409159979': 'file_storage/function-call-8504362619409159979.json', 'var_function-call-37697407624885467': [{'AgentId': '005Wt000003NDEBIA4', 'AvgCycle': 304.0, 'Count': 1}]}

exec(code, env_args)
