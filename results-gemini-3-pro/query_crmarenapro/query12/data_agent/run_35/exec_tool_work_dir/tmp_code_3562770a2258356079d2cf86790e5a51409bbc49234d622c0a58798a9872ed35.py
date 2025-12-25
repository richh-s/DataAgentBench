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

# Find the contract(s)
target_contracts = {}
for c in contracts:
    c_id = clean_id(c.get('Id'))
    d_str = c.get('CompanySignedDate')
    if d_str:
        try:
            dt = datetime.strptime(d_str, "%Y-%m-%d")
            if dt.year == 2023 and dt.month == 4:
                target_contracts[c_id] = dt
        except:
            pass

print(f"Target Contracts: {target_contracts}")

# Find linked opportunity
found_opps = []
for opp in opportunities:
    c_id = clean_id(opp.get('ContractID__c'))
    if c_id in target_contracts:
        created_str = opp.get('CreatedDate')
        created_dt = datetime.strptime(created_str[:10], "%Y-%m-%d")
        signed_dt = target_contracts[c_id]
        days = (signed_dt - created_dt).days
        found_opps.append({
            'OppId': opp.get('Id'),
            'OwnerId': clean_id(opp.get('OwnerId')),
            'Days': days,
            'Created': created_str,
            'Signed': str(signed_dt.date())
        })

print("__RESULT__:")
print(json.dumps(found_opps))"""

env_args = {'var_function-call-8504362619409159086': 'file_storage/function-call-8504362619409159086.json', 'var_function-call-8504362619409159979': 'file_storage/function-call-8504362619409159979.json', 'var_function-call-37697407624885467': [{'AgentId': '005Wt000003NDEBIA4', 'AvgCycle': 304.0, 'Count': 1}], 'var_function-call-3494831580389978234': {'april_contracts_count': 1, 'linked_opps': 1}, 'var_function-call-6320255451467349316': 'Done', 'var_function-call-9956766205769855697': [['2023-10', 9], ['2022-09', 7], ['2021-09', 5], ['2021-06', 5], ['2023-02', 5], ['2022-03', 5], ['2022-12', 5], ['2023-08', 5], ['2024-07', 5], ['2022-06', 5], ['2021-01', 5], ['2023-01', 5], ['2021-07', 4], ['2023-07', 4], ['2024-04', 4], ['2022-01', 4], ['2021-11', 4], ['2021-08', 4], ['2023-09', 4], ['2023-06', 4], ['2020-11', 4], ['2020-08', 4], ['2023-11', 4], ['2022-04', 3], ['2021-04', 3], ['2023-12', 3], ['2021-12', 3], ['2020-06', 3], ['2023-05', 3], ['2023-03', 3], ['2021-05', 2], ['2020-12', 2], ['2022-02', 2], ['2024-05', 2], ['2021-02', 2], ['2021-10', 2], ['2021-03', 2], ['2022-08', 2], ['2020-09', 2], ['2024-09', 2], ['2024-02', 2], ['2022-11', 2], ['2024-03', 1], ['2022-07', 1], ['2024-08', 1], ['2022-10', 1], ['2024-01', 1], ['2022-05', 1], ['2023-04', 1], ['2024-06', 1]], 'var_function-call-13847199770941298947': 'file_storage/function-call-13847199770941298947.json'}

exec(code, env_args)
