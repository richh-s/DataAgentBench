code = """import json, pandas as pd

def load(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r') as f:
            return json.load(f)
    return path_or_obj

def norm_id(s):
    if s is None:
        return None
    s = str(s).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

contracts = pd.DataFrame(load(var_call_JRfGbdNmZXLgeTezqQyt9uOt))
opps = pd.DataFrame(load(var_call_MNhDz1bgk2bZcm6qiDrnVB29))
orders = pd.DataFrame(load(var_call_fP8xrrqSUSrO1Vy17WgnY07H))
order_items = pd.DataFrame(load(var_call_4PBHJt1Rgx8O4enmPcPLjesa))

for df, cols in [(contracts,['ContractId']), (opps,['OpportunityId','ContractID__c','AccountId','OwnerId']), (orders,['OrderId','AccountId','OwnerId']), (order_items,['OrderId'])]:
    for c in cols:
        df[c] = df[c].apply(norm_id)

# dates
start = pd.to_datetime('2022-06-25')
end = pd.to_datetime('2022-11-25')
contracts['CompanySignedDate'] = pd.to_datetime(contracts['CompanySignedDate'], errors='coerce')
elig_contracts = set(contracts.loc[(contracts['CompanySignedDate']>=start) & (contracts['CompanySignedDate']<=end), 'ContractId'].dropna())

opps['ContractID__c'] = opps['ContractID__c'].replace({'None':None,'nan':None})
elig_opps = opps[opps['ContractID__c'].isin(elig_contracts)].copy()
elig_accounts = set(elig_opps['AccountId'].dropna())

# eligible orders: those whose AccountId is in eligible_accounts
elig_orders = orders[orders['AccountId'].isin(elig_accounts)][['OrderId','OwnerId']].copy()

# join order items and sum sales by order then owner
order_items['Quantity'] = pd.to_numeric(order_items['Quantity'], errors='coerce')
order_items['UnitPrice'] = pd.to_numeric(order_items['UnitPrice'], errors='coerce')
order_items['sales'] = order_items['Quantity'] * order_items['UnitPrice']

sales_by_order = order_items.groupby('OrderId', as_index=False)['sales'].sum()
merged = elig_orders.merge(sales_by_order, on='OrderId', how='inner')

sales_by_owner = merged.groupby('OwnerId', as_index=False)['sales'].sum().sort_values('sales', ascending=False)

top_owner = None
if not sales_by_owner.empty:
    top_owner = sales_by_owner.iloc[0]['OwnerId']

print('__RESULT__:')
print(json.dumps({'top_agent_id': top_owner}))"""

env_args = {'var_call_JRfGbdNmZXLgeTezqQyt9uOt': 'file_storage/call_JRfGbdNmZXLgeTezqQyt9uOt.json', 'var_call_S6iCHJyqS4FhXlMMwNgYzjVt': 'file_storage/call_S6iCHJyqS4FhXlMMwNgYzjVt.json', 'var_call_fP8xrrqSUSrO1Vy17WgnY07H': 'file_storage/call_fP8xrrqSUSrO1Vy17WgnY07H.json', 'var_call_4PBHJt1Rgx8O4enmPcPLjesa': 'file_storage/call_4PBHJt1Rgx8O4enmPcPLjesa.json', 'var_call_MEfd8t6MWNIFEKEeUTrFzJrw': {'need_more': 'Opportunity.AccountId missing'}, 'var_call_MNhDz1bgk2bZcm6qiDrnVB29': 'file_storage/call_MNhDz1bgk2bZcm6qiDrnVB29.json'}

exec(code, env_args)
