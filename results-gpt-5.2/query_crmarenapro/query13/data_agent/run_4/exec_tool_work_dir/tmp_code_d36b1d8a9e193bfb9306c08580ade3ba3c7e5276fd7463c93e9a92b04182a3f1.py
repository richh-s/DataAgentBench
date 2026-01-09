code = """import json, pandas as pd
from datetime import date

def load(var):
    if isinstance(var, str):
        with open(var, 'r') as f:
            return json.load(f)
    return var

def norm_id(x):
    if x is None:
        return None
    s = str(x).strip()
    if s.lower() == 'none' or s == '':
        return None
    if s.startswith('#'):
        s = s[1:]
    return s

contracts = pd.DataFrame(load(var_call_pdg4yf8YmfDXELpAdP5NRidr))
opps = pd.DataFrame(load(var_call_iou4P3B4TJMrYCAh7EF3iSDs))
orders = pd.DataFrame(load(var_call_VJp8gzQL5OSlYkOz3jOGkolc))
orderitems = pd.DataFrame(load(var_call_FsNv81Q35UYsPhVH9Yn5TPpA))

# normalize ids
contracts['c_id'] = contracts['Id'].map(norm_id)
opps['ContractID__c_norm'] = opps['ContractID__c'].map(norm_id)
orders['o_id'] = orders['Id'].map(norm_id)
orders['OwnerId_norm'] = orders['OwnerId'].map(norm_id)
orderitems['OrderId_norm'] = orderitems['OrderId'].map(norm_id)

# signed date window: past five months from 2022-11-25 => 2022-06-25 to 2022-11-25
start = pd.to_datetime('2022-06-25')
end = pd.to_datetime('2022-11-25')
contracts['CompanySignedDate_dt'] = pd.to_datetime(contracts['CompanySignedDate'], errors='coerce')
eligible_contracts = set(contracts.loc[(contracts['CompanySignedDate_dt']>=start) & (contracts['CompanySignedDate_dt']<=end), 'c_id'].dropna())

# eligible opportunities
eligible_opps = set(opps.loc[opps['ContractID__c_norm'].isin(eligible_contracts), 'Id'].map(norm_id).dropna())

# Order-opportunity link not provided; assume OrderId corresponds to OpportunityId (common in synthetic datasets)
orders['opp_like_id'] = orders['o_id']
eligible_orders = orders.loc[orders['opp_like_id'].isin(eligible_opps), ['o_id','OwnerId_norm']]

# compute sales per order: sum(qty*unitprice)
for col in ['Quantity','UnitPrice']:
    orderitems[col] = pd.to_numeric(orderitems[col], errors='coerce')
orderitems['amount'] = orderitems['Quantity'] * orderitems['UnitPrice']
order_sales = orderitems.groupby('OrderId_norm', as_index=False)['amount'].sum()

merged = eligible_orders.merge(order_sales, left_on='o_id', right_on='OrderId_norm', how='inner')
agent_sales = merged.groupby('OwnerId_norm', as_index=False)['amount'].sum().sort_values('amount', ascending=False)

top_agent = None
if len(agent_sales):
    top_agent = agent_sales.iloc[0]['OwnerId_norm']

print('__RESULT__:')
print(json.dumps({'top_agent_id': top_agent}))"""

env_args = {'var_call_pdg4yf8YmfDXELpAdP5NRidr': 'file_storage/call_pdg4yf8YmfDXELpAdP5NRidr.json', 'var_call_iou4P3B4TJMrYCAh7EF3iSDs': 'file_storage/call_iou4P3B4TJMrYCAh7EF3iSDs.json', 'var_call_VJp8gzQL5OSlYkOz3jOGkolc': 'file_storage/call_VJp8gzQL5OSlYkOz3jOGkolc.json', 'var_call_FsNv81Q35UYsPhVH9Yn5TPpA': 'file_storage/call_FsNv81Q35UYsPhVH9Yn5TPpA.json'}

exec(code, env_args)
