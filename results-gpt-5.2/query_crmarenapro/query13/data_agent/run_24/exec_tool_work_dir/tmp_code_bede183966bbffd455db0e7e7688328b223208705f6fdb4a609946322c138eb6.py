code = """import json, pandas as pd
from datetime import date

# load big json files

def load(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r') as f:
            return json.load(f)
    return path_or_obj

contracts = pd.DataFrame(load(var_call_JRfGbdNmZXLgeTezqQyt9uOt))
opps = pd.DataFrame(load(var_call_S6iCHJyqS4FhXlMMwNgYzjVt))
orders = pd.DataFrame(load(var_call_fP8xrrqSUSrO1Vy17WgnY07H))
order_items = pd.DataFrame(load(var_call_4PBHJt1Rgx8O4enmPcPLjesa))

# normalize ids: strip whitespace and leading '#'

def norm_id(s):
    if s is None:
        return None
    s = str(s).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

for df, cols in [(contracts,['ContractId']), (opps,['OpportunityId','ContractID__c','OwnerId']), (orders,['OrderId','OwnerId']), (order_items,['OrderId'])]:
    for c in cols:
        df[c] = df[c].apply(norm_id)

# date filter: past five months from 2022-11-25 => start 2022-06-25
start = pd.to_datetime('2022-06-25')
end = pd.to_datetime('2022-11-25')
contracts['CompanySignedDate'] = pd.to_datetime(contracts['CompanySignedDate'], errors='coerce')
eligible_contracts = contracts[(contracts['CompanySignedDate']>=start) & (contracts['CompanySignedDate']<=end)][['ContractId']]

# eligible opportunities
opps['ContractID__c'] = opps['ContractID__c'].replace({'None':None,'nan':None})
elig_opps = opps.merge(eligible_contracts, left_on='ContractID__c', right_on='ContractId', how='inner')

# eligible accounts from those opportunities
# if no eligible opps, result empty
eligible_accounts = set()
if not elig_opps.empty:
    # Opportunity table has AccountId but we didn't fetch; need it. We'll fallback by using orders only where their AccountId matches contracts? can't.
    pass

# We need Opportunity.AccountId to link to Order.AccountId. Not fetched; derive by extra query? can't here.

print('__RESULT__:')
print(json.dumps({'need_more':'Opportunity.AccountId missing'}))"""

env_args = {'var_call_JRfGbdNmZXLgeTezqQyt9uOt': 'file_storage/call_JRfGbdNmZXLgeTezqQyt9uOt.json', 'var_call_S6iCHJyqS4FhXlMMwNgYzjVt': 'file_storage/call_S6iCHJyqS4FhXlMMwNgYzjVt.json', 'var_call_fP8xrrqSUSrO1Vy17WgnY07H': 'file_storage/call_fP8xrrqSUSrO1Vy17WgnY07H.json', 'var_call_4PBHJt1Rgx8O4enmPcPLjesa': 'file_storage/call_4PBHJt1Rgx8O4enmPcPLjesa.json'}

exec(code, env_args)
